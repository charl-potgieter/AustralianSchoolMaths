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
    def states(self) -> list[str]:
        return_value = self.data["State"]
        return_value = return_value.unique().tolist()
        return return_value

    @property
    def topic_codes(self) -> list[str]:
        return_value = self.data["Syllabus_subtopic_code"]
        return_value = return_value.unique().tolist()
        return return_value

    @property
    def state_and_topic_codes(self) -> list[tuple[str, str]]:
        return_value = (
            self.data[["State", "Syllabus_subtopic_code"]]
            .drop_duplicates()
            .values
        )
        return_value = return_value.tolist()
        return return_value

    def per_state_and_topic_code(self, state: str, topic: str) -> Formulas:
        new_data = pd.DataFrame(
            self.data[
                (self.data["State"] == state)
                & (self.data["Syllabus_subtopic_code"] == topic)
            ].copy()
        )
        new_formulas = Formulas(new_data)
        return new_formulas

    @property
    def simple_table(self):
        # TODO: return styled pandas table
        return "TBA"


class FormulaTable:
    """Summary table of formulas"""

    def __init__(self, formulas: Formulas):
        self._formulas = formulas

    @property
    def has_tabs(self) -> bool:
        """Returns true if table has / requires tabs"""
        return (
            self.contains_formula_sheet_items
            or self.contains_proof_required_items
        )

    @property
    def contains_formula_sheet_items(self) -> bool:
        """Returns True if the table contains formulas that appear on the
        formula sheet"""
        formula_columns = self.table_type.formula_columns
        formulas_in_table = self.table_type.to_dataframe()[
            formula_columns
        ].stack()
        formula_sheet_items = self._formulas.formula_sheet_items
        return (
            len(set(formulas_in_table).intersection(set(formula_sheet_items)))
            > 0
        )

    @property
    def contains_proof_required_items(self) -> bool:
        """Returns True if the table contains formulas that require proofs"""
        formula_columns = self.table_type.formula_columns
        formulas_in_table = self.table_type.to_dataframe()[
            formula_columns
        ].stack()
        proof_required_items = self._formulas.proofs_required_items
        return (
            len(set(formulas_in_table).intersection(set(proof_required_items)))
            > 0
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

    @property
    def contains_content(self) -> bool:
        """Returns true if the Formula table contains content"""
        if self._table_type is None:
            return False
        if self._table_type.to_dataframe() is None:
            return False
        return len(self._table_type.to_dataframe()) > 0

    def to_markdown(self) -> str:
        """Returns formula table in markdown format"""
        if not self.contains_content:
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

    def to_markdown_with_heading(self) -> str:
        return (
            self.table_type.topic_page_heading
            + "\n<br>\n"
            + self.to_markdown()
        )
