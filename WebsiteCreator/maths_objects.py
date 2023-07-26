"""This Module contains classes of maths objects including:
    -  formulas
    -  descriptions
"""

import os
import pandas as pd


class DataManager():
    """Reads, validates and returns data"""

    def __init__(self, file_path_or_data):
        """Initiates class with content of csv or data

        Args:
            file_path_or_data (string or datafram): Either input csv file path
                or pandas dataframe
        """
        if isinstance(file_path_or_data, str):
            self._data = pd.read_csv(
                filepath_or_buffer=file_path_or_data)
        elif isinstance(file_path_or_data, pd.core.frame.DataFrame):
            self._data = file_path_or_data.copy()

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


class DirectoryHierarchies():
    """Stores, retrieves, filters and creates file directory (path) hierarchies
       as well as their indexed sort orders
    """

    def __init__(self, file_path_or_data):
        """Initiates class with content of csv or data

        Args:
            file_path_or_data (string or datafram): Eitherinput csv file path
                or pandas dataframe
        """
        self._hierarchy_data = DataManager(file_path_or_data).to_dataframe()
        self._current_index = -1  # Utilised for iterator
        if self._first_hierarchy_with_inconsistent_sort_order():
            raise ValueError(
                'Inconsistent site hieriarchy file.  '
                + 'Out of order item: '
                + str(self._first_hierarchy_with_inconsistent_sort_order()))

    def __getitem__(self, item):
        """Returns the item-th hierarchy stored in this class (removing
        null values) and returns result as a a pandas series.
        """
        return_value = self.to_dataframe().iloc[item]
        return_value = return_value[return_value.notnull()]
        return return_value

    def __iter__(self):
        """Initialise the iterator"""
        self._current_index = -1
        return self

    def __next__(self):
        """Implelemts the next item of the class iterator
        """
        max_index = len(self.to_dataframe().index)-1
        self._current_index += 1
        if self._current_index <= max_index:
            return self[self._current_index]
        raise StopIteration

    def _first_hierarchy_with_inconsistent_sort_order(self):
        """Checks for sort consistency in hieriarchies.  Returns a string
        containing the first inconsistent sort path found, othewise None.
        Example: Below is inconsistent as all the Path_A in
        first levels of the hierarchies below are not consecutive
            /path_A/path_B
            /path_A/path_C
            /path_B/Path_X
            /path_A/Path_Y
        """
        for i in range(len(self._hierarchy_data.columns)):
            current_level_data = self._hierarchy_data.iloc[:, :i+1].copy()
            current_level_data_last_path = current_level_data.iloc[:, i]
            current_level_data = current_level_data[
                current_level_data_last_path.notnull()]
            ordered_paths = list(
                # https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unnecessary-lambda.html
                current_level_data.apply(list, axis=1))
            inconsistent_item = (
                self._first_non_consecutive_like_item(ordered_paths))
            if inconsistent_item:
                return inconsistent_item
        return None

    def _first_non_consecutive_like_item(self, input_values):
        """Returns first item if it is an item in input_values that equals
        another item in input_values but they do not appear consecutively,
        otherwise returns None.

        Args:
            input_values (iterable): Values to test
        """

        values_ex_consecutive_duplicates = []
        for item in input_values:
            if not values_ex_consecutive_duplicates:
                values_ex_consecutive_duplicates.append(item)
            elif item != values_ex_consecutive_duplicates[-1]:
                values_ex_consecutive_duplicates.append(item)
                if values_ex_consecutive_duplicates.count(item) != 1:
                    return item
        return None

    def copy(self):
        """Creates a copy of the this object
        """
        new_hierarchy_data = self._hierarchy_data.copy()
        return DirectoryHierarchies(new_hierarchy_data)

    def to_dataframe(self):
        """Returns the full set of hierarhcies as a pandas dataframe"""
        return self._hierarchy_data.copy()

    def to_list(self):
        """Returns the full set of hierarhcies as a list"""
        return self._hierarchy_data.values.tolist()

    def filter_by_function(self, filter_function):
        """Returns a new filtered WebPagHierarchies object where
        filter_function returns True when passed each item in
        WebPageHierarchies as a pandas series.

        Args:
            filter_function (function): Function taking a pandas series as a
            parameter and returns a Boolean value
        """
        return_rows = self.to_dataframe().apply(filter_function, axis=1)
        return_data = self.to_dataframe().copy()[return_rows]
        return DirectoryHierarchies(return_data)

    def get_sort_index(self, dir_to_find):
        """Returns sort index of dir_to_find relative to all paths in the
            hierarchies stored in this object

        Args:
            dir_to_find (iterable): The directory (path) for which the sort
                index is to be returned
        """
        matching_hierarchies = self.filter_by_path(dir_to_find)
        if len(matching_hierarchies.to_dataframe()):
            return matching_hierarchies.to_dataframe().index[0]
        return None

    def get_sort_index_in_parent_path(self, dir_to_find):
        """Returns sort_index of dir_to_find relative to other directories
        with the same parent path

        Args:
            dir_to_find (list): the directory to find
        """
        unique_truncated_hierarchies = (
            self.truncate_to_path_length(len(dir_to_find)).unique())
        if len(dir_to_find) > 1:
            hierarchies_with_same_parent = (
                unique_truncated_hierarchies
                .filter_by_path_start(dir_to_find[:-1]))
        else:
            hierarchies_with_same_parent = unique_truncated_hierarchies
        hierarchies_with_same_parent = (
            hierarchies_with_same_parent.reset_sort_index())
        return hierarchies_with_same_parent.get_sort_index(dir_to_find)

    def truncate_to_path_length(self, path_length):
        """Restricts  hieararches to paths of path_length and returns as a
        new object

        Args:
            path_length (int): The path length restriction to apply when
                creating the object copy.
        """
        hierarchy_data_to_length = self._hierarchy_data.iloc[
            :, :path_length].copy()
        hierarchies_to_length = DirectoryHierarchies(hierarchy_data_to_length)
        return hierarchies_to_length

    def unique(self):
        """Restricts hierarchies to unique values and returns as a new object
        """
        unique_hierarchy_data = self._hierarchy_data.copy()
        unique_hierarchy_data = unique_hierarchy_data.drop_duplicates()
        return DirectoryHierarchies(unique_hierarchy_data)

    def reset_sort_index(self):
        """Resets the hiearatchy sort order to commence from zero and return
        as a new object
        """
        return DirectoryHierarchies(
            self._hierarchy_data.copy().reset_index(drop=True))

    def filter_by_path(self, path_to_filter):
        """filters hieararchies where each hierarchy equals value_to_filter
            and returns as a new object
        Args:
            value_to_filter (iterable): the value to filter on
        """
        filtered_hierarchy_data = self._hierarchy_data.copy()
        filtered_hierarchy_data = filtered_hierarchy_data[
            filtered_hierarchy_data.apply(tuple, axis=1)
            == tuple(path_to_filter)
        ]
        return DirectoryHierarchies(filtered_hierarchy_data)

    def filter_by_path_start(self, path_to_filter):
        """Filters hieararchies by value_to_filter where the
        start of each item (same length as value_to_filter) in
        hieararchies equals value_to_filter and returns hierarchies as a new
        object

        Args:
            value_to_filter (iterable): The value to filter by
        """
        hierarchies_to_filter = self._hierarchy_data.copy()
        hierarchies_to_search = hierarchies_to_filter.iloc[
            :, :len(path_to_filter)]
        filtered_hierarchies = hierarchies_to_filter[
            hierarchies_to_search.apply(
                tuple, axis=1) == tuple(path_to_filter)
        ]
        return DirectoryHierarchies(filtered_hierarchies)

    def create_directories(self, base_dir):
        """Creates directory by concatanating base_dir with the directories
        stored in this class

        Args:
            base_dir (string): The base directory to concentate with the
                directories stored in this classs
        """
        for current_path in self:
            fname = base_dir + os.path.sep + os.path.sep.join(current_path)
            os.makedirs(fname)

    def all_path_levels(self, base_dir=None):
        """Returns a list of unique paths recursively at each directory level
        for the directory hierarchies stored in this class, optionally prefixed
        woth base_dir

        Args:
            base_dir (string, optional): Optional prefix to all returned path
                levels. Defaults to None.
        """

        all_path_levels = []
        for column_index in range(len(self._hierarchy_data.columns)):
            paths_at_current_level = self._hierarchy_data.iloc[
                :, :column_index+1]
            paths_at_current_level = (paths_at_current_level
                                      .drop_duplicates().dropna())
            if base_dir:
                paths_at_current_level = paths_at_current_level.apply(
                    lambda x: os.path.sep.join([base_dir] + list(x)), axis=1)
            else:
                paths_at_current_level = paths_at_current_level.apply(
                    os.path.sep.join, axis=1)
            all_path_levels = all_path_levels + list(paths_at_current_level)
        all_path_levels = list(set(all_path_levels))
        return all_path_levels


