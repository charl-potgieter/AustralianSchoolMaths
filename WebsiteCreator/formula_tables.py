import typing
from enum import Enum
from abc import ABC, abstractmethod
import hashlib
import pandas as pd
from pandas.io.formats.style import Styler
from site_content import Formulas
from page_structure import PageTabs


class FormulaTableType(ABC):
    """Implements an abstract base class for various types of Formula Tables
    https://python-course.eu/oop/the-abc-of-abstract-base-classes.php
    https://docs.python.org/3/library/abc.html
    """

    def __init__(self, formulas):
        self._formulas = formulas

    @property
    @abstractmethod
    def content_type(self) -> str:
        pass

    @property
    @abstractmethod
    def has_hidden_column_headers(self) -> bool:
        pass

    @property
    @abstractmethod
    def has_hidden_row_headers(self) -> bool:
        pass

    @property
    @abstractmethod
    def formula_menu_display_name(self) -> str:
        """This is the name as it appears on the formula secion of the site
        menu / navigator
        """

    @property
    @abstractmethod
    def topic_page_heading(self) -> str:
        """This is the heading that appears on topic pages above the formula
        table
        """

    @property
    @abstractmethod
    def formula_columns(self) -> list[str]:
        pass

    @abstractmethod
    def to_dataframe(self) -> pd.DataFrame:
        pass


class FormulaTableTypeSimple(FormulaTableType):
    """Simple formula table implementation of abstract class FormulaTableType"""

    @property
    def content_type(self) -> str:
        return ContentTypes.FORMULAS.value

    @property
    def has_hidden_column_headers(self) -> bool:
        return True

    @property
    def has_hidden_row_headers(self) -> bool:
        return True

    @property
    def formula_menu_display_name(self) -> str:
        return self._formulas.field_value("Category")

    @property
    def topic_page_heading(self) -> str:
        return "Formulas"

    @property
    def formula_columns(self) -> list[str]:
        """Returns the names of columns containing formulas as a list"""
        return ["Formula"]

    def to_dataframe(self) -> pd.DataFrame:
        """Returns the table as a dataframe"""
        return self._formulas.data[["Formula"]]


class FormulaTableTypeCalculus(FormulaTableType):
    """Table summary of derivatives and their equivalent integrals"""

    @property
    def content_type(self) -> str:
        return ContentTypes.FORMULA_SUMMARIES.value

    @property
    def has_hidden_column_headers(self) -> bool:
        return False

    @property
    def has_hidden_row_headers(self) -> bool:
        return True

    @property
    def formula_menu_display_name(self) -> str:
        return "Calculus"

    @property
    def topic_page_heading(self) -> str:
        return "Derivatives vs integrals "

    @property
    def formula_columns(self) -> list[str]:
        """Returns the names of columns containing formulas as a list"""
        return ["Derivative", "Equivalent integral"]

    def to_dataframe(self) -> pd.DataFrame:
        """Returns a summary table in dataframe format"""

        if not self._formulas_contain_grouped_derivatives_and_integrals():
            return pd.DataFrame()
        formulas_df = self._formulas.data
        calculus_df = formulas_df[
            formulas_df["Category"].isin(["Differentiation", "Integration"])
        ]
        calculus_df = calculus_df.dropna(subset=["Group"])
        calculus_df = calculus_df[["Category", "Group", "Formula", "Comment"]]
        calculus_df = calculus_df.pivot(
            columns="Category", index="Group"
        ).fillna("")

        # Flatten the multi-index headings after pivot
        calculus_df.columns = (
            calculus_df.columns.get_level_values(0)
            + " "
            + calculus_df.columns.get_level_values(1)
        )
        calculus_df = calculus_df.reset_index()

        calculus_df["Comment"] = calculus_df.apply(
            self._get_comment, axis="columns"
        )

        calculus_df = calculus_df.sort_values(by="Group")
        calculus_df = calculus_df.drop(
            labels=["Group", "Comment Differentiation", "Comment Integration"],
            axis="columns",
        )
        calculus_df = calculus_df.rename(
            columns={
                "Formula Differentiation": "Derivative",
                "Formula Integration": "Equivalent integral",
            }
        )

        # Reorder columns
        calculus_df = calculus_df[
            ["Derivative", "Equivalent integral", "Comment"]
        ]
        return calculus_df

    def _formulas_contain_grouped_derivatives_and_integrals(self) -> bool:
        grouped_formulas = self._formulas.data.dropna(subset=["Group"])
        return ("Differentiation" in grouped_formulas["Category"].values) and (
            "Integration" in grouped_formulas["Category"].values
        )

    def _get_comment(self, row) -> str:
        """Returns a comment for calculus formula summary based on
        combined derivative and integral comments
        """
        if row["Comment Differentiation"] == row["Comment Integration"]:
            return_value = row["Comment Differentiation"]
        elif row["Comment Differentiation"] == "":
            return_value = row["Comment Integration"]
        elif row["Comment Integration"] == "":
            return_value = row["Comment Differentiation"]
        else:
            return_value = (
                row["Comment Differentiation"]
                + "\n"
                + row["Comment Integration"]
            )
        return return_value


