"""Module for generating formula related markdown files to be utilised for Hugo
site generation.
"""

import pandas as pd
from IPython.display import Math
import utilities


def get_formulas_df(formulas_input_df, syllabus_df, sort_orders_df):
    """Merges formulas_input_df with syllabus_df.
    Returns a combined pandas dataframe from formulus_input_df
    containging formulas by year (subject code) as well as cumululative
    formulas by year (subject code) based on sort_orders_df
    """
    input_copy_df = formulas_input_df.copy()
    input_copy_df = pd.merge(
        left=syllabus_df, right=input_copy_df,
        left_on=['State', 'Subject code', 'Syllabus subtopic code'],
        right_on=['State', 'Subject code', 'Syllabus subtopic code'],
        how='right')
    by_year_df = get_formulas_by_year_df(input_copy_df)
    cumulative_df = get_formulas_by_year_cumulative_df(
        input_copy_df, sort_orders_df)
    formulas_df = pd.concat([by_year_df, cumulative_df])
    return formulas_df


def get_formulas_by_topic_df(formulas_input_df, syllabus_df):
    """Makes a copy of formulas_df pandas dataframe and adds
    below field to formulas_df dataframe and returns
    the result:"""
    by_topic_df = formulas_input_df.copy()
    by_topic_df = pd.merge(
        left=syllabus_df, right=by_topic_df,
        left_on=['State', 'Subject code', 'Syllabus subtopic code'],
        right_on=['State', 'Subject code', 'Syllabus subtopic code'],
        how='right')
    by_topic_df['Topic subcategory 1'] = 'Topics'
    return by_topic_df


def create_formulas_content(formulas_df, formula_sheet_items,
                            formula_proof_required_items, sort_orders_df,
                            docs_dir):
    """Creates markdown files containing formula tables as input for static
    web page creation via Hugo
    """
    dirs_df = (
        formulas_df[['State', 'Formula subcategory 1',
                     'Formula subcategory 2',
                     'Subject code']].drop_duplicates())
    file_paths_df = (
        formulas_df[['State', 'Formula subcategory 1',
                     'Formula subcategory 2',
                     'Subject code', 'Category']].drop_duplicates())
    utilities.create_subdirectories_from_df(base_dir=docs_dir,
                                            subpaths_df=dirs_df)
    front_matter_index_files = {'bookCollapseSection': True}
    utilities.create_index_files(base_dir=docs_dir, dirs_df=dirs_df,
                                 front_matter=front_matter_index_files,
                                 sort_orders_df=sort_orders_df)
    utilities.create_files(base_dir=docs_dir, file_paths_df=file_paths_df,
                           file_extension='.md',
                           string_creator=generate_formula_page,
                           sort_orders_df=sort_orders_df,
                           formulas_df=formulas_df,
                           formula_sheet_items=formula_sheet_items,
                           formula_proof_required_items=(
                               formula_proof_required_items),
                           cols_to_highlight=[
                               'Formula'])


def create_calculus_summary_files(formulas_df, formula_sheet_items,
                                  formula_proof_required_items,
                                  sort_orders_df, docs_dir):
    """Creates custom differentiation and integration formulas markdown
    files"""
    calculus_summary_dirs_df = get_calculus_summary_dir_paths_df(
        formulas_df)
    utilities.create_subdirectories_from_df(
        base_dir=docs_dir, subpaths_df=calculus_summary_dirs_df)
    front_matter_index_files = {'bookCollapseSection': True}
    utilities.create_index_files(base_dir=docs_dir,
                                 dirs_df=calculus_summary_dirs_df,
                                 front_matter=front_matter_index_files,
                                 sort_orders_df=sort_orders_df)
    calculus_summary_file_paths_df = get_calculus_summary_file_paths_df(
        calculus_summary_dirs_df)
    utilities.create_files(base_dir=docs_dir,
                           file_paths_df=calculus_summary_file_paths_df,
                           file_extension='.md',
                           string_creator=generate_calculus_page,
                           sort_orders_df=sort_orders_df,
                           formulas_df=formulas_df,
                           formula_sheet_items=formula_sheet_items,
                           formula_proof_required_items=(
                               formula_proof_required_items),
                           cols_to_highlight=[
                               'Derivative', 'Equivalent integral'])


