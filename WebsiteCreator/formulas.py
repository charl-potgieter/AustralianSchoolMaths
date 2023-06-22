import pandas as pd
import numpy as np
import os
import shutil
from IPython.display import Markdown, clear_output



def get_formulas_by_year_df(filepath):
    """Reads dataframe from csv at filepath   Returns a dataframe summary 
    containing below columns in order:
         - 'State'
         - new column 'Formula sub category 1' containing text 'Formulas'
         - new column 'Formula sub category 2' containing text 'By Year'
         - 'Subject code'
         - 'Category'
         - 'Formula_1'
         - 'Formula_2"""

    df = pd.read_csv(filepath)
    df = (
        df[['State', 'Subject code', 'Category', 'Formula_1', 'Formula_2']])
    df['Formula sub category 1'] = 'Formulas'
    df['Formula sub category 2'] = 'By Year'
    df = (df[['State', 'Formula sub category 1', 'Formula sub category 2', 
                            'Subject code', 'Category', 'Formula_1', 'Formula_2']])
    return(df)


def get_formulas_by_year_cumulative_df(formula_file_path, 
                                           order_file_path):
    """Reads dataframe from csv at formula_filepath and order_file_path.
    Returns a dataframe summary containing below columns in order:
         - 'State'
         - new column 'Formula sub category 1' containing text 'Formulas'
         - new column 'Formula sub category 2' containing text 
             'By year cumulative'
         - 'Subject code'
         - 'Category'
         - 'Formula_1'
         - 'Formula_2
    The returned dataframe is 'cumulative' based on the Subject code in the 
    psort order file for examp;e subject code year 11 includes year 9 and 
    year 10 formulas etc."""

    formulas_df = pd.read_csv(formula_file_path)
    sort_orders_df = pd.read_csv(order_file_path)
    
    cumulative_hierarchy_df = sort_orders_df.copy()
    cumulative_hierarchy_df = cumulative_hierarchy_df.rename(
        columns={'Level_0':'State', 'Level_1':'Formula sub category 1',
                 'Level_2':'Formula sub category 2', 'Level_3':'Subject code',
                 'Level_4':'Category'})
    
    cumulative_hierarchy_df = (
        cumulative_hierarchy_df[
            (cumulative_hierarchy_df['Formula sub category 2'].str.upper() ==
             'BY YEAR CUMULATIVE') &
            (cumulative_hierarchy_df['Subject code'].notnull()) &
              (cumulative_hierarchy_df['Category'].isnull())].iloc[:, :4])
    
    cumulative_hierarchy_df = cumulative_hierarchy_df.reset_index(drop = True)
    cumulative_hierarchy_df['Hierarchy sort order'] = (
        cumulative_hierarchy_df.index)
    
    subject_code_sort_df = cumulative_hierarchy_df.copy()
    subject_code_sort_df = (subject_code_sort_df
        [['Subject code', 'Hierarchy sort order']])
    subject_code_sort_df = subject_code_sort_df.rename(columns=
        {'Hierarchy sort order': 'Subject sort order'})

    # Add the subject code sort order to the formulas file
    formulas_df = pd.merge(
        left = formulas_df, right = subject_code_sort_df, 
        left_on = ['Subject code'], right_on = ['Subject code'], 
        how = 'left')
    formulas_df = formulas_df.drop(labels = ['Subject code'], axis=1)

    # Merge with the heriarchy_df and filter where sort order per 
    # hierarchy_df >= subject sort order
    formulas_df = pd.merge(left = cumulative_hierarchy_df, 
                           right = formulas_df, left_on = ['State'], 
                           right_on = ['State'], how = 'left')
    
    formulas_df = (formulas_df[
                   formulas_df['Hierarchy sort order'] >= 
                   formulas_df['Subject sort order']])
    formulas_df = formulas_df.drop(
        labels = ['Hierarchy sort order', 'Subject sort order'], axis=1)

    formulas_df = (formulas_df[
                   ['State', 'Formula sub category 1', 
                    'Formula sub category 2', 'Subject code', 'Category', 
                    'Formula_1', 'Formula_2']])

    return(formulas_df)


def get_formula_display_string(input_series, **kwarg):
    """Returns a summmary formula table in markdown format with embedded
    html.  Input series is a pandas series with Indices State, Subec code
    and category.  **Kwarg must be called with parameter  = df_formulas
    where df_Formulas contains fields State, Subject code, Category, 
    Formula_1, Formula_2"""
    
    df_formulas = kwarg['df_formulas']
    df = df_formulas[(
        (df_formulas['State'] == str(input_series['State'])) &
        (df_formulas['Formula sub category 2'] == str(input_series['Formula sub category 2'])) &
        (df_formulas['Subject code'] == str(input_series['Subject code'])) & 
        (df_formulas['Category'] == str(input_series['Category'])))]
        
    
    formula_2_col_is_empty = df['Formula_2'].dropna().empty    
    if formula_2_col_is_empty:
        df = df[['Formula_1']]
    else:
        df = df[['Formula_1', 'Formula_2']]
    
    formula_set_styler = (df_to_formula_styled_table(
        df=df, col_widths={'Formula_1':300, 'Formula_2':400},
        display_col_headers = False))
    output_string =  '#  \n<br>\n' + formula_set_styler.to_html()
    return(output_string)

    

        