class FormulaTableTypeFinancial(FormulaTableType):
    @property
    def content_type(self) -> str:
        return ContentTypes.FORMULA_SUMMARIES.value

    @property
    def has_hidden_column_headers(self) -> bool:
        return False

    @property
    def has_hidden_row_headers(self) -> bool:
        return False

    @property
    def formula_menu_display_name(self) -> str:
        return "Financial mathematics"

    @property
    def topic_page_heading(self) -> str:
        return "Arithmetic vs geometric sequences"

    @property
    def formula_columns(self) -> list[str]:
        """Returns the names of columns containing formulas as a list"""
        return ["Arithmetic sequence", "Geometric sequence"]

    def to_dataframe(self) -> pd.DataFrame:
        financial_df = self._formulas.data
        financial_df = financial_df[
            (financial_df["Category"] == "Financial mathematics")
            & (
                (financial_df["Subcategory_1"] == "Arithmetic sequence")
                | (financial_df["Subcategory_1"] == "Geometric sequence")
            )
        ]
        if len(financial_df.index) == 0:
            return pd.DataFrame()

        financial_df = financial_df[
            ["Subcategory_1", "Subcategory_2", "Formula"]
        ]
        financial_df = pd.pivot_table(
            data=financial_df,
            values="Formula",
            columns="Subcategory_1",
            index="Subcategory_2",
            aggfunc=lambda x: x,
        )
        financial_df.index.name = None
        financial_df.columns.name = None

        # Convert index to categorical data to enable custom sort order
        financial_df.index = pd.CategoricalIndex(
            financial_df.index,
            [
                "Recursive definition",
                "n-th term",
                "Sum of first n terms",
                "Limiting sum",
            ],
        )
        financial_df = financial_df.sort_index()
        return financial_df


class FormulaTable:
    """Summary table of formulas"""

    def __init__(self, formulas: Formulas, table_type: type[FormulaTableType]):
        self._formulas = formulas
        self._state = formulas.field_value("State")
        self._subject = formulas.field_value("Subject")
        self._table_type = table_type(formulas)

    @property
    def state(self) -> str:
        return typing.cast(str, self._state)

    @property
    def subject(self) -> str:
        return typing.cast(str, self._subject)

    @property
    def table_type(self) -> FormulaTableType:
        return self._table_type

    def _to_dataframe(self) -> pd.DataFrame:
        return self._table_type.to_dataframe()

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
        return return_table.to_html()

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
        return return_table.to_html()

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
        return return_table.to_html()

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
            '###  <span style="color:RGB(139,69,19)"> '
            + self.table_type.topic_page_heading
            + " </span>"
            + "\n<br>\n"
            + self.to_markdown()
        )


class ContentTypes(Enum):
    """Implements enumeration containing website content types"""

    TOPICS = "Topics"
    FORMULAS = "Formulas"
    FORMULA_SUMMARIES = "Formula summaries"


class _StyledTable:
    """Implements a dataframe styler customised for maths formula display"""

    def __init__(self, input_df: pd.DataFrame):
        self._df = input_df.fillna("")
        self._table = self._create_styler()
        # Calculate and assign unique table hash to prevent pandas from auto
        # generating different values each time which are identified as changes
        # by git
        self._table_hash = self._compute_table_hash()
        self._table.set_uuid(self._table_hash)

    def _create_styler(self):
        styler = self._df.style
        styler = styler.set_table_styles(
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
        return styler

    def _compute_table_hash(self):
        """Compute a stable hash of the DataFrame content."""
        df_bytes = self._df.to_csv(index=False).encode("utf-8")
        return hashlib.md5(df_bytes).hexdigest()[:8]

    def _raw(self) -> Styler:
        return self._table

    def to_html(self) -> str:
        return self._table.to_html()

    def hide_column_headers(self) -> None:
        self._table = self._table.hide(axis="columns")

    def hide_row_headers(self) -> None:
        self._table = self._table.hide(axis="index")

    def highlight_values_in_list(
        self, value_list, columns_to_highlight=None, rgba="255,194,10, 0.2"
    ) -> None:
        format_value = "background-color:rgba(" + rgba + ");"
        default_value = "background-color:rgba(0,0,0,0);"
        self._table = self._table.map(
            func=lambda x: format_value if x in value_list else default_value,
            subset=columns_to_highlight,
        )


formula_table_types = (
    FormulaTableTypeSimple,
    FormulaTableTypeFinancial,
    FormulaTableTypeCalculus,
)
