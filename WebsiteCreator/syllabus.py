# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from typing import Callable, Self
import pandas as pd
import numpy as np
from data_validator import DataColumnValidator


class Syllabus():
    """Contains syllabus details"""

    # Enforces structure of csv when loaded
    _data_structure = {'State': 'object',
                       'Subject': 'object',
                       'Syllabus_topic': 'object',
                       'Syllabus_subtopic_code': 'object',
                       'Syllabus_subtopic': 'object'}

    def __init__(self, input_data: pd.DataFrame):
        column_validator = DataColumnValidator(
            list(input_data.columns), list(self._data_structure.keys()))
        column_validator.validate_column_names()
        self._syllabus_data = input_data.astype(self._data_structure)
        self._is_cumulative = False

    @property
    def is_cumulative(self) -> bool:
        """Returns whether this obeject is cumulative across
        subjects (years)"""
        return self._is_cumulative

    @is_cumulative.setter
    def is_cumulative(self, value: bool):
        """Sets this objects is cumulative status representing whether
        it contains items that are cumulative across subjects / years"""
        self._is_cumulative = value

    @property
    def data(self) -> pd.DataFrame:
        return self._syllabus_data

    @data.setter
    def data(self, values: pd.DataFrame):
        self._syllabus_data = values

    def copy(self) -> Self:
        new_syllabus = Syllabus(self.data.copy())
        new_syllabus.is_cumulative = self.is_cumulative
        return new_syllabus

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

    def filter_by_function(self, filter_function: Callable) -> Self:
        """Returns a new filtered Syllabus object where
        filter_function returns True when passed each item in
        Formulas as a pandas series.
        """
        new_syllabus = self.copy()
        return_mask = new_syllabus.data.apply(filter_function, axis=1)
        new_syllabus.data = pd.DataFrame(new_syllabus.data[return_mask])
        return new_syllabus

    @property
    def unique_subtopics(self) -> list[str]:
        return list(set(self._syllabus_data['Syllabus_subtopic']))