class IndexFile():
    """Creates, and contents and saves _index.md files
    """

    def __init__(self):
        self._dict = {}

    def add_property(self, property_key, property_value):
        """Adds property_value for corresponding property_key to the
        index file"""

        self._dict[property_key] = property_value

    def _content(self):
        """Returns the content of index file as a string"""
        return_value = '---\n'
        if self._dict:
            for key, value in self._dict.items():
                return_value += str(key) + ': ' + str(value) + '\n'
        return_value += '---'
        return return_value

    def save(self, target_dir):
        """Saves the content of this IndexFileClass as an ._index.md in
        directory dir.

        Args:
            file_directory (string): The directory excluding file name where
                the ._index.md file will be saved.
        """
        file_name = target_dir + os.path.sep + '_index.md'
        if os.path.isfile(file_name):
            raise OSError('Cannot create ._index.md file as it already ' +
                          'exists at directory ' + target_dir)
        else:
            with open(file_name, "w", encoding="utf-8") as text_file:
                text_file.write(self._content())


class Formulas():
    """Contains the formulas object representing different views / slices
    of the given input set of formulas
    """

    # Specifies felds for conversion when the formula csv is loaded during
    # class init
    _formula_input_converter = {
        'On formula sheet': lambda x: True if x else False,
        'Proof required': lambda x: True if x else False}

    # Enforces structure of fomulas csv when loaded along with the
    # _formula_input_converter
    _formula_input_structure = {'State': str,
                                'Syllabus subtopic code': str,
                                'Category': str,
                                'Subcategory_1': str,
                                'Subcategory_2': str,
                                'Description': str,
                                'Group': str,
                                'Formula': str,
                                'Subject': str,
                                'Comment': str}
    # Enforces structure of syllabus.csv which is loaded during class init
    _syllabus_input_structure = {'State': str,
                                 'Subject': str,
                                 'Syllabus topic': str,
                                 'Syllabus subtopic code': str,
                                 'Syllabus subtopic': str}

    def __init__(self, formula_input_file_path, syllabus_input_file_path,
                 page_sort_orders):
        """Initiates class with csv located at input_file_path

        Args:
            formula_input_file_path (string): input csv file path
            page_sort_orders (WebPageSortOrders) : Object storing
                details of the web page sort orders
        """
        self._page_sort_orders = page_sort_orders
        formula_cols_to_use = (
            list(self._formula_input_structure.keys()) +
            list(self._formula_input_converter.keys())
        )
        formula_detail_df = pd.read_csv(
            filepath_or_buffer=formula_input_file_path,
            usecols=formula_cols_to_use,
            dtype=self._formula_input_structure,
            converters=self._formula_input_converter
        )
        syllabus_cols_to_use = list(self._syllabus_input_structure.keys())
        syllabus_detail_df = pd.read_csv(
            filepath_or_buffer=syllabus_input_file_path,
            usecols=syllabus_cols_to_use,
            dtype=self._syllabus_input_structure
        )
        self._formula_detail_df = formula_detail_df.merge(
            right=syllabus_detail_df,
            left_on=['State', 'Subject', 'Syllabus subtopic code'],
            right_on=['State', 'Subject', 'Syllabus subtopic code'],
            how='left')

    def by_year(self):
        """Returns detail dataframe with formula related information
        """
        return self._formula_detail_df

    def by_year_cumulative(self):
        """Returns formula details dataframe on a cumulative level by subject
        order  as provided in the page_sort_order object on class init.
        For example if subject Year 12 is ordered after Year 10 and Year 9 for
        a given state then include the formula details for Year 10 and Year 9
        in the dataframe under subject Year 12.
        """

        state_subject_order_df = (
            self._page_sort_orders.formulas_cumulative_state_subject())
        # Add the subject Sort order (representing the sort order for the
        # subject by given state) to the formulas file
        return_df = state_subject_order_df.merge(
            right=self._formula_detail_df,
            how='inner',
            left_on=['Sort state', 'Sort subject'],
            right_on=['State', 'Subject']
        )
        return_df = return_df.rename(
            columns={'Sort order': 'Subject sort order'})
        return_df = return_df.drop(columns=['Sort state',
                                            'Sort subject'])
        return_df = return_df.merge(
            right=state_subject_order_df,
            how='inner', left_on=['State'], right_on=['Sort state']
        )
        return_df = return_df[return_df['Sort order'] >=
                              return_df['Subject sort order']]
        return_df = return_df.drop(columns=['Sort order',
                                            'Subject sort order',
                                            'Sort state', 'Subject'])
        return_df = return_df.rename(columns={
            'Sort subject': 'Subject'
        })
        return return_df

    def formula_sheet_items_by_state(self, state):
        """Returns a pandas series of formulas where field 'On formula sheet'
        per the csv utilised to init this class is True and State = state

        Args:
            state (string): filter to apply before returning formula sheet
                            items
        """
        formulas_on_sheet = (self._formula_detail_df[
            (self._formula_detail_df['State'] == state) &
            (self._formula_detail_df['On formula sheet']) &
            (self._formula_detail_df['Formula'].notnull())
        ]['Formula'].drop_duplicates())
        return formulas_on_sheet

    def proofs_required_by_state(self, state):
        """Returns a pandas series of formulas where field 'Proof required'
        per the csv utilised to init this class is True and State = state

        Args:
            state (string): filter to apply before returning items
        """
        formulas_on_sheet = (self._formula_detail_df[
            (self._formula_detail_df['State'] == state) &
            (self._formula_detail_df['Proof required']) &
            (self._formula_detail_df['Formula'].notnull())
        ]['Formula'].drop_duplicates())
        return formulas_on_sheet

    def by_year_dirs(self):
        """Returns a dataframe containing target directories to
        save formula by year pages where each column in the dataframe
        represents a different directory level
        """
        by_year_df = self.by_year().copy()
        by_year_df['Formula subcategory 1'] = 'Formulas'
        by_year_df['Formula subcategory 2'] = 'By Year'
        by_year_df = by_year_df[['State', 'Formula subcategory 1',
                                 'Formula subcategory 2',
                                 'Subject']].drop_duplicates()
        return by_year_df

    def by_year_cumulative_dirs(self):
        """Returns a dataframe containing target directories to
        save formula by year cumulative pages where each column in the
        dataframe represents a different directory level
        """
        by_year_df = self.by_year_cumulative().copy()
        by_year_df['Formula subcategory 1'] = 'Formulas'
        by_year_df['Formula subcategory 2'] = 'By year cumulative'
        by_year_df = by_year_df[['State', 'Formula subcategory 1',
                                 'Formula subcategory 2',
                                 'Subject']].drop_duplicates()
        return by_year_df
