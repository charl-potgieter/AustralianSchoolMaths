"""This Module contains classes relating the various file content types
e.g. formulas, definitions etc
"""

import numpy as np
from data_management import DataManager


class Formulas():
    """Contains the formulas object representing different views / slices
    of the given input set of formulas
    """

    # Enforces structure of csv when loaded
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

    def __init__(self, input_data):
        """Initiates class with data from input_data"""
        data_to_load = DataManager(input_data)
        self._check_column_names(data_to_load)
        data_to_load.set_column_types(self._data_structure)
        self._formula_data = data_to_load.to_dataframe()
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
        """Returns whether this Formulas obeject is cumulative across
        subjects (years)"""
        return self._is_cumulative

    @is_cumulative.setter
    def is_cumulative(self, value: bool):
        """Sets this objects is cumulative status representing whether
        it contains formulas that are cumulative across subjects / years"""
        self._is_cumulative = value

    def to_dataframe(self):
        """Returns formula data as a pandas dataframe
        """
        return self._formula_data

    @property
    def formula_sheet_items(self):
        """Returns a list of formulas where field 'On_formula_sheet'
        is True
        """
        formulas_on_sheet = (self._formula_data[
            (self._formula_data['On_formula_sheet']) &
            (self._formula_data['Formula'].notnull())
        ]['Formula'].drop_duplicates())
        return list(formulas_on_sheet)

    @property
    def proofs_required_items(self):
        """Returns a list of formulas where field 'Proof_required'
         is True

        Args:
            state (string): filter to apply before returning items
        """
        proofs_required = (self._formula_data[
            (self._formula_data['Proof_required']) &
            (self._formula_data['Formula'].notnull())
        ]['Formula'].drop_duplicates())
        return list(proofs_required)

    def filter_by_function(self, filter_function):
        """Returns a new filtered Formulas object where
        filter_function returns True when passed each item in
        Formulas as a pandas series.

        Args:
            filter_function (function): Function taking a pandas series as a
            parameter and returns a Boolean value
        """
        return_rows = self._formula_data.apply(filter_function, axis=1)
        return_data = self._formula_data.copy()[return_rows]
        return Formulas(return_data)

    def field_value(self, field_name):
        """Returns the value in field_name.  If multiple non-unique values exist
        return 'Multiple Values'"""
        unique_values_in_field = (
            self._formula_data[field_name].drop_duplicates())
        if len(unique_values_in_field) == 1:
            return list(unique_values_in_field)[0]
        return 'Multiple values'

    def group_by_columns(self, columns):
        """Returns a generator of formulas object grouped by columns (iterable)
        """
        grouper = self._formula_data.groupby(columns)
        for _, data in grouper:
            yield Formulas(data)


class Syllabus():
    """Contains syllabus details"""

    # Enforces structure of csv when loaded
    _data_structure = {'State': 'object',
                       'Subject': 'object',
                       'Syllabus_topic': 'object',
                       'Syllabus_subtopic_code': 'object',
                       'Syllabus_subtopic': 'object'}

    def __init__(self, input_data):
        """Initiates class with data from input_data"""
        data_to_load = DataManager(input_data)
        self._check_column_names(data_to_load)
        data_to_load.set_column_types(self._data_structure)
        self._syllabus_data = data_to_load.to_dataframe()
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
        """Returns whether this Syllabus obeject is cumulative across
        subjects (years)"""
        return self._is_cumulative

    @is_cumulative.setter
    def is_cumulative(self, value: bool):
        """Sets this objects is cumulative status representing whether
        it contains syllabus that are cumulative across subjects / years"""
        self._is_cumulative = value

    def topic_summary_level(self):
        """Returns syllabus at a unique state, subject topic level with
        subtopic related fiels as Nan
        """
        return_data = self._syllabus_data.copy()
        return_data = (
            return_data[['State', 'Subject', 'Syllabus_topic']]
            .drop_duplicates())
        return_data['Syllabus_subtopic_code'] = np.NAN
        return_data['Syllabus_subtopic'] = np.NAN
        return_value = Syllabus(return_data)
        # TODO the way the is_cumilative property is being copied across is needs improving
        return_value.is_cumulative = self.is_cumulative
        return return_value

    def filter_by_function(self, filter_function):
        """Returns a new filtered Syllabus object where
        filter_function returns True when passed each item in
        Syllabus as a pandas series.

        Args:
            filter_function (function): Function taking a pandas series as a
            parameter and returns a Boolean value
        """
        return_rows = self._syllabus_data.apply(filter_function, axis=1)
        return_data = self._syllabus_data.copy()[return_rows]
        return_value = Syllabus(return_data)
        # TODO the way the is_cumilative property is being copied across is needs improving
        return_value.is_cumulative = self.is_cumulative
        return return_value

    @property
    def subtopics(self):
        """Retuns subtopics as a list"""
        return list(self._syllabus_data['Syllabus_subtopic'])

    def to_dataframe(self):
        """Returns syllabus data as a pandas dataframe
        """
        return self._syllabus_data


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
        data_to_load = DataManager(input_data)
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
