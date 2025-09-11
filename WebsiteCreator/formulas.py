# prevents raising an rror of a return value of type class before completing
# the class definition, for example per_topic_code returns type Formuals
# before the definition for Formulas is conmpelte
from __future__ import annotations
import pandas as pd
import hashlib


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
        self._apply_table_properties()

    def _set_table_properties(self, formulas: Formulas):
        self._formulas = formulas
        self._dataframe = formulas.data
        self._has_hidden_column_headers = False
        self._has_hidden_row_headers = False
        self._table_tabs = {}

    def _apply_table_properties(self):
        self._styled_table = self._create_styled_table()
        self._set_table_header_visibility()

    def _create_styled_table(self) -> pd.io.formats.style.Styler:
        return_value = self._dataframe.style.set_table_styles(
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

    def to_string(self) -> str:
        """Returns string format for inclusion in hugo markdown files"""
        if not self._formulas.contains_data:
            return self._empty_table_string()
        elif not self.requires_tabs:
            return self._single_table_string()
        else:
            self._create_table_tabs()
            return self._multi_tab_string()

    def _empty_table_string(self) -> str:
        return ""

    @property
    def requires_tabs(self) -> bool:
        """Returns true if table has / requires tabs"""
        return (
            self._formulas.contains_formula_sheet_items
            or self._formulas.contains_proof_required_items
        )

    def _single_table_string(self, prefix: str | None = None) -> str:
        self._set_table_header_visibility()
        table_id = self._stable_uuid(prefix)
        return self._styled_table.to_html(table_uuid=table_id)

    def _create_table_tabs(self) -> None:
        self._add_table_tab(
            "Standard view", self._single_table_string("standard")
        )
        if self._formulas.contains_formula_sheet_items:
            self._highlight_values_in_list(
                items_to_highlight=self._formulas.formula_sheet_items,
                rgba="255,194,10, 0.2",
            )
            self._add_table_tab(
                "Formulas sheet", self._single_table_string("formula_sheet")
            )
        if self._formulas.contains_proof_required_items:
            self._highlight_values_in_list(
                items_to_highlight=self._formulas.proof_required_items,
                rgba="0,150,200, 0.2",
            )
            self._add_table_tab(
                "Proof required", self._single_table_string("proof")
            )

    def _multi_tab_string(self) -> str:
        return_value = '{{< tabs "' + self._stable_uuid("tab") + '" >}}'
        for tab_name, tab_content in self._table_tabs.items():
            return_value += '\n\n{{< tab "' + tab_name + '" >}}\n\n'
            return_value += tab_content
            return_value += "{{< /tab >}}"
        return_value += "\n{{< /tabs >}}"
        return return_value

    def _add_table_tab(self, tab_name: str, tab_content: str) -> None:
        self._table_tabs[tab_name] = tab_content

    def _stable_uuid(self, prefix: str | None = None) -> str:
        """Returns a stable identifier with optional prefix.  If not id
        provided one will be auto generated by pandas dataframe which will
        trigger git differences
        """
        hash_input = (prefix or "") + self._dataframe.to_csv(index=False)
        h = hashlib.sha256(hash_input.encode("utf-8")).hexdigest()[:16]
        if prefix:
            return f"{prefix}_{h}"
        else:
            return h

    def _highlight_values_in_list(self, items_to_highlight, rgba) -> None:
        format_value = "background-color:rgba(" + rgba + ");"
        default_value = "background-color:rgba(0,0,0,0);"
        self._table = self._styled_table.map(
            func=lambda x: format_value
            if x in items_to_highlight
            else default_value
        )

    # def _table_no_higlights(self) -> str:
    #     """Returns table with no highlights"""
    #     return_table = _StyledTable(self._to_dataframe())
    #     if self._table_type.has_hidden_column_headers:
    #         return_table.hide_column_headers()
    #     if self._table_type.has_hidden_row_headers:
    #         return_table.hide_row_headers()
    #     return return_table.to_html(prefix="standard")
    #
    # def _table_formula_sheet_higlights(self) -> str:
    #     """Returns table with formulas on formula sheet higlighted"""
    #     return_table = _StyledTable(self._to_dataframe())
    #     if self._table_type.has_hidden_column_headers:
    #         return_table.hide_column_headers()
    #     if self._table_type.has_hidden_row_headers:
    #         return_table.hide_row_headers()
    #     return_table.highlight_values_in_list(
    #         self._formulas.formula_sheet_items,
    #         columns_to_highlight=self._table_type.formula_columns,
    #     )
    #     return return_table.to_html(prefix="formula_sheet")
    #
    # def _table_proofs_required_higlights(self) -> str:
    #     """Returns table with formulas where proofs are required higlighted"""
    #     return_table = _StyledTable(self._to_dataframe())
    #     if self._table_type.has_hidden_column_headers:
    #         return_table.hide_column_headers()
    #     if self._table_type.has_hidden_row_headers:
    #         return_table.hide_row_headers()
    #     return_table.highlight_values_in_list(
    #         self._formulas.proofs_required_items,
    #         columns_to_highlight=self._table_type.formula_columns,
    #         rgba="0,150,200, 0.2",
    #     )
    #     return return_table.to_html(prefix="proof_required")
    #
    # def to_markdown(self) -> str:
    #     if not self._formulas.contains_data:
    #         return ""
    #     if not self.has_tabs:
    #         return_value = self._table_no_higlights()
    #     else:
    #         tabs = TableTabs()
    #         tabs.add_tab("Standard view", self._table_no_higlights())
    #         if self.contains_formula_sheet_items:
    #             tabs.add_tab(
    #                 "Formula sheet",
    #                 "Items on formula sheet are highlighted \n<br>\n"
    #                 + self._table_formula_sheet_higlights(),
    #             )
    #         if self.contains_proof_required_items:
    #             tabs.add_tab(
    #                 "Proofs required",
    #                 "Items where proofs required are highlighted \n<br>\n"
    #                 + self._table_proofs_required_higlights(),
    #             )
    #         return_value = tabs.to_markdown()
    #     return return_value


class FormulaTableSimple(_FormulaTable):
    """Simple formula table implementation of abstract class FormulaTableType"""

    def __init__(self, formulas: Formulas):
        self._set_properties_per_parent__table_class(formulas)
        self._override_parent_table_class_properties(formulas)
        self._apply_table_properties()

    def _set_properties_per_parent__table_class(self, formulas: Formulas):
        self._set_table_properties(formulas)

    def _override_parent_table_class_properties(self, formulas: Formulas):
        self._dataframe = formulas.data[["Formula"]]
        self._has_hidden_column_headers = True
        self._has_hidden_row_headers = True
