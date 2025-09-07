# prevents raising an error of a return value of type class before completing
# the class definition, for example per_topic_code returns type Formuals
# before the definition for Formulas is conmpelte
from __future__ import annotations
import pandas as pd


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
        return_value = bool(self.data["On_formula_sheet"].astype(bool).any())
        return return_value

    @property
    def contains_proof_required_items(self) -> bool:
        return_value = bool(self.data["Proof_required"].astype(bool).any())
        return return_value

    @property
    def to_simple_table_html(self):
        # TODO: return styled pandas table in html
        simple_table = FormulaTableSimple(self)
        return simple_table.to_markdown()


class _FormulaTable:
    def __init__(self, formulas: Formulas):
        self._formulas = formulas

    @property
    def has_hidden_column_headers(self) -> bool:
        return False

    @property
    def has_hidden_row_headers(self) -> bool:
        return False

    @property
    def has_tabs(self) -> bool:
        """Returns true if table has / requires tabs"""
        return (
            self._formulas.contains_formula_sheet_items
            or self._formulas.contains_proof_required_items
        )

    def _table_no_higlights(self) -> str:
        """Returns table with no highlights"""
        return_table = _StyledTable(self._to_dataframe())
        if self._table_type.has_hidden_column_headers:
            return_table.hide_column_headers()
        if self._table_type.has_hidden_row_headers:
            return_table.hide_row_headers()
        return return_table.to_html(prefix="standard")

    def _table_formula_sheet_higlights(self) -> str:
        """Returns table with formulas on formula sheet higlighted"""
        return_table = _StyledTable(self._to_dataframe())
        if self._table_type.has_hidden_column_headers:
            return_table.hide_column_headers()
        if self._table_type.has_hidden_row_headers:
            return_table.hide_row_headers()
        return_table.highlight_values_in_list(
            self._formulas.formula_sheet_items,
            columns_to_highlight=self._table_type.formula_columns,
        )
        return return_table.to_html(prefix="formula_sheet")

    def _table_proofs_required_higlights(self) -> str:
        """Returns table with formulas where proofs are required higlighted"""
        return_table = _StyledTable(self._to_dataframe())
        if self._table_type.has_hidden_column_headers:
            return_table.hide_column_headers()
        if self._table_type.has_hidden_row_headers:
            return_table.hide_row_headers()
        return_table.highlight_values_in_list(
            self._formulas.proofs_required_items,
            columns_to_highlight=self._table_type.formula_columns,
            rgba="0,150,200, 0.2",
        )
        return return_table.to_html(prefix="proof_required")

    def to_markdown(self) -> str:
        if not self._formulas.contains_data:
            return ""
        if not self.has_tabs:
            return_value = self._table_no_higlights()
        else:
            tabs = PageTabs()
            tabs.add_tab("Standard view", self._table_no_higlights())
            if self.contains_formula_sheet_items:
                tabs.add_tab(
                    "Formula sheet",
                    "Items on formula sheet are highlighted \n<br>\n"
                    + self._table_formula_sheet_higlights(),
                )
            if self.contains_proof_required_items:
                tabs.add_tab(
                    "Proofs required",
                    "Items where proofs required are highlighted \n<br>\n"
                    + self._table_proofs_required_higlights(),
                )
            return_value = tabs.to_markdown()
        return return_value


class FormulaTableSimple(_FormulaTable):
    """Simple formula table implementation of abstract class FormulaTableType"""

    def to_dataframe(self) -> pd.DataFrame:
        """Returns the table as a dataframe"""
        return pd.DataFrame(self._formulas.data[["Formula"]])