def create_financial_summary(formulas_df, formula_sheet_items,
                             formula_proof_required_items, sort_orders_df,
                             docs_dir):
    """Creates custom financial formulas formulas markdown files"""
    financial_summary_dirs_df = (
        get_financial_summary_dir_paths_df(formulas_df))
    utilities.create_subdirectories_from_df(
        base_dir=docs_dir, subpaths_df=financial_summary_dirs_df)
    front_matter_index_files = {'bookCollapseSection': True}
    utilities.create_index_files(base_dir=docs_dir,
                                 dirs_df=financial_summary_dirs_df,
                                 front_matter=front_matter_index_files,
                                 sort_orders_df=sort_orders_df)
    financial_summary_file_paths_df = (
        get_financial_summary_file_paths_df(financial_summary_dirs_df))
    utilities.create_files(base_dir=docs_dir,
                           file_paths_df=financial_summary_file_paths_df,
                           file_extension='.md',
                           string_creator=create_financial_summary_page,
                           sort_orders_df=sort_orders_df,
                           formulas_df=formulas_df,
                           formula_sheet_items=formula_sheet_items,
                           formula_proof_required_items=formula_proof_required_items,
                           cols_to_highlight=[
                               'Arithmetic sequence', 'Geometric sequence'])


def get_formulas_by_year_df(formulas_df):
    """Makes a copy of formulas_df pandas dataframe and adds
    below 2 fields to formulas_df dataframe and returns
    the result:
         - 'Formula subcategory 1' containing text 'Formulas'
         - 'Formula subcategory 2' containing text 'By Year'"""
    by_year_df = formulas_df.copy()
    by_year_df['Formula subcategory 1'] = 'Formulas'
    by_year_df['Formula subcategory 2'] = 'By Year'
    return by_year_df


def get_formulas_by_year_cumulative_df(formulas_df, sort_orders_df):
    """Makes a copy of formulas_df pandas dataframe and adds
    Adds below 2 fields to formulas_df dataframe and returns
    the result:
         - 'Formula subcategory 1' containing text 'Formulas'
         - 'Formula subcategory 2' containing text
             'By year cumulative'
    The returned dataframe is 'cumulative' based on the Subject code in the
    sort_order_df for example subject code year 11 includes year 9 and
    year 10 formulas etc."""

    cumulative_hierarchy_df = sort_orders_df.copy()
    cumulative_hierarchy_df = cumulative_hierarchy_df.rename(
        columns={'Level_0': 'State', 'Level_1': 'Formula subcategory 1',
                 'Level_2': 'Formula subcategory 2', 'Level_3': 'Subject code',
                 'Level_4': 'Category'})

    cumulative_hierarchy_df = (
        cumulative_hierarchy_df[
            (cumulative_hierarchy_df['Formula subcategory 1'].str.upper() ==
             'FORMULAS') &
            (cumulative_hierarchy_df['Formula subcategory 2'].str.upper() ==
             'BY YEAR CUMULATIVE') &
            (cumulative_hierarchy_df['Subject code'].notnull()) &
            (cumulative_hierarchy_df['Category'].isnull())].iloc[:, :4])

    cumulative_hierarchy_df = cumulative_hierarchy_df.reset_index(drop=True)
    cumulative_hierarchy_df['Hierarchy sort order'] = (
        cumulative_hierarchy_df.index)

    subject_code_sort_df = cumulative_hierarchy_df.copy()
    subject_code_sort_df = subject_code_sort_df[[
        'Subject code', 'Hierarchy sort order']]
    subject_code_sort_df = subject_code_sort_df.rename(
        columns={'Hierarchy sort order': 'Subject sort order'})

    # Add the subject code sort order to the formulas file
    cumulative_df = formulas_df.copy()
    cumulative_df = pd.merge(
        left=cumulative_df, right=subject_code_sort_df,
        left_on=['Subject code'], right_on=['Subject code'],
        how='left')
    cumulative_df = cumulative_df.drop(labels=['Subject code'], axis=1)

    # Merge with the heriarchy_df and filter where sort order per
    # hierarchy_df >= subject sort order
    cumulative_df = pd.merge(left=cumulative_hierarchy_df,
                             right=cumulative_df, left_on=['State'],
                             right_on=['State'], how='left')
    cumulative_df = cumulative_df[cumulative_df['Hierarchy sort order']
                                  >= cumulative_df['Subject sort order']]
    cumulative_df = cumulative_df.drop(labels=[
        'Hierarchy sort order', 'Subject sort order'
    ], axis=1)
    cumulative_df = cumulative_df.reset_index()

    return cumulative_df


