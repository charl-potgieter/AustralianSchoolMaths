"""This Module contains classes of maths objects including:
    -  formulas
    -  descriptions
"""

import pandas as pd


class WebPageSortOrders():
    """Implements Sort order views for ordering pages on maths website
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

    def formulas_by_year_state_subject_code(self):
        """Filters this classes input dataframe, renames columns and returns an
        ordered pandas dataframe representing the web page (menu) order of the
        'formula by year' section at a state and subject_code page level, where
         each column in the dataframe represents the (ordered) level in the
         menu.  Below columns are returned in the dataframe:
         - Sort order
         - Sort state
         - Sort subject code
        """

        return_value = self._sort_order_input.rename(
            columns={'Level_0': 'Sort state',
                     'Level_1': 'Formula subcategory 1',
                     'Level_2': 'Formula subcategory 2',
                     'Level_3': 'Sort subject code',
                     'Level_4': 'Sort category'})
        return_value = return_value[
            (return_value['Formula subcategory 1'].str.upper() ==
             'FORMULAS') &
            (return_value['Formula subcategory 2'].str.upper() ==
             'BY YEAR') &
            (return_value['Sort subject code'].notnull()) &
            (return_value['Sort category'].isnull())].copy()
        return_value = return_value.reset_index(drop=True)
        return_value['Sort order'] = return_value.index
        return_value = return_value[['Sort order', 'Sort state',
                                     'Sort subject code']]
        return return_value

    def formulas_by_year_state_subject_code_category(self):
        """Filters this classes input dataframe, renames columns and returns an
        ordered pandas dataframe representing the web page (menu) order of the
        'formula by year' section at a state and subject_code and category page
        level, where each column in the dataframe represents the (ordered)
        level in the menu. Below columns are returned in the dataframe:
         - Sort order
         - Sort state
         - Sort subject code
         - Sort category
        """

        return_value = self._sort_order_input.rename(
            columns={'Level_0': 'Sort state',
                     'Level_1': 'Formula subcategory 1',
                     'Level_2': 'Formula subcategory 2',
                     'Level_3': 'Sort subject code',
                     'Level_4': 'Sort category'})
        return_value = (
            return_value[
                (return_value['Formula subcategory 1'].str.upper() ==
                 'FORMULAS') &
                (return_value['Formula subcategory 2'].str.upper() ==
                 'BY YEAR') &
                (return_value['Sort subject code'].notnull()) &
                (return_value['Sort category'].notnull()) &
                (return_value['Level_5'].isnull())]).copy()
        return_value = return_value.reset_index(drop=True)
        return_value['Sort order'] = return_value.index
        return_value = return_value[['Sort order', 'Sort state',
                                     'Sort subject code', 'Sort category']]
        return return_value

    def formulas_cumulative_state_subject_code(self):
        """Filters this classes input dataframe, renames columns and returns an
        ordered pandas dataframe representing the web page (menu) order of the
        cumulative formula pages by state and subject code, where each
        column in the dataframe represents the (ordered) level in the menu.
        Below columns are returned in the dataframe:
         - Sort order
         - Sort state
         - Sort subject code
        """

        return_value = self._sort_order_input.rename(
            columns={'Level_0': 'Sort state',
                     'Level_1': 'Formula subcategory 1',
                     'Level_2': 'Formula subcategory 2',
                     'Level_3': 'Sort subject code',
                     'Level_4': 'Sort category'})
        return_value = return_value[
            (return_value['Formula subcategory 1'].str.upper() ==
             'FORMULAS') &
            (return_value['Formula subcategory 2'].str.upper() ==
             'BY YEAR CUMULATIVE') &
            (return_value['Sort subject code'].notnull()) &
            (return_value['Sort category'].isnull())].copy()
        return_value = return_value.reset_index(drop=True)
        return_value['Sort order'] = return_value.index
        return_value = return_value[['Sort order', 'Sort state',
                                     'Sort subject code']]
        return return_value

    def formulas_cumulative_state_subject_code_category(self):
        """Filters this classes input dataframe, renames columns and returns an
        ordered pandas dataframe representing the web page (menu) order of the
        cumulative formula subject pages by state, subject code and category
        where each column in the dataframe represents the (ordered) level in
        the menu.  Below columns are returned in the dataframe:
         - Sort order
         - Sort state
         - Sort subject code
         - Sort category
        """

        return_value = self._sort_order_input.rename(
            columns={'Level_0': 'Sort state',
                     'Level_1': 'Formula subcategory 1',
                     'Level_2': 'Formula subcategory 2',
                     'Level_3': 'Sort subject code',
                     'Level_4': 'Sort category'})
        return_value = (
            return_value[
                (return_value['Formula subcategory 1'].str.upper() ==
                 'FORMULAS') &
                (return_value['Formula subcategory 2'].str.upper() ==
                 'BY YEAR CUMULATIVE') &
                (return_value['Sort subject code'].notnull()) &
                (return_value['Sort category'].notnull()) &
                (return_value['Level_5'].isnull())]).copy()
        return_value = return_value.reset_index(drop=True)
        return_value['Sort order'] = return_value.index
        return_value = return_value[['Sort order', 'Sort state',
                                     'Sort subject code',
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
                                'Subject code': str,
                                'Comment': str
                                }

    def __init__(self, formula_input_file_path):
        """Initiates class with csv located at input_file_path

        Args:
            formula_input_file_path (string): input csv file path
        """
        cols_to_use = (
            list(self._formula_input_structure.keys()) +
            list(self._formula_input_converter.keys())
        )
        self._formula_detail_df = pd.read_csv(
            filepath_or_buffer=formula_input_file_path,
            usecols=cols_to_use,
            dtype=self._formula_input_structure,
            converters=self._formula_input_converter
        )

    def formula_detail(self):
        """Returns detail dataframe with formula related information
        """
        return self._formula_detail_df

    def get_formulas_by_year_cumulative_df(self, state_subject_code_order_df):
        """Returns formula details dataframe on a cumulative level by subject
        code order  as provided in state_subject_code_order_df per
        state(province).  For example if subject code Year 12 is ordered after
        Year 10 and Year 9 for a given state then include the formula details
        for Year 10 and Year 9 in the dataframe under subject code Year 12.

        Args:
            state_subject_code_order_df (pandas dataframe): Contains the below
                columns:
                 - Sort order
                 - Sort state
                 - Sort subject code
        """

        # Add the subject Sort order (representing the sort order for the
        # subject by given state) to the formulas file
        return_df = state_subject_code_order_df.merge(
            right=self._formula_detail_df,
            how='inner',
            left_on=['Sort state', 'Sort subject code'],
            right_on=['State', 'Subject code']
        )
        return_df = return_df.rename(
            columns={'Sort order': 'Subject sort order'})
        return_df = return_df.drop(columns=['Sort state',
                                            'Sort subject code'])
        return_df = return_df.merge(
            right=state_subject_code_order_df,
            how='inner', left_on=['State'], right_on=['Sort state']
        )
        return_df = return_df[return_df['Sort order'] >=
                              return_df['Subject sort order']]
        return_df = return_df.drop(columns=['Sort order',
                                            'Subject sort order',
                                            'Sort state', 'Subject code'])
        return_df = return_df.rename(columns={
            'Sort subject code': 'Subject code'
        })
        return return_df
