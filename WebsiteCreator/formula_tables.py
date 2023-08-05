""" This module contains formula table related classes"""

from enum import Enum
from abc import ABC, abstractmethod
import pandas as pd


class FormulaTable():
    """Summary table of formulas"""

    def __init__(self, formulas):
        """Initiates the class

        Args:
            formulas (Formulas object): the input data
        """
        self._formulas = formulas
        self._state = formulas.field_value('State')
        self._subject = formulas.field_value('Subject')
        self._table_type = None

    @property
    def state(self):
        """Returns the state of formulas included in the table"""
        return self._state

    @property
    def subject(self):
        """Returns the subject of formulas included in the table"""
        return self._subject

    @property
    def type(self):
        """Returns the table type"""
        return self._table_type

    @type.setter
    def type(self, table_type):
        """Sets table type"""
        self._table_type = table_type(self._formulas)

    def _to_dataframe(self):
        """Returns FormulaTable as pandas dataframe"""
        return self._table_type.to_dataframe()

    @property
    def has_tabs(self):
        """Returns true if table has / requires tabs"""
        return (
            self.contains_formula_sheet_items or
            self.contains_proof_required_items
        )

    @property
    def contains_formula_sheet_items(self):
        """Returns True if the table contains formulas that appear on the
        formula sheet"""
        formula_columns = self.type.formula_columns
        formulas_in_table = (
            self.type.to_dataframe()[formula_columns].stack())
        formula_sheet_items = self._formulas.formula_sheet_items
        return (len(
            set(formulas_in_table).intersection(set(formula_sheet_items))
        ) > 0)

    @property
    def contains_proof_required_items(self):
        """Returns True if the table contains formulas that require proofs"""
        formula_columns = self.type.formula_columns
        formulas_in_table = (
            self.type.to_dataframe()[formula_columns].stack())
        proof_required_items = self._formulas.proofs_required_items
        return (len(
            set(formulas_in_table).intersection(set(proof_required_items))
        ) > 0)

    def _table_no_higlights(self):
        """Returns table with no highlights"""
        return_table = _StyledTable(self._to_dataframe())
        return_table.hide_column_headers()
        return_table.hide_row_headers()
        return return_table.to_html()

    def _table_formula_sheet_higlights(self):
        """Returns table with formulas on formula sheet higlighted"""
        return_table = _StyledTable(self._to_dataframe())
        return_table.hide_column_headers()
        return_table.hide_row_headers()
        return_table.highlight_values_in_list(
            self._formulas.formula_sheet_items,
            columns_to_highlight=self._table_type.formula_columns)
        return return_table.to_html()

    def _table_proofs_required_higlights(self):
        """Returns table with formulas where proofs are required higlighted"""
        return_table = _StyledTable(self._to_dataframe())
        return_table.hide_column_headers()
        return_table.hide_row_headers()
        return_table.highlight_values_in_list(
            self._formulas.proofs_required_items,
            columns_to_highlight=self._table_type.formula_columns,
            rgba='0,150,200, 0.2')
        return return_table.to_html()

    @property
    def contains_content(self):
        """Returns true if the Formula table contains content"""
        if self._table_type is None:
            return False
        if self._table_type.to_dataframe() is None:
            return False
        return len(self._table_type.to_dataframe()) > 0

    def to_markdown(self):
        """Returns formula table in markdown format"""
        if not self.has_tabs:
            return_value = self._table_no_higlights()
        else:
            tabs = PageTabs()
            tabs.add_tab('Standard view', self._table_no_higlights())
            if self.contains_formula_sheet_items:
                tabs.add_tab(
                    'Formula sheet',
                    'Items on formula sheet are highlighted \n<br>\n'
                    + self._table_formula_sheet_higlights())
            if self.contains_proof_required_items:
                tabs.add_tab(
                    'Poofs required',
                    'Items where proofs required are highlighted \n<br>\n'
                    + self._table_proofs_required_higlights())
            return_value = tabs.to_markdown()
        return return_value


class ContentTypes(Enum):
    """Implements enumeration containing website content types"""
    TOPICS = 'Topics'
    FORMULAS = 'Formulas'
    FORMULA_SUMMARIES = 'Formula summaries'


class FormulaTableType(ABC):
    """Implements an abstract base class for various types of Formula Tables
    https://python-course.eu/oop/the-abc-of-abstract-base-classes.php
    https://docs.python.org/3/library/abc.html
    """

    def __init__(self, formulas):
        self._formulas = formulas

    @property
    @abstractmethod
    def content_type(self):
        """Abstract method for returning a ContentTypes enum class """

    @property
    @abstractmethod
    def display_name(self):
        """Abstract method for returning display name"""

    @property
    @abstractmethod
    def formula_columns(self):
        """Abstract method for returning formulas containing columns"""

    @abstractmethod
    def to_dataframe(self):
        """Abstract method for returning table as a dataframe"""


class FormulaTableTypeSimple(FormulaTableType):
    """Simple formula table implementatio of abstract class FormulaTableType
    """

    content_type = ContentTypes.FORMULAS.value

    @property
    def display_name(self):
        return self._formulas.field_value('Category')

    @property
    def formula_columns(self):
        """Returns the names of columns containing formulas as a list"""
        return ['Formula']

    def to_dataframe(self):
        """Returns the table as a dataframe"""
        return self._formulas.to_dataframe()[['Formula']]


