"""This Module contains classes of maths objects including:
    -  formulas
    -  descriptions
"""

import pandas as pd


class WebPageHierarchies():
    """Stores and retrieves sort the hierarchies (paths) for website
    pages as well as their indexed orders
    """

    def __init__(self, sort_order_file_path):
        """Initiates class with content of csv

        Args:
            sort_order_file_path (_type_): input csv file path
        """
        self._hierarchy_input = pd.read_csv(
            filepath_or_buffer=sort_order_file_path)

    def all(self):
        """Returns the full set of hierarhcies"""
        return self._hierarchy_input

    def filter(self, level=None):
        """Returns a filtered view of the web page hierarchies with 'level'
        number of non-mull levels.

        Args:
            level (int, optional): Number of levels to return
                Defaults to None.
        """
        max_hierarchy_level = len(self._hierarchy_input.columns)
        return_hierarchy = self._hierarchy_input.copy()
        return_hierarchy = return_hierarchy[
            return_hierarchy.iloc[
                :, level-1].notnull()]
        if level < max_hierarchy_level:
            return_hierarchy = return_hierarchy[
                return_hierarchy.iloc[
                    :, level].isnull()]
        return_hierarchy = return_hierarchy.iloc[
            :, :level]
        return return_hierarchy

    def get_hierararchy_index(self, hierarchy_to_find):
        """Looks up hierarchy_to_find in the hierarchies stored in this class
        and returns the index of the first match found.  The index represents
        the order of hierarchies with same path length as hierarchy_to_find.
        """
        hierarchies_to_search = self._hierarchy_input.copy()
        # length_of_hierarchies_to_search = len(hierarchies_to_search.columns)
        # length_of_hierarchy_to_find = len(hierarchy_to_find)
        # if length_of_hierarchy_to_find > length_of_hierarchies_to_search:
        #     return None

        # # Restrict hierarchies_to_search to non-null rows of the same length
        # # as hierarchy_to_find
        # # !! Refactor below into a seperate (?hidden) sub.  Thinking about keeping visible
        # # !! Can just be part of filter
        # hierarchies_to_search = hierarchies_to_search[
        #     hierarchies_to_search.iloc[
        #         :, length_of_hierarchy_to_find-1].notnull()]
        # if length_of_hierarchy_to_find < length_of_hierarchies_to_search:
        #     hierarchies_to_search = hierarchies_to_search[
        #         hierarchies_to_search.iloc[
        #             :, length_of_hierarchy_to_find].isnull()]
        # hierarchies_to_search = hierarchies_to_search.iloc[
        #     :, :length_of_hierarchy_to_find]

        # # !! Convert dataframe values to a list and then find the index

        return hierarchies_to_search


