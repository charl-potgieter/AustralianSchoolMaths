"""This Module contains classes of maths objects including:
    -  formulas
    -  descriptions
"""

import os
import pandas as pd


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
        if isinstance(file_path_or_data, str):
            self._hierarchy_data = pd.read_csv(
                filepath_or_buffer=file_path_or_data)
        elif isinstance(file_path_or_data, pd.core.frame.DataFrame):
            self._hierarchy_data = file_path_or_data.copy()
        # Utilised for iterator

        if self._inconsistent_hierarchy_sort_path():
            raise ValueError(
                'Inconsistent site hieriarchy file.  '
                + 'Out of order item: '
                + str(self._inconsistent_hierarchy_sort_path()))

        self._current_index = -1

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

    def _inconsistent_hierarchy_sort_path(self):
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

    def to_dataframe(self):
        """Returns the full set of hierarhcies as a pandas dataframe"""
        return self._hierarchy_data.copy()

    def to_list(self):
        """Returns the full set of hierarhcies as a list"""
        return self._hierarchy_data.values.tolist()

    def filter_by_depth(self, depth):
        """Returns a new filtered WebPagHierarchies object where the paths are
        'depth' deep.

        Args:
            level_number (int): Number of levels to return.
        """
        max_hierarchy_level = len(self._hierarchy_data.columns)
        return_data = self._hierarchy_data.copy()
        return_data = return_data[
            return_data.iloc[
                :, depth-1].notnull()]
        if depth < max_hierarchy_level:
            return_data = return_data[
                return_data.iloc[
                    :, depth].isnull()]
        return_data = return_data.iloc[
            :, :depth]
        return DirectoryHierarchies(return_data)

    def filter_by_function(self, filter_function):
        """Returns a new filtered WebPagHierarchies object where
        filter_function returns True when passed each item in
        WebPageHierarchies as a pandas series.

        Args:
            filter_function (function): Function taking a pandas series as a
            parameter and returns a Boolean value
        """
        return_rows = self.to_dataframe().apply(filter_function, axis=1)
        return_data = self.to_dataframe()[return_rows]
        return DirectoryHierarchies(return_data)

    def get_sort_index(self, dir_to_find):
        """Looks up dir_to_find in the hierarchies stored in this class as
        follows:
         - filters on stored hierarchies of same number of path levels as
           dir_to_find
         - filters stored hierarches equal to dir_to_find for all path
           levels excluding the last level
         - returns the index of the first match found otherwise none

        Args:
            dir_to_find (list): the directory to find
        """

        # Get unique hierarchies of the same length as hierarchy_to_find
        hierarchies_to_search = self._hierarchy_data.copy()
        hierarchies_to_search = hierarchies_to_search.iloc[
            :, :len(dir_to_find)]
        hierarchies_to_search = hierarchies_to_search.drop_duplicates()

        # Restrict hieararchy_to_search to paths equal to dir_to_find
        # when the last path level is excluded
        hierarchies_to_search = hierarchies_to_search[
            hierarchies_to_search.apply(
                lambda x: tuple(x)[:-1], axis=1) == tuple(dir_to_find[:-1])
        ]
        hierarchies_to_search = hierarchies_to_search.reset_index(drop=True)

        # Filter hierarchies by dir_to_find and return first index
        hierarchies_to_search = hierarchies_to_search[
            # https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unnecessary-lambda.html
            hierarchies_to_search.apply(tuple, axis=1) == tuple(dir_to_find)]
        if len(hierarchies_to_search):
            return hierarchies_to_search.index[0]
        return None

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