class FormulaTableTypeCalculus(FormulaTableType):
    """Table summary of derivatives and their equivalent integrals
    """

    content_type = ContentTypes.FORMULA_SUMMARIES.value

    @property
    def display_name(self):
        """Returns the table's display name"""
        return 'Calculus'

    @property
    def formula_columns(self):
        """Returns the names of columns containing formulas as a list"""
        return ['Derivative', 'Equivalent integral']

    def to_dataframe(self):
        """Returns a summary table in dataframe format"""

        if not self._formulas_contain_both_derivatives_and_integrals():
            return None
        formulas_df = self._formulas.to_dataframe()
        calculus_df = (formulas_df[formulas_df["Category"].isin(
            ["Differentiation", "Integration"])])
        calculus_df = calculus_df[['Category', 'Group', 'Formula', 'Comment']]
        calculus_df = calculus_df.pivot(
            columns='Category', index='Group').fillna('')

        # Flatten the multi-index headings after pivot
        calculus_df.columns = (
            calculus_df.columns.get_level_values(0) + ' ' +
            calculus_df.columns.get_level_values(1))
        calculus_df = calculus_df.reset_index()

        calculus_df['Comment'] = (
            calculus_df.apply(self._get_comment, axis='columns'))

        calculus_df = calculus_df.sort_values(by='Group')
        calculus_df = calculus_df.drop(
            labels=['Group', 'Comment Differentiation', 'Comment Integration'],
            axis='columns')
        calculus_df = calculus_df.rename(columns={
            "Formula Differentiation": "Derivative",
            "Formula Integration": "Equivalent integral"})

        # Reorder columns
        calculus_df = calculus_df[['Derivative', 'Equivalent integral',
                                   'Comment']]
        return calculus_df

    def _formulas_contain_both_derivatives_and_integrals(self):
        """Returns true if formulas contain both derivatives and integrals"""
        formula_data = self._formulas.to_dataframe()
        return (
            ("Differentiation" in formula_data['Category'].values) and
            ("Integration" in formula_data['Category'].values))

    def _get_comment(self, row):
        """Returns a comment for calculus formula summary based on
        combined derivative and integral comments
        """
        if row['Comment Differentiation'] == row['Comment Integration']:
            return_value = row['Comment Differentiation']
        elif row['Comment Differentiation'] == '':
            return_value = row['Comment Integration']
        elif row['Comment Integration'] == '':
            return_value = row['Comment Differentiation']
        else:
            return_value = (row['Comment Differentiation'] + '\n' +
                            row['Comment Integration'])
        return return_value


class FormulaTableTypeFinancial(FormulaTableType):
    """Table summary of financial maths formulas"""

    content_type = ContentTypes.FORMULA_SUMMARIES.value

    @property
    def display_name(self):
        """Returns the table's display name"""
        return 'Financial mathematics'

    @property
    def formula_columns(self):
        """Returns the names of columns containing formulas as a list"""
        return ['Arithmetic sequence', 'Geometric sequence']

    def to_dataframe(self):
        """Returns a summary table in dataframe format"""
        financial_df = self._formulas.to_dataframe()
        financial_df = (financial_df[
            (financial_df['Category'] == 'Financial mathematics') &
            (
                (financial_df['Subcategory_1'] == 'Arithmetic sequence') |
                (financial_df['Subcategory_1'] == 'Geometric sequence')
            )
        ])
        if len(financial_df.index) == 0:
            return None

        financial_df = financial_df[['Subcategory_1', 'Subcategory_2',
                                     'Formula']]
        financial_df = pd.pivot_table(data=financial_df, values='Formula',
                                      columns='Subcategory_1',
                                      index='Subcategory_2',
                                      aggfunc=lambda x: x)
        financial_df.index.name = None
        financial_df.columns.name = None

        # Convert index to categorical data to enable custom sort order
        financial_df.index = pd.Categorical(
            financial_df.index,
            ['Recursive definition', 'n-th term', 'Sum of first n terms',
             'Limiting sum'])
        financial_df = financial_df.sort_index()
        return financial_df


class _StyledTable():
    """Implements a dataframe styler customised for maths formula display"""

    def __init__(self, input_df):
        """Initialises the class with pandas input dataframe with
        default table formatting"""
        self._table = input_df.fillna('').style
        self._table = self._table.set_table_styles([
            {'selector': 'th.col_heading',
             'props': 'text-align: left; font-size:1em;'},
            {'selector': 'td', 'props':
             'text-align: left; font-size:1em;padding: 1.5em;'}])

    def _raw(self):
        """Returns the pandas styler"""
        return self._table

    def to_html(self):
        """Returns the styled table object in html format"""
        return self._table.to_html()

    def hide_column_headers(self):
        """Hides headers"""
        self._table = self._table.hide(axis='columns')

    def hide_row_headers(self):
        """Hides headers"""
        self._table = self._table.hide(axis='index')

    def highlight_values_in_list(self, value_list,
                                 columns_to_highlight=None,
                                 rgba='255,194,10, 0.2'):
        """Highlights values in columns_to_highlight if they appear in
        value_list.  Values in all columns are highlighted if
        colums_to_higlight is None
        """
        format_value = 'background-color:rgba(' + rgba + ');'
        self._table = self._table.applymap(
            func=lambda x: format_value if x in value_list else None,
            subset=columns_to_highlight, )


class PageTabs():
    """Manages page tabs for Hugo wesite creation"""

    def __init__(self):
        self._tabs = None

    def add_tab(self, tab_name, tab_content):
        """Adds tab with name and content"""
        if not self._tabs:
            self._tabs = {}
        self._tabs[tab_name] = tab_content

    def to_markdown(self):
        """Returns the tabs as markdown string"""
        return_value = '{{< tabs "uniqueid" >}}'
        for tab_name, tab_content in self._tabs.items():
            return_value += '\n\n{{< tab "' + tab_name + '" >}}\n\n'
            return_value += tab_content
            return_value += '{{< /tab >}}'
        return_value += '\n{{< /tabs >}}'
        return return_value
