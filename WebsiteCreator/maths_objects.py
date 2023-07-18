"""This Module contains classes of maths objects including:
    -  formulas
    -  descriptions
"""

import pandas as pd


class SortOrders():
    """Implements sort order views for ordering pages on maths website
    """

    # Enforces structure of sort orders csv when loaded
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
        """Returns an ordered pandas series of states / provinces represented
        by the ordered items in field 'Level_0' from the  csv used to
        initialise this  SortOrders class where field 'Level_1' is null.

        Returns:
            pandas: ordered list of states
        """
        return self._sort_order_input[
            (self._sort_order_input['Level_0'].notnull()) &
            (self._sort_order_input['Level_1'].isnull())
        ]['Level_0']


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
        self._formula_detail = pd.read_csv(
            filepath_or_buffer=formula_input_file_path,
            usecols=cols_to_use,
            dtype=self._formula_input_structure,
            converters=self._formula_input_converter
        )

    def formula_detail(self):
        """Returns detail dataframe with formula related information

        Returns:
            dataframe: Details of formuls with fields as per
                       self._formula_input_strucutre
        """

        return self._formula_detail

    def formula_detail_cumulative_by_subject(self, subject_order):
        """Returns a dataframe of cumulative formulas based on the subject
        order list.   For example subject Year 12 will include formulas from
        Year 11, Year 10 etc if that is the order provided in the subject
        order parameter

        Args:
            subject_order (list): list of strings reporesenting the subject
            orders

        Returns:
            dataframe: Details of formuls with fields as per
                       self._formula_input_strucutr

        """

    # cumulative_hierarchy_df = sort_orders_df.copy()
    # cumulative_hierarchy_df = cumulative_hierarchy_df.rename(
    #     columns={'Level_0': 'State', 'Level_1': 'Formula subcategory 1',
    #              'Level_2': 'Formula subcategory 2', 'Level_3': 'Subject code',
    #              'Level_4': 'Category'})

    # cumulative_hierarchy_df = (
    #     cumulative_hierarchy_df[
    #         (cumulative_hierarchy_df['Formula subcategory 1'].str.upper() ==
    #          'FORMULAS') &
    #         (cumulative_hierarchy_df['Formula subcategory 2'].str.upper() ==
    #          'BY YEAR CUMULATIVE') &
    #         (cumulative_hierarchy_df['Subject code'].notnull()) &
    #         (cumulative_hierarchy_df['Category'].isnull())].iloc[:, :4])

    # cumulative_hierarchy_df = cumulative_hierarchy_df.reset_index(drop=True)
    # cumulative_hierarchy_df['Hierarchy sort order'] = (
    #     cumulative_hierarchy_df.index)

    # subject_code_sort_df = cumulative_hierarchy_df.copy()
    # subject_code_sort_df = subject_code_sort_df[[
    #     'Subject code', 'Hierarchy sort order']]
    # subject_code_sort_df = subject_code_sort_df.rename(
    #     columns={'Hierarchy sort order': 'Subject sort order'})

    # # Add the subject code sort order to the formulas file
    # cumulative_df = formulas_df.copy()
    # cumulative_df = pd.merge(
    #     left=cumulative_df, right=subject_code_sort_df,
    #     left_on=['Subject code'], right_on=['Subject code'],
    #     how='left')
    # cumulative_df = cumulative_df.drop(labels=['Subject code'], axis=1)

    # # Merge with the heriarchy_df and filter where sort order per
    # # hierarchy_df >= subject sort order
    # cumulative_df = pd.merge(left=cumulative_hierarchy_df,
    #                          right=cumulative_df, left_on=['State'],
    #                          right_on=['State'], how='left')
    # cumulative_df = cumulative_df[cumulative_df['Hierarchy sort order']
    #                               >= cumulative_df['Subject sort order']]
    # cumulative_df = cumulative_df.drop(labels=[
    #     'Hierarchy sort order', 'Subject sort order'
    # ], axis=1)
    # cumulative_df = cumulative_df.reset_index()

    # return cumulative_df