def get_calculus_summary_dir_paths_df(formulas_df):
    """Returns a dataframe where each cell rerepresents componenets of the
    directory path for the calculus summary formulas.   The formulas_df input
    is filtered for subject codes with field Category containing both entries
    for differentiation and integration
    """
    calculus_dir_df = formulas_df.copy()
    calculus_dir_df = calculus_dir_df[
        (calculus_dir_df['Category'] == 'Differentiation') |
        (calculus_dir_df['Category'] == 'Integration')
    ]
    calculus_dir_df = calculus_dir_df[
        ['State', 'Category', 'Formula subcategory 1',
         'Formula subcategory 2', 'Subject code']].drop_duplicates()
    calculus_dir_df['counter'] = 1
    calculus_dir_df = pd.pivot_table(
        data=calculus_dir_df, index=['State', 'Formula subcategory 1',
                                     'Formula subcategory 2',
                                     'Subject code'],
        columns=['Category'], values='counter',
        aggfunc=pd.Series.nunique)
    calculus_dir_df = calculus_dir_df.reset_index()
    calculus_dir_df = calculus_dir_df[
        (calculus_dir_df['Differentiation'].notnull()) &
        (calculus_dir_df['Integration'].notnull())]

    calculus_dir_df = calculus_dir_df.drop(
        ['Differentiation', 'Integration'], axis=1)
    calculus_dir_df['Menu type'] = 'Summaries'
    return calculus_dir_df


def get_calculus_summary_file_paths_df(calculus_dir_df):
    """Returns a dataframe where each cell rerepresents componenets of the
    file path for the calculus summary formulas.  The dataframe is obtained
    by adding a filename column to calculus_dir_df"""
    calculus_file_path_df = calculus_dir_df.copy()
    calculus_file_path_df['Filename'] = 'Calculus'
    return calculus_file_path_df


def get_financial_summary_dir_paths_df(formulas_df):
    """Returns a dataframe where each cell rerepresents componenets of the
    directory path for the financial summary formulas.   The formulas_df
    input is filtered for subject codes with field Category containing
    entries for Financial mathematics
    """
    financial_dir_df = formulas_df.copy()
    financial_dir_df = financial_dir_df[
        (financial_dir_df['Category'] == 'Financial mathematics')
    ]
    financial_dir_df = financial_dir_df[
        ['State', 'Formula subcategory 1',
         'Formula subcategory 2', 'Subject code']].drop_duplicates()
    financial_dir_df['Menu type'] = 'Summaries'
    return financial_dir_df


def get_financial_summary_file_paths_df(financial_dir_df):
    """Returns a dataframe where each cell rerepresents componenets of the
    file     path for the financial summary formulas.  The dataframe is
    obtained by adding  a filename column to financial_dir_df
    """
    financial_file_path_df = financial_dir_df.copy()
    financial_file_path_df['Filename'] = 'Financial'
    return financial_file_path_df


def generate_formula_page(formulas_df, state, formula_subcategory_2,
                          subject_code, category, formula_sheet_items,
                          formula_proof_required_items,
                          cols_to_highlight, **kwargs):
    """Filters formulas_df and returns a summmary formula string table in
    markdown format with embedded html. Generates seperate tabs to
    highlight items on formula sheet or formula proofs if there are any."""

    # ***kwargs are utilised to ignore any excess paramaters passed by
    # wrapper function to generate files
    _ = kwargs

    formulas_df = formulas_df[(
        (formulas_df['State'] == state) &
        (formulas_df['Formula subcategory 2'] == formula_subcategory_2) &
        (formulas_df['Subject code'] == subject_code) &
        (formulas_df['Category'] == category))]
    formulas_df = formulas_df[['Formula']]
    formula_string = generate_formula_string(formulas_df,
                                             formula_sheet_items,
                                             formula_proof_required_items,
                                             cols_to_highlight)
    return formula_string


