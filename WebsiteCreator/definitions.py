"""This Module contains classes relating the various file content types
e.g. formulas, definitions etc
"""

import numpy as np
from WebsiteCreator.data_validator import DataColumnValidator


class Definitions():
    """Contains maths definitions"""

    # Enforces structure of csv when loaded
    _data_structure = {'State': 'object',
                       'Subject': 'object',
                       'Syllabus_topic': 'object',
                       'Syllabus_subtopic_code': 'object',
                       'Syllabus_subtopic': 'object',
                       'Definition': 'object'}

    def __init__(self, input_data):
        """Initiates class with data from input_data

        Args:
            input_data (dataframe): formula data
        """
        data_to_load = DataColumnValidator(input_data)
        self._check_column_names(data_to_load)
        data_to_load.set_column_types(self._data_structure)
        self._definition_data = data_to_load.to_dataframe()
        self._is_cumulative = False

    def _check_column_names(self, data_to_load):
        """Check if column names in data_to_load match expecations as per
            self._data_structure.  Raise ValueError if not matching.

        Args:
            data_to_load (DataManager): The data to check
        """
        expected_columns = self._data_structure.keys()
        if not data_to_load.column_names_are_correct(expected_columns):
            raise ValueError(
                data_to_load.column_mismatch_message(expected_columns))

    @property
    def is_cumulative(self):
        """Returns whether this obeject is cumulative across
        subjects (years)"""
        return self._is_cumulative

    @is_cumulative.setter
    def is_cumulative(self, value: bool):
        """Sets this objects is cumulative status representing whether
        it contains definitions that are cumulative across subjects / years"""
        self._is_cumulative = value

    def to_dataframe(self):
        """Returns definition data as a pandas dataframe
        """
        return self._definition_data
