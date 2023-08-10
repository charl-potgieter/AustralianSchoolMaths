# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from data_validator import DataColumnValidator


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
        self._formula_data = input_data
        DataColumnValidator().validate_column_names(
            input_data.columns, self._data_structure.keys())
        self._formula_data = self._formula_data.astype(self._data_structure)
        self._is_cumulative = False

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