def generate_formula_string(formulas_df, formula_sheet_items,
                            formula_proof_required_items,
                            cols_to_highlight):
    """Returns a summmary formula string table in markdown format with
    embedded html. Generates seperate tabs to highlight items on
    formula sheet or formula proofs if there are any."""

    standard_display = df_to_formula_styled_table(
        input_df=formulas_df, col_widths={'Formula': 400},
        display_col_headers=False, display_row_headers=False
    ).to_html()

    some_formulas_are_on_formula_sheet = (
        utilities.series_intersect(formulas_df['Formula'],
                                   formula_sheet_items))
    some_formulas_require_proofs = (
        utilities.series_intersect(formulas_df['Formula'],
                                   formula_proof_required_items))
    tabs_required = (some_formulas_are_on_formula_sheet or
                     some_formulas_require_proofs)

    if not tabs_required:
        output_string = standard_display
    else:
        output_string = (
            '{{< tabs "uniqueid" >}}\n\n' +
            '{{< tab "Standard view" >}}\n\n' +
            standard_display + '{{< /tab >}}')

        if some_formulas_are_on_formula_sheet:
            output_string += '\n\n' + '{{< tab "Formula sheet" >}}'
            output_string += 'Items on formula sheet are highlighted'
            output_string += '\n<br>\n'
            output_string += df_to_formula_styled_table(
                input_df=formulas_df, col_widths={'Formula': 400},
                cols_to_highlight=(
                    cols_to_highlight),
                formula_sheet_items=formula_sheet_items,
                display_col_headers=False,
                display_row_headers=False).to_html()
            output_string += '{{< /tab >}}'

        if some_formulas_require_proofs:
            output_string += '\n\n' + '{{< tab "Proofs required" >}}'
            output_string += 'Items where proofs are required are highlighted'
            output_string += '\n<br>\n'
            output_string += df_to_formula_styled_table(
                input_df=formulas_df, col_widths={'Formula': 400},
                cols_to_highlight=(
                    cols_to_highlight),
                formula_proof_required_items=formula_proof_required_items,
                display_col_headers=False,
                display_row_headers=False).to_html()
            output_string += '{{< /tab >}}'
        output_string += '\n{{< /tabs >}}'

    return output_string


def generate_calculus_page(formulas_df, state,
                           formula_subcategory_2, subject_code,
                           formula_sheet_items,
                           formula_proof_required_items,
                           cols_to_highlight, **kwargs):
    """Filters formulas_df and returns a summmary calculus string table in
    markdown format with embedded html. Generates seperate tabs to
    highlight items on formula sheet or formula proofs if there are any.
    """

    # kwargs are utilised to ignore any excess paramaters passed by
    # wrapper function to generate files
    _ = kwargs

    formulas_df = formulas_df[(
        (formulas_df['State'] == state) &
        (formulas_df['Formula subcategory 2'] == formula_subcategory_2) &
        (formulas_df['Subject code'] == subject_code))]
    calculus_df = get_calculus_summary_df(formulas_df)
    calculus_string = generate_calculus_summary_string(calculus_df,
                                                       formula_sheet_items,
                                                       formula_proof_required_items,
                                                       cols_to_highlight)
    return calculus_string


