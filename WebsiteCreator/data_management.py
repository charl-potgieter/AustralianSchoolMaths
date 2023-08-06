"""This Module contains classes relating to data management"""

import os
import pandas as pd


class DataSource():
    """Gets file directories and data source from underlying files (sometimes
    requiring merging and filtering and returns data as pandas dataframes)
    """

    @property
    def website_creator_directory(self):
        """Returns the directory containing various files utilised to
        create the hugo website by relative reference to the directory
        of the file containgin this code"""
        this_file_path = os.path.dirname(__file__)
        return this_file_path

    @property
    def docs_directory(self):
        """Returns the docs directory used to generate Hugo website content.
        The directory path is determined by relative reference the file
        containing this code"""
        this_file_path = os.path.dirname(__file__)
        return (os.path.join(
            os.path.dirname(this_file_path),
            'content', 'docs'))

    @property
    def hierarchies_file_path(self):
        """Returns directory string of site_hierarchy.csv file"""
        return (self.website_creator_directory
                + os.path.sep
                + 'site_hierarchy.csv')

    @property
    def formulas_file_path(self):
        """Returns directory string of formulas.csv file"""
        return (self.website_creator_directory + os.path.sep
                + 'formulas.csv')

    @property
    def definitions_file_path(self):
        """Returns directory string of definitions.csv file"""
        return (self.website_creator_directory + os.path.sep
                + 'definitions.csv')

    @property
    def syllabus_directory(self):
        """Returns directory string of syllabus_topics.csv file"""
        return (self.website_creator_directory + os.path.sep
                + 'syllabus_topics.csv')

    @property
    def syllabus(self):
        """Returns the syllabus data as dataframe"""
        return pd.read_csv(self.syllabus_directory)

    @property
    def site_hierarchies(self):
        """Returns the site hierarchy data as a pandas dataframe
        """
        hierarchy_data = pd.read_csv(self.hierarchies_file_path)
        return hierarchy_data

    @property
    def state_subject_sort_orders(self):
        """Returns subjects in order per state as a dataframe
        """
        return_data = self.site_hierarchies
        return_data = return_data[
            (return_data['Content type'] == 'Formulas') &
            (return_data['Time period'] == 'By year')
        ]
        return_data = return_data[['State', 'Subject']].drop_duplicates()
        return_data = return_data.reset_index(drop=True)
        return_data = return_data.rename(
            columns={'State': 'Sort state', 'Subject': 'Sort subject'}
        )
        return_data['State subject sort order'] = return_data.index
        return return_data

    @property
    def formulas_by_year(self):
        """Returns dataframe of formulas and related fields by merging
        formulas (ex-syllabus) and syllabus files
        """

        # TODO Temporarily mark empty boolean fields as false to avoid type errors
        # Remove once all data capture is complete
        formulas_input_converter = {
            'Proof required': lambda x: True if x else False}
        formulas_ex_syllabus = pd.read_csv(
            filepath_or_buffer=self.formulas_file_path,
            converters=formulas_input_converter)
        formulas = pd.merge(
            left=self.syllabus, right=formulas_ex_syllabus,
            left_on=['State', 'Subject', 'Syllabus subtopic code'],
            right_on=['State', 'Subject', 'Syllabus subtopic code'],
            how='right')
        return formulas

    @property
    def formulas_by_year_cumulative(self):
        """Returns formula details dataframe on a cumulative level by subject
        order  for a given state.
        For example if subject Year 12 is ordered after Year 10 and Year 9 for
        a given state then include the formula details for Year 10 and Year 9
        in the dataframe under subject Year 12.
        """

        formulas_by_year = self.formulas_by_year
        state_subject_sort_orders = self.state_subject_sort_orders

        # Add the subject Sort order (representing the sort order for the
        # subject by given state) to the formulas data
        return_data = state_subject_sort_orders.merge(
            right=formulas_by_year,
            how='inner',
            left_on=['Sort state', 'Sort subject'],
            right_on=['State', 'Subject']
        )
        return_data = return_data.rename(
            columns={
                'State subject sort order': 'Data sort index'})
        return_data = return_data.drop(columns=['Sort state',
                                                'Sort subject'])

        return_data = return_data.merge(
            right=state_subject_sort_orders,
            how='inner', left_on=['State'], right_on=['Sort state']
        )
        return_data = return_data[return_data['State subject sort order'] >=
                                  return_data['Data sort index']]
        return_data = return_data.drop(columns=['Data sort index',
                                                'State subject sort order',
                                                'Sort state', 'Subject'])
        return_data = return_data.rename(columns={
            'Sort subject': 'Subject'})
        return return_data

    @property
    def definitions_by_year(self):
        """Returns the maths definitions as a pandas dataframe
        """
        definitions_data = pd.read_csv(self.definitions_file_path)

        definitions_data = pd.merge(
            left=self.syllabus, right=definitions_data,
            left_on=['State', 'Subject', 'Syllabus subtopic code'],
            right_on=['State', 'Subject', 'Syllabus subtopic code'],
            how='right')
        return definitions_data


class DataManager():
    """Validates, sets data types and returns data"""

    def __init__(self, data):
        """Initiates class with content of data

        Args:
            data (Pandas dataframe): Input data
        """
        self._data = data.copy()

    def set_column_types(self, column_types):
        """Sets the column types

        Args:
            column_types (dictionary): The column types to set
        """
        self._data = self._data.astype(column_types)

    def to_dataframe(self):
        """Returns data as a pandas dataframe"""
        return self._data

    def column_names_are_correct(self, expected_column_names):
        """Returns true if expected_column_names match the column names
        of the data stored by this object

        Args:
            expected_column_names (iterable): The expected colummn names to
            check against column names of data stored in this object
        """
        number_of_unexpected_columns = len(
            self._unexpected_column_names_in_data(expected_column_names))
        number_of_missing_columns = len(
            self._missing_column_names_in_data(expected_column_names))
        return (number_of_unexpected_columns == 0
                and number_of_missing_columns == 0)

    def column_mismatch_message(self, expected_column_names):
        """Returns a string listing any differences between
        expected_column_names and column_names of data stored in this object.
        Returns None if no differences

        Args:
            expected_column_names (iterable): The expected colummn names to
            check against column names of data stored in this object
        """
        if self.column_names_are_correct(expected_column_names):
            return None
        message = ''
        missing_column_names = (
            self._missing_column_names_in_data(expected_column_names))
        unexpected_column_names = (
            self._unexpected_column_names_in_data(expected_column_names)
        )
        if missing_column_names:
            message += ('The following columns are missing from the data: '
                        + str(missing_column_names) + '\n')
        if unexpected_column_names:
            message += ('The following unexpected columns appear in the data: '
                        + str(unexpected_column_names))
        return message

    def _unexpected_column_names_in_data(self, expected_column_names):
        """Returns a list of column names in this objects data that are not
        in the expected_column_names parameter

        Args:
            expected_column_names (iterable): column names to check
        """
        return list(
            set(self.to_dataframe().columns) - set(expected_column_names))

    def _missing_column_names_in_data(self, expected_column_names):
        """Returns a list of column names that are included in in the
        expected_column_names parameter but do not appear in this objects data

        Args:
            expected_column_names (iterable): column names to check
        """
        return list(
            set(expected_column_names) - set(self.to_dataframe().columns))
