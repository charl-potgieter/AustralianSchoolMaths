# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import copy
from typing import Callable, Self, Dict
from collections.abc import Generator
import pandas as pd
from data_validator import DataColumnValidator


class _SiteContent():
    """Defines a base class for site content used to derive other classes
    such as formulas, definitions etc"""

    # Enforces structure of csv when loaded
    _data_structure = {}

    def __init__(self, input_data: pd.DataFrame):
        column_validator = DataColumnValidator(
            list(input_data.columns), list(self._data_structure.keys()))
        column_validator.validate_column_names()
        self._data = input_data.astype(self._data_structure)
        self._is_cumulative = False

    @property
    def is_cumulative(self) -> bool:
        """Returns whether this obeject is cumulative across
        subjects / years"""
        return self._is_cumulative

    @is_cumulative.setter
    def is_cumulative(self, value: bool):
        """Sets this objects is cumulative status representing whether
        it contains items that are cumulative across subjects / years"""
        self._is_cumulative = value

    @property
    def data(self) -> pd.DataFrame:
        return self._data.copy()

    @data.setter
    def data(self, values: pd.DataFrame):
        self._data = values

    def field_value(self, field_name: str) -> str | float:
        """Returns the value in field_name.  If multiple non-unique values
          exist return 'Multiple Values'
          """
        unique_values_in_field = (
            self._data[field_name].drop_duplicates())
        if len(unique_values_in_field) == 1:
            return list(unique_values_in_field)[0]
        return 'Multiple values'

    def copy(self) -> Self:
        return copy.deepcopy(self)

    def filter_by_function(self, filter_function: Callable) -> Self:
        """Returns a new filtered object where
        filter_function returns True when passed each data item in the
        object as a pandas series.
        """
        new_object = self.copy()
        return_mask = new_object.data.apply(filter_function, axis=1)
        new_object.data = pd.DataFrame(new_object.data[return_mask])
        return new_object

    def filter_by_dict(self, filter_dict: Dict[str, str]) -> Self:
        """Returns a new filtered object filtered by field per dictionary
        key equal to dictionary value"""
        new_object = self.copy()
        for key, value in filter_dict.items():
            new_object.data = new_object.data[new_object.data[key] == value]
        return new_object

    def group_by_columns(self, columns: list[str]) -> Generator[Self,
                                                                None, None]:
        """Returns a generator of this object grouped by columns (iterable)
        """
        grouper = self._data.groupby(columns)
        for _, data in grouper:
            yield Formulas(data)


class Syllabus(_SiteContent):

    _data_structure = {'State': 'object',
                       'Subject': 'object',
                       'Syllabus_topic': 'object',
                       'Syllabus_subtopic_code': 'object',
                       'Syllabus_subtopic': 'object'}

    @property
    def unique_subtopics(self) -> list[str]:
        return list(set(self._data['Syllabus_subtopic']))

    def topics(self):
        """generator of topics in syllabus (excludes subtopic levels)"""
        working_data = self.data[['State', 'Subject', 'Syllabus_topic']
                                 ].drop_duplicates()
        for item in working_data.itertuples():
            item = SyllabusTopic(item.State,
                                 item.Subject,
                                 item.Syllabus_topic,
                                 )
            yield item


class SyllabusTopic():
    """Single syllabus topic item of Syllabus class excluding subtopic level
    details
    """

    def __init__(self, state: str, subject: str, syllabus_topic: str):
        self._state = state
        self._subject = subject
        self._syllabus_topic = syllabus_topic

    @property
    def state(self) -> str:
        return self._state

    @property
    def subject(self) -> str:
        return self._subject

    @property
    def syllabus_topic(self) -> str:
        return self._syllabus_topic


class Formulas(_SiteContent):

    _data_structure = {'State': 'object',
                       'Subject': 'object',
                       'Syllabus_topic': 'object',
                       'Syllabus_subtopic_code': 'object',
                       'Syllabus_subtopic': 'object',
                       'Category': 'object',
                       'Subcategory_1': 'object',
                       'Subcategory_2': 'object',
                       'Description': 'object',
                       'Group': 'object',
                       'Formula': 'object',
                       'On_formula_sheet': 'bool',
                       'Proof_required': 'bool',
                       'Comment': 'object'}

    @property
    def formula_sheet_items(self) -> list[str]:
        """Returns a list of formulas where field 'On_formula_sheet'
        is True
        """
        formulas_on_sheet = list(self._data[
            (self._data['On_formula_sheet']) &
            (self._data['Formula'].notnull())
        ]['Formula'].drop_duplicates())
        return formulas_on_sheet

    @property
    def proofs_required_items(self) -> list[str]:
        """Returns a list of formulas where field 'Proof_required'
         is True
        """
        proofs_required = list(self._data[
            (self._data['Proof_required']) &
            (self._data['Formula'].notnull())
        ]['Formula'].drop_duplicates())
        return proofs_required


class Definitions(_SiteContent):

    _data_structure = {'State': 'object',
                       'Subject': 'object',
                       'Syllabus_topic': 'object',
                       'Syllabus_subtopic_code': 'object',
                       'Syllabus_subtopic': 'object',
                       'Definition': 'object'}