def generate_calculus_summary_string(calculus_df, formula_sheet_items,
                                     formula_proof_required_items,
                                     cols_to_highlight):
    """Returns a summmary calculus string table in markdown format with
    embedded html. Generates seperate tabs to highlight items on
    formula sheet or formula proofs if there are any."""

    standard_display = df_to_formula_styled_table(
        input_df=calculus_df,
        col_widths={'Derivative': 400, 'Equivalent integral': 400,
                    'Comment': 600}
    ).to_html()

    calculus_formulas = pd.concat(
        [calculus_df['Derivative'], calculus_df['Equivalent integral']])

    some_formulas_are_on_formula_sheet = (
        utilities.series_intersect(calculus_formulas,
                                   formula_sheet_items))
    some_formulas_require_proofs = (
        utilities.series_intersect(calculus_formulas,
                                   formula_proof_required_items))
    tabs_required = (some_formulas_are_on_formula_sheet or
                     some_formulas_require_proofs)

    if not tabs_required:
        output_string = standard_display
    else:
        output_string = (
            '{{< tabs "uniqueid" >}}\n\n' +
            '{{< tab "Standard view" >}}' + '\n' +
            standard_display + '{{< /tab >}}')
        if some_formulas_are_on_formula_sheet:
            output_string += '\n\n' + '{{< tab "Formula sheet" >}}'
            output_string += 'Items on formula sheet are highlighted'
            output_string += '\n<br><br>'
            output_string += df_to_formula_styled_table(
                input_df=calculus_df, col_widths={'Derivative': 400,
                                                  'Equivalent integral': 400,
                                                  'Comment': 600},
                cols_to_highlight=cols_to_highlight,
                formula_sheet_items=formula_sheet_items
            ).to_html()
            output_string += '{{< /tab >}}'
        if some_formulas_require_proofs:
            output_string += '\n\n' + '{{< tab "Proofs required" >}}'
            output_string += 'Items where proofs are required are highlighted'
            output_string += '\n<br>\n'
            output_string += df_to_formula_styled_table(
                input_df=calculus_df, col_widths={'Derivative': 400,
                                                  'Equivalent integral': 400,
                                                  'Comment': 600},
                cols_to_highlight=cols_to_highlight,
                formula_proof_required_items=formula_proof_required_items
            ).to_html()
            output_string += '{{< /tab >}}'

        output_string += '\n{{< /tabs >}}'

    return output_string


def create_financial_summary_page(formulas_df, state,
                                  formula_subcategory_2, subject_code,
                                  formula_sheet_items,
                                  formula_proof_required_items,
                                  cols_to_highlight,
                                  **kwargs):
    """Filters formulas_df and returns a summmary financial maths string table
    in markdown format with embedded html. Generates seperate tabs to
    highlight items on formula sheet or formula proofs if there are any.
    """

    # kwargs are utilised to ignore any excess paramaters passed by
    # wrapper function to generate files
    _ = kwargs

    formulas_df = formulas_df[(
        (formulas_df['State'] == state) &
        (formulas_df['Formula subcategory 2'] == formula_subcategory_2) &
        (formulas_df['Subject code'] == subject_code))]
    financial_df = get_financial_summary_df(formulas_df)
    return create_financial_summary_string(
        formula_sheet_items, formula_proof_required_items,
        cols_to_highlight, financial_df)


def create_financial_summary_string(formula_sheet_items,
                                    formula_proof_required_items,
                                    cols_to_highlight, financial_df):
    """Returns a summmary calculus string table in markdown format with
    embedded html. Generates seperate tabs to highlight items on
    formula sheet or formula proofs if there are any.

    Args:
        formula_sheet_items (pandas serie): formulas that appear on formula
            sheet
        formula_proof_required_items (pandas series): formulas requiring proof
        cols_to_highlight (list): _column names to highlight when on formula
            sheet or if proof is required
        financial_df (dataframe): Financial maths formulas

    Returns:
        string: String in markdown format representing financial maths summary
        formulas for purpose of Hugo web page generation.
    """
    financial_formulas = pd.concat([financial_df['Arithmetic sequence'],
                                    financial_df['Geometric sequence']])
    standard_display = df_to_formula_styled_table(
        input_df=financial_df,
        col_widths={'Arithmetic sequence': 400,
                    'Geometric sequence': 400}
    ).to_html()

    some_formulas_are_on_formula_sheet = (
        utilities.series_intersect(financial_formulas,
                                   formula_sheet_items))
    some_formulas_require_proofs = (
        utilities.series_intersect(financial_formulas,
                                   formula_proof_required_items))
    tabs_required = (some_formulas_are_on_formula_sheet or
                     some_formulas_require_proofs)

    if tabs_required:
        output_string = (
            '{{< tabs "uniqueid" >}}\n\n' +
            '{{< tab "Standard view" >}}\n' +
            standard_display + '{{< /tab >}}')
        if some_formulas_are_on_formula_sheet:
            output_string += '\n\n' + '{{< tab "Formula sheet" >}}'
            output_string += 'Items on formula sheet are highlighted'
            output_string += '\n<br><br>'
            output_string += df_to_formula_styled_table(
                input_df=financial_df, col_widths={'Arithmetic sequence': 400,
                                                   'Geometric sequence': 400},
                cols_to_highlight=cols_to_highlight,
                formula_sheet_items=formula_sheet_items
            ).to_html()
            output_string += '{{< /tab >}}'
        if some_formulas_require_proofs:
            output_string += '\n\n' + '{{< tab "Proofs required" >}}'
            output_string += 'Items where proofs are required are highlighted'
            output_string += '\n<br>\n'
            output_string += df_to_formula_styled_table(
                input_df=financial_df, col_widths={'Arithmetic sequence': 400,
                                                   'Geometric sequence': 400},
                cols_to_highlight=cols_to_highlight,
                formula_proof_required_items=formula_proof_required_items
            ).to_html()
            output_string += '{{< /tab >}}'

        output_string += '\n{{< /tabs >}}'

    return output_string


