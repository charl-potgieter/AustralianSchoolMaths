# from __future__ import annotations prevents raising an rror of a return value
# of type class before completing the class definition, for example
# per_topic_code returns type Formuals before the definition for Formulas is
# conmpelte
from __future__ import annotations
import pandas as pd
import hashlib
from enum import Enum, auto
from formatters import WebSiteFormatter


class HighlightType(Enum):
    NONE = auto()
    FORMULA_SHEET = auto()
    PROOF_REQUIRED = auto()


class TableType(Enum):
    SIMPLE = auto()
    FINANCIAL = auto()
    CALCULUS = auto()


class Formulas:
    def __init__(self, formula_data: pd.DataFrame):
        self._data = formula_data

    @property
    def data(self) -> pd.DataFrame:
        return self._data

    @property
    def contains_data(self):
        return not self._data.empty

    @property
    def unique_states(self) -> list[str]:
        """Returns unique states in formula data"""
        return_value = self.data["State"]
        return_value = return_value.unique().tolist()
        return return_value

    @property
    def unique_topic_codes(self) -> list[str]:
        return_value = self.data["Code"]
        return_value = return_value.unique().tolist()
        return return_value

    @property
    def unique_state_and_topic_codes(self) -> list[tuple[str, str]]:
        return_value = self.data[["State", "Code"]].drop_duplicates().values
        return_value = return_value.tolist()
        return return_value

    def per_state_and_topic_code(self, state: str, topic: str) -> Formulas:
        new_data = pd.DataFrame(
            self.data[
                (self.data["State"] == state) & (self.data["Code"] == topic)
            ].copy()
        )
        new_formulas = Formulas(new_data)
        return new_formulas

    @property
    def contains_formula_sheet_items(self) -> bool:
        return_value = bool(self.data["On_formula_sheet"].any())
        return return_value

    @property
    def contains_proof_required_items(self) -> bool:
        return_value = bool(self.data["Proof_required"].any())
        return return_value

    @property
    def formula_sheet_items(self) -> list:
        return list(self.data.loc[self.data["On_formula_sheet"], "Formula"])

    @property
    def proof_required_items(self) -> list:
        return list(self.data.loc[self.data["Proof_required"], "Formula"])

    def to_formula_display_string(
        self, table_type: TableType, formatter: WebSiteFormatter
    ) -> str:
        formula_display = _FormulaDisplay(self, table_type, formatter)
        return formula_display._to_string()

    @property
    def _stable_uuid(self) -> str:
        """Returns a stable identifier based on the formula data pandas
        dataframe.  This can be used if formulas are converted to a pandas
        styler to prevent an id from being auto-generated which causes the
        flagging of unecessary git differences.
        """
        hash_input = self._data.to_csv(index=False)
        h = hashlib.sha256(hash_input.encode("utf-8")).hexdigest()[:16]
        return h


class _FormulaDisplay:
    """Represents a string containing display of formulas in table format
    for inclusion in website generator markdown file, potentially containing
    multiple tabs.  String may contain html and markdown
    """

    def __init__(
        self,
        formulas: Formulas,
        table_type: TableType,
        formatter: WebSiteFormatter,
    ):
        self._formulas = formulas
        self._table_type = table_type
        self._formatter = formatter

    def _to_string(self) -> str:
        if not self._formulas.contains_data:
            return self._empty_display()
        elif not self._requires_tabs:
            return self._generate_single_table_string(HighlightType.NONE)
        else:
            return self._generate_multi_tab_string()

    @property
    def _requires_tabs(self) -> bool:
        """Returns true if table has / requires tabs"""
        return (
            self._formulas.contains_formula_sheet_items
            or self._formulas.contains_proof_required_items
        )

    def _empty_display(self) -> str:
        return ""

    def _generate_single_table_string(
        self, highlight_type: HighlightType
    ) -> str:
        if self._table_type == TableType.SIMPLE:
            table = _FormulaTableSimple(self._formulas, highlight_type)
        elif self._table_type == TableType.FINANCIAL:
            table = _FormulaTableFinancial(self._formulas, highlight_type)
        elif self._table_type == TableType.CALCULUS:
            table = _FormulaTableCalculus(self._formulas, highlight_type)
        else:
            raise TypeError("Incorrect table type")
        return table._to_string()

    def _generate_multi_tab_string(self) -> str:
        tab_id = "tab" + self._formulas._stable_uuid
        return_value = self._formatter.tabs_start(tab_id)
        return_value += self._tab_string_standard_view()
        if self._formulas.contains_formula_sheet_items:
            return_value += self._tab_string_formula_sheet()
        if self._formulas.contains_proof_required_items:
            return_value += self._tab_string_proof_required()
        return_value += self._formatter.tabs_end()
        return return_value

    def _tab_string_standard_view(self) -> str:
        return_value = self._formatter.tab_content(
            "Standard View",
            self._generate_single_table_string(HighlightType.NONE),
        )
        return return_value

    def _tab_string_formula_sheet(self) -> str:
        return_value = self._formatter.tab_content(
            "Formula sheet",
            self._generate_single_table_string(HighlightType.FORMULA_SHEET),
        )
        return return_value

    def _tab_string_proof_required(self) -> str:
        return_value = self._formatter.tab_content(
            "Proof Required",
            self._generate_single_table_string(HighlightType.PROOF_REQUIRED),
        )
        return return_value