def df_calculus_summary(df_formulas):
    """Returns a summary of derivative and integral formulasas a pandas dataframe"""
    
    df_calculus = df_formulas[['Category', 'Group', 'Formula_1', 'Formula_2', 'Comment']][df_formulas["Category"].isin(["Differentiation","Integration"])]
    df_calculus = df_calculus.pivot(columns='Category', index = 'Group').fillna('')
    
    # Flatten the multi-index headings after pivot
    df_calculus.columns = df_calculus.columns.get_level_values(0) +' ' + df_calculus.columns.get_level_values(1)
    df_calculus = df_calculus.reset_index()

    df_calculus['Comment'] = df_calculus.apply(_calclus_summary_comment, axis=1)
    
    df_calculus = df_calculus.sort_values(by='Group')
    df_calculus =  df_calculus.drop(labels = ['Group', 'Comment Differentiation', 'Comment Integration', 'Formula_2 Integration'], axis = 1)
    df_calculus = df_calculus.rename(columns={
        "Formula_1 Differentiation": "Function", 
        "Formula_1 Integration":"Equivalent integral",
        "Formula_2 Differentiation": "Derivative"})

    # Reorder columns
    df_calculus = df_calculus[['Function', 'Derivative', 'Equivalent integral', 'Comment']]

    return(df_calculus)


def styler_calculus_summary(df_calculus, formula_sheet_list=[]):
    """Returns a pandas styler version of the df_calculus dataframe as returned by df_calculus_summary function"""

    if len(formula_sheet_list):
        styler_calculus = df_to_formula_styled_table(df=df_calculus, 
                                                     col_widths={'Function': 200, 'Derivative': 300,'Equivalent integral': 400,'Comment':600},
                                                     cols_to_highlight_if_in_formula_sheet= {'Derivative', 'Equivalent integral'},
                                                     formula_sheet_list=formula_sheet_list)
    else:
        styler_calculus = df_to_formula_styled_table(df=df_calculus, 
                                                     col_widths={'Function': 200, 'Derivative': 300,'Equivalent integral': 400,'Comment':600})
    
    return(styler_calculus)


def _calclus_summary_comment(row):
    """Returns a comment for calculus formula summary based on derivative and integral comments"""
    if row['Comment Differentiation'] == row['Comment Integration']:
        return_value = row['Comment Differentiation']
    elif row['Comment Differentiation'] == '':
        return_value = row['Comment Integration']
    elif row['Comment Integration'] == '':
        return_value = row['Comment Differentiation']            
    else:
        return_value = row['Comment Differentiation'] + '\n' + row['Comment Integration']
    return(return_value)


def set_styled_table_widths(styled_table, widths):
    """Sets pandas dataframe stlyle column withs where widths is represents a dict of column names and widths in pixels as integers
    Ignores column names that do not exist.  Purpously does not generate an error to allow the function to be called for a 
    broader set of column names without requiring a check in the calling sub"""
    return_table = styled_table
    for column_name, width in widths.items():
        if column_name in styled_table.columns:
            return_table = return_table.set_properties(subset=[column_name], **{'width': str(width) + 'px'})
    return(return_table)


def df_to_formula_styled_table(df, col_widths={}, cols_to_highlight_if_in_formula_sheet=[], formula_sheet_list=[], display_col_headers = True):
    """Converts pandas dataframe to a styler and applies various formatting"""

    # Index needs to be unique for to enable apply map to be used on styler
    df = df.reset_index(drop = True)
    
    styled_table = df.fillna('').style
    styled_table = set_styled_table_widths(styled_table, col_widths)

    if not display_col_headers:
        styled_table = styled_table.hide().hide(axis='columns')


    # Calculate intersect with df columns to avoid error if cols not in df
    cols_to_highlght = list(set(cols_to_highlight_if_in_formula_sheet) & set(list(df.columns)))
    
    for col in cols_to_highlght:
        styled_table = styled_table.applymap(
            is_on_formula_sheet_formatting, 
            subset=[col], 
            formula_sheet_list=formula_sheet_list) 
    
    styled_table = styled_table.set_table_styles ([
        {'selector': 'th.col_heading', 'props': 'text-align: left; font-size:1em;'},
        {'selector': 'td', 'props': 'text-align: left; font-size:1em;padding: 1.5em;'}]) 

    # below allows newlines in the csv, outside of the latex dollar signs to be reflected on display
    styled_table= styled_table.set_properties(**{'white-space': 'pre-wrap'})
    
    return (styled_table)


def get_formulas_on_formula_sheet(file_path):
    """Reads csv at file path into a pandas dataframe.  Returns a list of 
    formulas on formula sheet that returns all fields Formula_1 and Formula_2 
    of the dataframe where field 'On formula sheet' field is True"""

    df = pd.read_csv(file_path)
    formulas_one_on_sheet = (df[
                             (df['On formula sheet'] == True) & 
                             (df['Formula_1'].notnull())
                             ]
                             ['Formula_1'].unique().tolist()) 
    formulas_two_on_sheet = (df[
                             (df['On formula sheet'] == True) & 
                             (df['Formula_2'].notnull())
                             ]
                             ['Formula_2'].unique().tolist())
    
    formulas_on_sheet = formulas_one_on_sheet + formulas_two_on_sheet
    return (formulas_on_sheet)


def is_on_formula_sheet_formatting(formula, formula_sheet_list):
    """Returns formatting for pandas styler object based on whether formulas is contained in formula_sheet list"""
    if formula in formula_sheet_list:
        return ('background-color:rgba(255,194,10, 0.2);')
    else:
        return (None)