def generate_definition_string():
    """TBA"""
    return 'These are the definitions'


def get_calculus_summary_df(formulas_df):
    """Returns a summary of derivative and integral formulas

    Args:
        formulas_df (pandas dataframe): The source of fomulas for producing the
        summary

    Returns:
        pandas dataframe: Summary of calculus and equicalent integraml
        formulas.Returns None if no derivative of integration formulas
        exists in formulas_input_df
    """
    calculus_df = (formulas_df
                   [['Category', 'Group', 'Formula', 'Comment']]
                   [formulas_df["Category"].isin(["Differentiation", "Integration"])])
    if len(calculus_df.index) == 0:
        return None
    calculus_df = calculus_df.pivot(
        columns='Category', index='Group').fillna('')

    # Flatten the multi-index headings after pivot
    calculus_df.columns = (
        calculus_df.columns.get_level_values(0) + ' ' +
        calculus_df.columns.get_level_values(1))
    calculus_df = calculus_df.reset_index()

    calculus_df['Comment'] = (
        calculus_df.apply(_calclus_summary_comment, axis=1))

    calculus_df = calculus_df.sort_values(by='Group')
    calculus_df = calculus_df.drop(
        labels=['Group', 'Comment Differentiation', 'Comment Integration'],
        axis=1)
    calculus_df = calculus_df.rename(columns={
        "Formula Differentiation": "Derivative",
        "Formula Integration": "Equivalent integral"})

    # Reorder columns
    calculus_df = calculus_df[['Derivative', 'Equivalent integral',
                               'Comment']]
    return calculus_df


def _calclus_summary_comment(row):
    """Returns a comment for calculus formula summary based on
    derivative and integral comments
    """
    if row['Comment Differentiation'] == row['Comment Integration']:
        return_value = row['Comment Differentiation']
    elif row['Comment Differentiation'] == '':
        return_value = row['Comment Integration']
    elif row['Comment Integration'] == '':
        return_value = row['Comment Differentiation']
    else:
        return_value = (row['Comment Differentiation'] + '\n' +
                        row['Comment Integration'])
    return return_value


def get_financial_summary_df(formulas_input_df):
    """Returns a summary of financial mathematic formulas displayed by
    arithmetic vs geometric sequence

    Args:
        formulas_df (pandas dataframe): The source of fomulas for producing the
        summary

    Returns:
        pandas dataframe: Summary of financial maths formula
                          Returns None if no financial formulas exists in
                          formulas_input_df
    """
    financial_df = (formulas_input_df[
        (formulas_input_df['Category'] == 'Financial mathematics') &
        (formulas_input_df['State'] == 'NSW') &
        (
            (formulas_input_df['Subcategory_1'] == 'Arithmetic sequence') |
            (formulas_input_df['Subcategory_1'] == 'Geometric sequence')
        )
    ])
    if len(financial_df.index) == 0:
        return None

    financial_df = financial_df[['Subcategory_1', 'Subcategory_2', 'Formula']]
    financial_df['temp_aggregator'] = 1
    financial_df = pd.pivot_table(data=financial_df, values='Formula',
                                  columns='Subcategory_1',
                                  index='Subcategory_2', aggfunc=lambda x: x)
    financial_df.index.name = None
    financial_df.columns.name = None

    # Convert index to categorical data to enable custom sort order
    financial_df.index = pd.Categorical(
        financial_df.index,
        ['Recursive definition', 'n-th term', 'Sum of first n terms',
         'Limiting sum'])
    financial_df = financial_df.sort_index()
    return financial_df