class _FormulaTable:
    def __init__(self, formulas: Formulas, highlight_type: HighlightType):
        # This is performed in 3 steps to allow child classes to override
        # parent properties with the _customise_properties method before they
        # are applied to the table
        self._set_table_properties(formulas, highlight_type)
        self._customise_properties()
        self._apply_table_properties()

    def _set_table_properties(
        self, formulas: Formulas, highlight_type: HighlightType
    ):
        self._formulas = formulas
        self._display_data = self._formulas.data
        self._has_hidden_column_headers = False
        self._has_hidden_row_headers = False
        self._highlight_type = highlight_type

    def _customise_properties(self):
        """Hook for subclasses to override properties"""
        pass

    def _apply_table_properties(self):
        self._styled_table = self._create_styled_table()
        self._set_table_header_visibility()
        self._apply_highlights()

    def _create_styled_table(self) -> pd.io.formats.style.Styler:
        return_value = self._display_data.style.set_table_styles(
            [
                {
                    "selector": "th.col_heading",
                    "props": "text-align: left; font-size:1em;",
                },
                {
                    "selector": "td",
                    "props": "text-align: left; font-size:1em;padding: 1.5em;",
                },
            ]
        )
        return return_value

    def _set_table_header_visibility(self):
        if self._has_hidden_column_headers:
            self._styled_table = self._styled_table.hide(axis="columns")
        if self._has_hidden_row_headers:
            self._styled_table = self._styled_table.hide(axis="index")

    def _apply_highlights(self):
        if self._highlight_type == HighlightType.FORMULA_SHEET:
            self._highlight_selected_values(
                items_to_highlight=self._formulas.formula_sheet_items,
                rgba="255,194,10, 0.2",
            )
        elif self._highlight_type == HighlightType.PROOF_REQUIRED:
            self._highlight_selected_values(
                items_to_highlight=self._formulas.proof_required_items,
                rgba="0,150,200, 0.2",
            )

    def _to_string(self) -> str:
        return self._styled_table.to_html(table_uuid=self._stable_uuid)

    @property
    def _stable_uuid(self):
        """Generates a stable id consisting of a highlight type prefix combined
        with the formula table id
        """
        return self._highlight_type.name + self._formulas._stable_uuid

    def _highlight_selected_values(
        self, items_to_highlight: list, rgba: str
    ) -> None:
        format_value = "background-color:rgba(" + rgba + ");"
        default_value = "background-color:rgba(0,0,0,0);"
        self._styled_table.map(
            func=lambda x: format_value
            if x in items_to_highlight
            else default_value
        )


class _FormulaTableSimple(_FormulaTable):
    """Simple formula table implementation of abstract class FormulaTableType"""

    def _customise_properties(self):
        self._display_data = self._formulas.data[["Formula"]]
        self._has_hidden_column_headers = True
        self._has_hidden_row_headers = True


class _FormulaTableFinancial(_FormulaTable):
    pass


class _FormulaTableCalculus(_FormulaTable):
    pass
