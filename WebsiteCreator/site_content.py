# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from typing import Callable, Self
from collections.abc import Generator
import numpy as np
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

    def group_by_columns(self, columns: list[str]) -> Generator[Self,
                                                                None, None]:
        """Returns a generator of this object grouped by columns (iterable)
        """
        grouper = self._data.groupby(columns)
        for _, data in grouper:
            yield _SiteContent(data)


class Syllabus(_SiteContent):

    _data_structure = {'State': 'object',
                       'Subject': 'object',
                       'Syllabus_topic': 'object',
                       'Syllabus_subtopic_code': 'object',
                       'Syllabus_subtopic': 'object'}

    def copy(self) -> Self:
        # Needs to reside here rather than _SiteContent parent class
        # as needs to copy all this classes attributes and be of this classes
        # type
        new_object = Syllabus(self.data)
        new_object.is_cumulative = self.is_cumulative
        return new_object

    def filter_by_function(self, filter_function: Callable) -> Self:
        """Returns a new filtered object where
        filter_function returns True when passed each item in
        Formulas as a pandas series.  Needs to reside in child class rather
        than _SiteContent parent class as needs to access this classes copy
        method
        """
        new_object = self.copy()
        return_mask = new_object.data.apply(filter_function, axis=1)
        new_object.data = pd.DataFrame(new_object.data[return_mask])
        return new_object

    @property
    def topic_summary_level(self) -> Self:
        """Returns syllabus at a unique state, subject topic level with
        subtopic related fiels as Nan
        """
        new_syllabus = self.copy()
        new_syllabus.data = new_syllabus.data[
            ['State', 'Subject', 'Syllabus_topic']].drop_duplicates()
        new_syllabus.data['Syllabus_subtopic_code'] = np.NAN
        new_syllabus.data['Syllabus_subtopic'] = np.NAN
        return new_syllabus

    @property
    def unique_subtopics(self) -> list[str]:
        return list(set(self._data['Syllabus_subtopic']))


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

    def copy(self) -> Self:
        new_object = Formulas(self.data)
        new_object.is_cumulative = self.is_cumulative
        return new_object

    def filter_by_function(self, filter_function: Callable) -> Self:
        """Returns a new filtered object where
        filter_function returns True when passed each item in
        Formulas as a pandas series.  Needs to reside in child class rather
        than _SiteContent parent class as needs to access this classes copy
        method
        """
        new_object = self.copy()
        return_mask = new_object.data.apply(filter_function, axis=1)
        new_object.data = pd.DataFrame(new_object.data[return_mask])
        return new_object

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

    def copy(self) -> Self:
        new_object = Definitions(self.data)
        new_object.is_cumulative = self.is_cumulative
        return new_object

    def filter_by_function(self, filter_function: Callable) -> Self:
        """Returns a new filtered object where
        filter_function returns True when passed each item in
        Formulas as a pandas series.  Needs to reside in child class rather
        than _SiteContent parent class as needs to access this classes copy
        method
        """
        new_object = self.copy()
        return_mask = new_object.data.apply(filter_function, axis=1)
        new_object.data = pd.DataFrame(new_object.data[return_mask])
        return new_object