class WebPageHierarchiesMaybeOutdated():
    """Stores and retrieves sort the hierarchies (paths) for maths site web
    pages as well as their indexed orders
    """

    # Enforces structure of Sort orders csv when loaded
    _sort_order_structure = {'Level_0': str,
                             'Level_1': str,
                             'Level_2': str,
                             'Level_3': str,
                             'Level_4': str,
                             'Level_5': str}

    def __init__(self, sort_order_file_path):
        """Initiates class with content of csv

        Args:
            sort_order_file_path (_type_): input csv file path
        """
        cols_to_use = list(self._sort_order_structure.keys())
        self._sort_order_input = pd.read_csv(
            filepath_or_buffer=sort_order_file_path,
            usecols=cols_to_use,
            dtype=self._sort_order_structure
        )

    def all(self):
        """Returns the full set of hierarhcies"""
        return self._sort_order_input

    def get_hierararchy_index(self, hierarchy_to_find):
        """Looks up hierarchy_to_find in the hierarchies stores in this class
        and returns the index of the first match found.  The index represents
        the order of hierarchies with same path lenght as hierarchy_to_find
        """

        sort_order_workings = self._sort_order_input.copy()
        list_len = len(hierarchy_to_find)
        if list_len > len(sort_order_workings.columns):
            return None

        if list_len < len(sort_order_workings.columns):
            sort_order_workings = sort_order_workings[
                sort_order_workings.iloc[:, list_len].isnull()]

        sort_order_workings = sort_order_workings[
            sort_order_workings.iloc[:, list_len-1].notnull()]

        for i in range(len(hierarchy_to_find)-1):
            sort_order_workings = sort_order_workings[
                (sort_order_workings.iloc[:, i].str.upper() ==
                 str(hierarchy_to_find[i]).upper())]
        sort_order_workings = sort_order_workings.reset_index(drop=True)

        sort_order_workings = sort_order_workings[
            (sort_order_workings.iloc[:, list_len-1].str.upper() ==
             str(hierarchy_to_find[list_len-1]).upper())]
        filtered_index = sort_order_workings.index

        if len(filtered_index) == 0:
            return None
        return filtered_index[0]

    def states(self):
        """Filters this classes input dataframe, renames column and returns an
        ordered pandas dataframe of states (provinces) for purposes of website
        page menu order.  Below columns are returned in the dataframe:
         - Sort order
         - Sort state
        """
        return_value = self._sort_order_input[
            (self._sort_order_input['Level_0'].notnull()) &
            (self._sort_order_input['Level_1'].isnull())
        ].copy()
        return_value = return_value.reset_index(drop=True)
        return_value['Sort order'] = return_value.index
        return_value = return_value.rename(columns={'Level_0': 'Sort state'})
        return_value = return_value[['Sort order', 'Sort state']]
        return return_value

    def formulas_by_year_state_subject(self):
        """Filters this classes input dataframe, renames columns and returns an
        ordered pandas dataframe representing the web page (menu) order of the
        'formula by year' section at a state and subject page level, where
         each column in the dataframe represents the (ordered) level in the
         menu.  Below columns are returned in the dataframe:
         - Sort order
         - Sort state
         - Sort subject
        """

        return_value = self._sort_order_input.rename(
            columns={'Level_0': 'Sort state',
                     'Level_1': 'Formula subcategory 1',
                     'Level_2': 'Formula subcategory 2',
                     'Level_3': 'Sort subject',
                     'Level_4': 'Sort category'})
        return_value = return_value[
            (return_value['Formula subcategory 1'].str.upper() ==
             'FORMULAS') &
            (return_value['Formula subcategory 2'].str.upper() ==
             'BY YEAR') &
            (return_value['Sort subject'].notnull()) &
            (return_value['Sort category'].isnull())].copy()
        return_value = return_value.reset_index(drop=True)
        return_value['Sort order'] = return_value.index
        return_value = return_value[['Sort order', 'Sort state',
                                     'Sort subject']]
        return return_value

    def formulas_by_year_state_subject_category(self):
        """Filters this classes input dataframe, renames columns and returns an
        ordered pandas dataframe representing the web page (menu) order of the
        'formula by year' section at a state and subject and category page
        level, where each column in the dataframe represents the (ordered)
        level in the menu. Below columns are returned in the dataframe:
         - Sort order
         - Sort state
         - Sort subject
         - Sort category
        """

        return_value = self._sort_order_input.rename(
            columns={'Level_0': 'Sort state',
                     'Level_1': 'Formula subcategory 1',
                     'Level_2': 'Formula subcategory 2',
                     'Level_3': 'Sort subject',
                     'Level_4': 'Sort category'})
        return_value = (
            return_value[
                (return_value['Formula subcategory 1'].str.upper() ==
                 'FORMULAS') &
                (return_value['Formula subcategory 2'].str.upper() ==
                 'BY YEAR') &
                (return_value['Sort subject'].notnull()) &
                (return_value['Sort category'].notnull()) &
                (return_value['Level_5'].isnull())]).copy()
        return_value = return_value.reset_index(drop=True)
        return_value['Sort order'] = return_value.index
        return_value = return_value[['Sort order', 'Sort state',
                                     'Sort subject', 'Sort category']]
        return return_value

    def formulas_cumulative_state_subject(self):
        """Filters this classes input dataframe, renames columns and returns an
        ordered pandas dataframe representing the web page (menu) order of the
        cumulative formula pages by state and subject, where each
        column in the dataframe represents the (ordered) level in the menu.
        Below columns are returned in the dataframe:
         - Sort order
         - Sort state
         - Sort subject
        """

        return_value = self._sort_order_input.rename(
            columns={'Level_0': 'Sort state',
                     'Level_1': 'Formula subcategory 1',
                     'Level_2': 'Formula subcategory 2',
                     'Level_3': 'Sort subject',
                     'Level_4': 'Sort category'})
        return_value = return_value[
            (return_value['Formula subcategory 1'].str.upper() ==
             'FORMULAS') &
            (return_value['Formula subcategory 2'].str.upper() ==
             'BY YEAR CUMULATIVE') &
            (return_value['Sort subject'].notnull()) &
            (return_value['Sort category'].isnull())].copy()
        return_value = return_value.reset_index(drop=True)
        return_value['Sort order'] = return_value.index
        return_value = return_value[['Sort order', 'Sort state',
                                     'Sort subject']]
        return return_value

    def formulas_cumulative_state_subject_category(self):
        """Filters this classes input dataframe, renames columns and returns an
        ordered pandas dataframe representing the web page (menu) order of the
        cumulative formula subject pages by state, subject and category
        where each column in the dataframe represents the (ordered) level in
        the menu.  Below columns are returned in the dataframe:
         - Sort order
         - Sort state
         - Sort subject
         - Sort category
        """

        return_value = self._sort_order_input.rename(
            columns={'Level_0': 'Sort state',
                     'Level_1': 'Formula subcategory 1',
                     'Level_2': 'Formula subcategory 2',
                     'Level_3': 'Sort subject',
                     'Level_4': 'Sort category'})
        return_value = (
            return_value[
                (return_value['Formula subcategory 1'].str.upper() ==
                 'FORMULAS') &
                (return_value['Formula subcategory 2'].str.upper() ==
                 'BY YEAR CUMULATIVE') &
                (return_value['Sort subject'].notnull()) &
                (return_value['Sort category'].notnull()) &
                (return_value['Level_5'].isnull())]).copy()
        return_value = return_value.reset_index(drop=True)
        return_value['Sort order'] = return_value.index
        return_value = return_value[['Sort order', 'Sort state',
                                     'Sort subject',
                                     'Sort category']]
        return return_value


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
