# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


# https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class/70932112#70932112  # pylint: disable=line-too-long
from typing import Callable, Self
from collections.abc import Generator
from data_validator import DataColumnValidator
import pandas as pd


class Formulas():

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

    def __init__(self, input_data: pd.DataFrame):
        column_validator = DataColumnValidator(
            list(input_data.columns), list(self._data_structure.keys()))
        column_validator.validate_column_names()
        self._formula_data = input_data.astype(self._data_structure)
        self._is_cumulative = False

    @property
    def is_cumulative(self) -> bool:
        """Returns whether this Formulas obeject is cumulative across
        subjects (years)"""
        return self._is_cumulative

    @is_cumulative.setter
    def is_cumulative(self, value: bool):
        """Sets this objects is cumulative status representing whether
        it contains formulas that are cumulative across subjects / years"""
        self._is_cumulative = value

    @property
    def data(self) -> pd.DataFrame:
        return self._formula_data

    @data.setter
    def data(self, values: pd.DataFrame):
        self._formula_data = values

    @property
    def formula_sheet_items(self) -> list[str]:
        """Returns a list of formulas where field 'On_formula_sheet'
        is True
        """
        formulas_on_sheet = list(self._formula_data[
            (self._formula_data['On_formula_sheet']) &
            (self._formula_data['Formula'].notnull())
        ]['Formula'].drop_duplicates())
        return formulas_on_sheet

    @property
    def proofs_required_items(self) -> list[str]:
        """Returns a list of formulas where field 'Proof_required'
         is True
        """
        proofs_required = list(self._formula_data[
            (self._formula_data['Proof_required']) &
            (self._formula_data['Formula'].notnull())
        ]['Formula'].drop_duplicates())
        return proofs_required

    def copy(self) -> Self:
        new_formulas = Formulas(self.data.copy())
        new_formulas.is_cumulative = self.is_cumulative
        return new_formulas

    def filter_by_function(self, filter_function: Callable) -> Self:
        """Returns a new filtered Formulas object where
        filter_function returns True when passed each item in
        Formulas as a pandas series.
        """
        new_formulas = self.copy()
        return_mask = new_formulas.data.apply(filter_function, axis=1)
        new_formulas.data = pd.DataFrame(new_formulas.data[return_mask])
        return new_formulas

    def field_value(self, field_name: str) -> str | float:
        """Returns the value in field_name.  If multiple non-unique values
          exist return 'Multiple Values'
          """
        unique_values_in_field = (
            self._formula_data[field_name].drop_duplicates())
        if len(unique_values_in_field) == 1:
            return list(unique_values_in_field)[0]
        return 'Multiple values'

    def group_by_columns(self, columns: list[str]) -> Generator[Self,
                                                                None, None]:
        """Returns a generator of formulas object grouped by columns (iterable)
        """
        grouper = self._formula_data.groupby(columns)
        for _, data in grouper:
            yield Formulas(data)