def set_styled_table_widths(styled_table, widths):
    """Sets pandas dataframe stlyle column withs where widths is represents a
    dict of column names and widths in pixels as integers.  Ignores column
    names that do not exist.  Purpously does not generate an error to allow
    the function to be called for a broader set of column names without
    requiring a check in the calling sub"""
    return_table = styled_table
    for column_name, width in widths.items():
        if column_name in styled_table.columns:
            return_table = return_table.set_properties(
                subset=[column_name], **{'width': str(width) + 'px'})
    return return_table


def df_to_formula_styled_table(input_df, col_widths=None,
                               cols_to_highlight=None,
                               formula_sheet_items=pd.Series(dtype="string"),
                               formula_proof_required_items=(
                                   pd.Series(dtype="string")),
                               display_col_headers=True,
                               display_row_headers=True):
    """Converts pandas dataframe to a styler and applies various formatting
    Note that index of df needs to be unique"""

    if col_widths is None:
        col_widths = {}
    if cols_to_highlight is None:
        cols_to_highlight = []

    styled_table = input_df.fillna('').style
    styled_table = set_styled_table_widths(styled_table, col_widths)

    if not display_col_headers:
        styled_table = styled_table.hide(axis='columns')
    if not display_row_headers:
        styled_table = styled_table.hide(axis='index')

    # Calculate intersect with df columns to avoid error if cols not in df
    cols_to_highlight = list(set(cols_to_highlight)
                             & set(list(input_df.columns)))
    if not formula_sheet_items.empty:
        for col in cols_to_highlight:
            styled_table = styled_table.applymap(
                is_on_formula_sheet_formatting,
                subset=[col],
                formula_sheet_items=formula_sheet_items)
    if not formula_proof_required_items.empty:
        for col in cols_to_highlight:
            styled_table = styled_table.applymap(
                is_on_formula_proof_required_formatting,
                subset=[col],
                formula_proof_required_items=formula_proof_required_items)

    styled_table = styled_table.set_table_styles([
        {'selector': 'th.col_heading', 'props':
         'text-align: left; font-size:1em;'},
        {'selector': 'td',
         'props': 'text-align: left; font-size:1em;padding: 1.5em;'}])

    # below allows newlines in the csv, outside of the latex dollar signs to
    # be reflected on display
    styled_table = styled_table.set_properties(**{'white-space': 'pre-wrap'})

    return styled_table


def get_formulas_on_formula_sheet(formulas_df):
    """Returns a pandas series of formulas on formula sheet that returns all
    fields Formula of the dataframe df where field 'On formula sheet'
    field is True"""
    formulas_on_sheet = (formulas_df[
        (formulas_df['On formula sheet']) &
        (formulas_df['Formula'].notnull())
    ]
        ['Formula'].drop_duplicates())
    return formulas_on_sheet


def get_formulas_where_proofs_required(formulas_df):
    """Returns a pandas series of formulas where proof is required where
    fields Formula of the dataframe df where field 'Proof required'
    field is True"""
    return_value = (formulas_df[
        (formulas_df['Proof required']) &
        (formulas_df['Formula'].notnull())
    ]
        ['Formula'].drop_duplicates())
    return return_value


def is_on_formula_sheet_formatting(formula, formula_sheet_items):
    """Returns formatting for pandas styler object based on whether formulas
    is contained in formula_sheet_items (pandas series)"""
    if formula in formula_sheet_items.values:
        return 'background-color:rgba(255,194,10, 0.2);'
    else:
        return None


def is_on_formula_proof_required_formatting(formula,
                                            formula_proof_required_items):
    """Returns formatting for pandas styler object based on whether formulas
    is contained in formula_sheet_items (pandas series)
    """
    if formula in formula_proof_required_items.values:
        return 'background-color:rgba(0,150,200, 0.2);'
    else:
        return None


def get_single_formula(formulas_df, category, description):
    """Returns value in column Formula of data frame formulas_df
    where category and descriptiom match the corresponding columns in the
    data frame
    """
    filtered_df = formulas_df.copy()[(
        (formulas_df['Category'] == category) &
        (formulas_df['Description'] == description))]
    filtered_array = filtered_df['Formula'].unique()
    if len(filtered_array) == 0:
        return_value = 'No matching formula'
    elif len(filtered_array) > 1:
        return_value = 'multiple matching formulas'
    else:
        return_value = Math(filtered_array[0])
    return return_value
