# prevents raising an rror of a return value of type class before completing
# the class definition, for example per_topic_code returns type Formuals
# before the definition for Formulas is conmpelte
from __future__ import annotations
import pandas as pd
import hashlib
from formatters import TabFormatter


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

    def to_formula_table_simple(self) -> FormulaTableSimple:
        return FormulaTableSimple(self)


class _FormulaTable:
    def __init__(self, formulas: Formulas):
        # This is performed in 2 steps to allow child classes to override
        # parent properties before they are applied to the table
        self._set_table_properties(formulas)
        self.customise_properties()
        self._apply_table_properties()

    def _set_table_properties(self, formulas: Formulas):
        self.formulas = formulas
        self.dataframe = formulas.data
        self.has_hidden_column_headers = False
        self.has_hidden_row_headers = False
        self._table_tabs = {}

    def customise_properties(self):
        """Hook for subclasses to override properties"""
        pass

    def _apply_table_properties(self):
        self._styled_table = self._create_styled_table()
        self._set_table_header_visibility()

    def _create_styled_table(self) -> pd.io.formats.style.Styler:
        return_value = self.dataframe.style.set_table_styles(
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
        if self.has_hidden_column_headers:
            self._styled_table = self._styled_table.hide(axis="columns")
        if self.has_hidden_row_headers:
            self._styled_table = self._styled_table.hide(axis="index")

    def to_string(self, formatter: TabFormatter) -> str:
        """Returns string format for inclusion in hugo markdown files"""
        if not self.formulas.contains_data:
            return self._empty_table_string()
        elif not self.requires_tabs:
            return self._single_table_string()
        else:
            self._create_table_tabs()
            return self._multi_tab_string(formatter)

    def _empty_table_string(self) -> str:
        return ""

    @property
    def requires_tabs(self) -> bool:
        """Returns true if table has / requires tabs"""
        return (
            self.formulas.contains_formula_sheet_items
            or self.formulas.contains_proof_required_items
        )

    def _single_table_string(self, prefix: str | None = None) -> str:
        self._set_table_header_visibility()
        table_id = self._stable_uuid(prefix)
        return self._styled_table.to_html(table_uuid=table_id)

    def _create_table_tabs(self) -> None:
        self._add_table_tab(
            "Standard view", self._single_table_string("standard")
        )
        if self.formulas.contains_formula_sheet_items:
            self._highlight_values_in_list(
                items_to_highlight=self.formulas.formula_sheet_items,
                rgba="255,194,10, 0.2",
            )
            self._add_table_tab(
                "Formulas sheet", self._single_table_string("formula_sheet")
            )
        if self.formulas.contains_proof_required_items:
            self._highlight_values_in_list(
                items_to_highlight=self.formulas.proof_required_items,
                rgba="0,150,200, 0.2",
            )
            self._add_table_tab(
                "Proof required", self._single_table_string("proof")
            )

    def _multi_tab_string(self, formatter: TabFormatter) -> str:
        tab_id = self._stable_uuid("tab")
        return_value = formatter.format_tabs_start(tab_id)
        for tab_name, tab_content in self._table_tabs.items():
            return_value += formatter.format_tab_content(tab_name, tab_content)
        return_value += formatter.format_tabs_end()
        return return_value

    def _add_table_tab(self, tab_name: str, tab_content: str) -> None:
        self._table_tabs[tab_name] = tab_content

    def _stable_uuid(self, prefix: str | None = None) -> str:
        """Returns a stable identifier with optional prefix.  If not id
        provided one will be auto generated by pandas dataframe which will
        trigger git differences
        """
        hash_input = (prefix or "") + self.dataframe.to_csv(index=False)
        h = hashlib.sha256(hash_input.encode("utf-8")).hexdigest()[:16]
        if prefix:
            return f"{prefix}_{h}"
        else:
            return h

    def _highlight_values_in_list(self, items_to_highlight, rgba) -> None:
        format_value = "background-color:rgba(" + rgba + ");"
        default_value = "background-color:rgba(0,0,0,0);"
        self._styled_table.map(
            func=lambda x: format_value
            if x in items_to_highlight
            else default_value
        )


class FormulaTableSimple(_FormulaTable):
    """Simple formula table implementation of abstract class FormulaTableType"""

    def customise_properties(self):
        self.dataframe = self.dataframe[["Formula"]]
        self.has_hidden_column_headers = True
        self.has_hidden_row_headers = True
