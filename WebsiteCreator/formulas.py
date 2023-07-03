import pandas as pd
import numpy as np
import os
import shutil
from IPython.display import Markdown, clear_output, Math

def get_formulas_by_year_df(formulas_df):
    """Makes a copy of formulas_df pandas dataframe and adds
    below 2 fields to formulas_df dataframe and returns
    the result:
         - 'Formula sub category 1' containing text 'Formulas'
         - 'Formula sub category 2' containing text 'By Year'"""

    df = formulas_df.copy()
    df['Formula sub category 1'] = 'Formulas'
    df['Formula sub category 2'] = 'By Year'
    return(df)


def get_formulas_by_year_cumulative_df(formulas_df, 
                                       sort_orders_df):
    """Makes a copy of formulas_df pandas dataframe and adds
    Adds below 2 fields to formulas_df dataframe and returns
    the result:
         - 'Formula sub category 1' containing text 'Formulas'
         - 'Formula sub category 2' containing text 
             'By year cumulative'
    The returned dataframe is 'cumulative' based on the Subject code in the 
    sort_order_df for example subject code year 11 includes year 9 and 
    year 10 formulas etc."""

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
    df = formulas_df.copy()
    df = pd.merge(
        left = df, right = subject_code_sort_df, 
        left_on = ['Subject code'], right_on = ['Subject code'], 
        how = 'left')
    df = df.drop(labels = ['Subject code'], axis=1)

    # Merge with the heriarchy_df and filter where sort order per 
    # hierarchy_df >= subject sort order
    df = pd.merge(left = cumulative_hierarchy_df, 
                           right = df, left_on = ['State'], 
                           right_on = ['State'], how = 'left')
    
    df = (df[
                   df['Hierarchy sort order'] >= 
                   df['Subject sort order']])
    df = df.drop(
        labels = ['Hierarchy sort order', 'Subject sort order'], axis=1)
    df = df.reset_index()

    return(df)


def formulas_contain_items_on_formula_sheet(formulas, formula_sheet_list):
    """Returns true if there are one or more items in formulas that 
    are contained in  formula_sheet_list"""
    if formulas is None or formula_sheet_list is None:
        return (False)
    else:
        formulas_ex_null = formulas.loc[lambda x: x.notnull()]
        return(len(
            (set(formulas_ex_null) & set(formula_sheet_list))
            )>0)


def get_calculus_summary_dir_paths_df(formulas_df):
    """Returns a dataframe where each cell rerepresents componenets of the directory 
    path for the calculus summary formulas.   The formulas_df input is 
    filtered for subject codes with field Category containing both entries
    for differentiation and integration
    """
    calculus_dir_df = formulas_df.copy()
    
    calculus_dir_df = calculus_dir_df[
        (calculus_dir_df['Category'] == 'Differentiation') |
        (calculus_dir_df['Category'] == 'Integration')
    ]
    
    calculus_dir_df =  calculus_dir_df[
        ['State', 'Category', 'Formula sub category 1', 
        'Formula sub category 2', 'Subject code']].drop_duplicates()
    
    calculus_dir_df['counter'] = 1
    
    calculus_dir_df = pd.pivot_table(
        data=calculus_dir_df, index = ['State', 'Formula sub category 1', 'Formula sub category 2', 
                                           'Subject code'], 
        columns = ['Category'], values='counter',  
        aggfunc=pd.Series.nunique)
    calculus_dir_df = calculus_dir_df.reset_index()
    calculus_dir_df =  calculus_dir_df[
        (calculus_dir_df['Differentiation'].notnull()) & 
        (calculus_dir_df['Integration'].notnull())]

    calculus_dir_df = calculus_dir_df.drop(
        ['Differentiation', 'Integration'], axis=1)
    calculus_dir_df['Type'] = 'Summaries'
    
    return(calculus_dir_df)


def get_calculus_summary_file_paths_df(calculus_dir_df):
    """Returns a dataframe where each cell rerepresents componenets of the file 
    path for the calculus summary formulas.  The dataframe is obtained by adding 
    a filename column to calculus_dir_df
    """
    calculus_file_path_df = calculus_dir_df.copy()
    calculus_file_path_df['Filename'] = 'Calculus'
    return(calculus_file_path_df)


def get_financial_summary_dir_paths_df(formulas_df):
    """Returns a dataframe where each cell rerepresents componenets of the directory 
    path for the financial summary formulas.   The formulas_df input is 
    filtered for subject codes with field Category containing entries for Financial 
    mathematics"""
    financial_dir_df = formulas_df.copy()
    
    financial_dir_df = financial_dir_df[
        (financial_dir_df['Category'] == 'Financial mathematics')
    ]    
    financial_dir_df =  financial_dir_df[
        ['State', 'Formula sub category 1', 
        'Formula sub category 2', 'Subject code']].drop_duplicates()
    financial_dir_df['Type'] = 'Summaries'
    return(financial_dir_df)


def get_financial_summary_file_paths_df(financial_dir_df):
    """Returns a dataframe where each cell rerepresents componenets of the file 
    path for the financial summary formulas.  The dataframe is obtained by adding 
    a filename column to financial_dir_df
    """
    financial_file_path_df = financial_dir_df.copy()
    financial_file_path_df['Filename'] = 'Financial'
    return(financial_file_path_df)


def get_formula_display_string(input_series, **kwarg):
    """Returns a summmary formula table in markdown format with embedded
    html.  Input series is a pandas series with Indices State, Subect code
    and category.  **Kwarg must be called with parameter  = formulas_df
    where formulas_df contains fields State, Subject code, Category, 
    Formula_1, Formula_2.  Generates seperate tabs to highlight items on
    formula sheet if there are any"""
    
    df = kwarg['formulas_df'].copy()
    df = df[(
        (df['State'] == str(input_series['State'])) &
        (df['Formula sub category 2'] == str(
            input_series['Formula sub category 2'])) &
        (df['Subject code'] == str(input_series['Subject code'])) & 
        (df['Category'] == str(input_series['Category'])))]

    formula_1_and_2 = pd.concat([df['Formula_1'], df['Formula_2']])
    formula_sheet_list =kwarg.get('formula_sheet_list')
    
    formula_2_col_is_empty = df['Formula_2'].dropna().empty    
    if formula_2_col_is_empty:
        df = df[['Formula_1']]
    else:
        df = df[['Formula_1', 'Formula_2']]

    output_string='#  \n<br>\n'
                      
    output_string+=(df_to_formula_styled_table(
        df=df, col_widths={'Formula_1':300, 'Formula_2':400},
        display_col_headers = False, display_row_headers = False)).to_html()

    if formulas_contain_items_on_formula_sheet(
        formula_1_and_2, formula_sheet_list):

        output_string = (
            '{{< tabs "uniqueid" >}}\n\n' + 
            '{{< tab "Standard view" >}}\n\n' + 
            output_string + '{{< /tab >}}')
                         
        output_string+='\n\n' + '{{< tab "Formula sheet" >}}'

        output_string+='Items on formula sheet are highlighted'
        output_string+='#  \n<br>\n'
            
        cols_to_highlight_if_in_formula_sheet = (
            kwarg.get('cols_to_highlight_if_in_formula_sheet'))
        
        output_string+=(df_to_formula_styled_table(
            df=df, col_widths={'Formula_1':300, 'Formula_2':400},
            cols_to_highlight_if_in_formula_sheet = (
                cols_to_highlight_if_in_formula_sheet),
            formula_sheet_list = formula_sheet_list,
            display_col_headers = False, display_row_headers = False)).to_html()

        output_string+='{{< /tab >}}\n{{< /tabs >}}'
                      
    return(output_string)
    

def get_calculus_summary_display_string(input_series, **kwarg):
    """Returns a calculus summmary formula table in markdown format with 
    embedded html.  Input series is a pandas series with Indices State, 
    Subect code and category.  **Kwarg must be called with 
    parameter  = formulas_df where formulas_df contains fields State, 
    Subject code, Category, Formula_1, Formula_2.  Generates seperate tabs 
    to highlight items on formula sheet if there are any"""
    
    df = kwarg['formulas_df'].copy()
    df = df[(
        (df['State'] == str(input_series['State'])) &
        (df['Formula sub category 2'] == str(
            input_series['Formula sub category 2'])) &
        (df['Subject code'] == str(input_series['Subject code'])))]

    formula_sheet_list =kwarg.get('formula_sheet_list')
    
    output_string='#  \n<br>\n'
    calculus_df = get_calculus_summary_df(df)
    calculus_styler = get_calculus_summary_styler(calculus_df)
    output_string+=calculus_styler.to_html()

    calculus_formulas = pd.concat([calculus_df['Derivative'], 
                                  calculus_df['Equivalent integral']])

    if formulas_contain_items_on_formula_sheet(
        calculus_formulas, formula_sheet_list):
        output_string = (
            '{{< tabs "uniqueid" >}}\n\n' + 
            '{{< tab "Standard view" >}}\n\n' + 
            output_string + '{{< /tab >}}')
        output_string+='\n\n' + '{{< tab "Formula sheet" >}}'
        output_string+='Items on formula sheet are highlighted'
        output_string+='\n<br><br><br>\n'
        calculus_styler = get_calculus_summary_styler(calculus_df, 
                                                      formula_sheet_list)
        output_string+=calculus_styler.to_html()
        output_string+='{{< /tab >}}\n{{< /tabs >}}'
    
    return(output_string)


def get_calculus_summary_df(formulas_df):
    """Returns a summary of derivative and integral formulas as a pandas 
    dataframe"""
    
    calculus_df = (formulas_df
        [['Category', 'Group', 'Formula_1', 
          'Formula_2', 'Comment']]
        [formulas_df["Category"].isin(["Differentiation","Integration"])])
    calculus_df = calculus_df.pivot(
        columns='Category', index = 'Group').fillna('')
    
    # Flatten the multi-index headings after pivot
    calculus_df.columns = (
        calculus_df.columns.get_level_values(0) +' ' + 
        calculus_df.columns.get_level_values(1))
    calculus_df = calculus_df.reset_index()

    calculus_df['Comment'] = (
        calculus_df.apply(_calclus_summary_comment, axis=1))
    
    calculus_df = calculus_df.sort_values(by='Group')
    calculus_df =  calculus_df.drop(
        labels = ['Group', 'Comment Differentiation', 'Comment Integration', 
                  'Formula_2 Integration'], axis = 1)
    calculus_df = calculus_df.rename(columns={
        "Formula_1 Differentiation": "Function", 
        "Formula_1 Integration":"Equivalent integral",
        "Formula_2 Differentiation": "Derivative"})

    # Reorder columns
    calculus_df = calculus_df[['Function', 'Derivative', 
                               'Equivalent integral', 'Comment']]

    return(calculus_df)


def get_calculus_summary_styler(calculus_df, formula_sheet_list=[]):
    """Returns a pandas styler version of the calculus_df dataframe as 
    returned by calculus_df_summary function"""

    if len(formula_sheet_list):
        styler_calculus = df_to_formula_styled_table(
            df=calculus_df, 
            col_widths={'Function': 200, 'Derivative': 300,
                        'Equivalent integral': 400,'Comment':600},
            cols_to_highlight_if_in_formula_sheet= {'Derivative', 
                                                    'Equivalent integral'},
            formula_sheet_list=formula_sheet_list)
    else:
        styler_calculus = df_to_formula_styled_table(
            df=calculus_df, 
            col_widths={'Function': 200, 'Derivative': 300,
                        'Equivalent integral': 400,'Comment':600})

    return(styler_calculus)


def _calclus_summary_comment(row):
    """Returns a comment for calculus formula summary based on 
    derivative and integral comments"""
    if row['Comment Differentiation'] == row['Comment Integration']:
        return_value = row['Comment Differentiation']
    elif row['Comment Differentiation'] == '':
        return_value = row['Comment Integration']
    elif row['Comment Integration'] == '':
        return_value = row['Comment Differentiation']            
    else:
        return_value = (row['Comment Differentiation'] + '\n' + 
                        row['Comment Integration'])
    return(return_value)


def get_financial_summary_display_string(input_series, **kwarg):
    """Returns a financial summmary formula table in markdown format with 
    embedded html.  Input series is a pandas series .  **Kwarg must be 
    called with parameter = formulas_df where formulas_df contains 
    fields State, Subject code, Category, Formula_1, Formula_2.  
    Generates seperate tabs to highlight items on formula sheet if there are
    any"""
    
    df = kwarg['formulas_df'].copy()
    df = df[(
        (df['State'] == str(input_series['State'])) &
        (df['Formula sub category 2'] == str(
            input_series['Formula sub category 2'])) &
        (df['Subject code'] == str(input_series['Subject code'])))]

    formula_sheet_list =kwarg.get('formula_sheet_list')
    
    output_string='#  \n<br>\n'
    financial_df = get_financial_summary_df(df)
    financial_styler = get_financial_summary_styler(financial_df)
    output_string+=financial_styler.to_html()

    financial_formulas = pd.concat([financial_df['Arithmetic sequence'], 
                                  financial_df['Geometric sequence']])

    if formulas_contain_items_on_formula_sheet(
        financial_formulas, formula_sheet_list):
        output_string = (
            '{{< tabs "uniqueid" >}}\n\n' + 
            '{{< tab "Standard view" >}}\n\n' + 
            output_string + '{{< /tab >}}')
        output_string+='\n\n' + '{{< tab "Formula sheet" >}}'
        output_string+='Items on formula sheet are highlighted'
        output_string+='\n<br><br><br>\n'
        financial_styler = get_financial_summary_styler(financial_df, 
                                                      formula_sheet_list)
        output_string+=financial_styler.to_html()
        output_string+='{{< /tab >}}\n{{< /tabs >}}'
    
    return(output_string)


def get_financial_summary_df(formulas_input_df):
    """Returns a summary of financial sequence and series formulas as a
    pandas dataframe"""
    
    df = (formulas_input_df[
          (formulas_input_df['Category'] == 'Financial mathematics') &
          (formulas_input_df['State'] == 'NSW') &
          (
              (formulas_input_df['Sub-category_1'] == 'Arithmetic sequence') | 
              (formulas_input_df['Sub-category_1'] == 'Geometric sequence')
          )
          ])
    
    df = df[['Sub-category_1', 'Sub-category_2', 'Formula_1']]
    df['temp_aggregator'] = 1
    
    df = pd.pivot_table(data=df, values='Formula_1', columns='Sub-category_1', 
                        index='Sub-category_2', aggfunc=lambda x: x)
    df.index.name = None
    df.columns.name = None
    
    # Convert index to categorical data to enable custom sort order
    df.index = pd.Categorical(
        df.index, 
        ['Recursive definition', 'n-th term', 'Sum of first n terms', 
         'Limiting sum'])
    df = df.sort_index()
    return(df)


def get_financial_summary_styler(financial_df, formula_sheet_list=[]):
    """Returns a pandas styler version of the financial_df dataframe as 
    returned by get_financial_summary_df function"""
    if len(formula_sheet_list):
        styler_financial = df_to_formula_styled_table(
            df=financial_df, 
            cols_to_highlight_if_in_formula_sheet= {'Arithmetic sequence', 
                                                    'Geometric sequence'},
            formula_sheet_list=formula_sheet_list)
    else:
        styler_financial = df_to_formula_styled_table(
            df=financial_df)
    return(styler_financial)


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
    return(return_table)


def df_to_formula_styled_table(
    df, col_widths={}, cols_to_highlight_if_in_formula_sheet=[], 
    formula_sheet_list=[], display_col_headers = True,
    display_row_headers = True):
    """Converts pandas dataframe to a styler and applies various formatting
    Note that index of df needs to be unique"""

    styled_table = df.fillna('').style
    styled_table = set_styled_table_widths(styled_table, col_widths)

    if not display_col_headers:
        styled_table = styled_table.hide(axis='columns')
    if not display_row_headers:
        styled_table = styled_table.hide(axis='index')
    


    # Calculate intersect with df columns to avoid error if cols not in df
    cols_to_highlght = list(set(cols_to_highlight_if_in_formula_sheet)
                            & set(list(df.columns)))
    
    for col in cols_to_highlght:
        styled_table = styled_table.applymap(
            is_on_formula_sheet_formatting, 
            subset=[col], 
            formula_sheet_list=formula_sheet_list) 
    
    styled_table = styled_table.set_table_styles ([
        {'selector': 'th.col_heading', 'props': 
         'text-align: left; font-size:1em;'},
        {'selector': 'td', 
         'props': 'text-align: left; font-size:1em;padding: 1.5em;'}]) 

    # below allows newlines in the csv, outside of the latex dollar signs to 
    # be reflected on display
    styled_table= styled_table.set_properties(**{'white-space': 'pre-wrap'})
    
    return (styled_table)


def get_formulas_on_formula_sheet(df):
    """Returns a list of formulas on formula sheet that returns all fields 
    Formula_1 and Formula_2 of the dataframe df where field 'On formula sheet' 
    field is True"""

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
    """Returns formatting for pandas styler object based on whether formulas 
    is contained in formula_sheet list"""
    if formula in formula_sheet_list:
        return ('background-color:rgba(255,194,10, 0.2);')
    else:
        return (None)


def get_single_formula_1(formulas_df, category, description):
    """Returns value in column Formula_1 of data frame formulas_df
    where category and descriptiom match the corresponding columns in the
    data frame
    """
    filtered_df = formulas_df.copy()[(
        (formulas_df['Category'] == category) & 
        (formulas_df['Description'] == description))]
    filtered_array = filtered_df['Formula_1'].unique()
    if len(filtered_array) ==0:
        return_value = 'No matching formula'
    elif len(filtered_array)>1:
        return_value = 'multiple matching formulas'
    else:
        return_value = Math(filtered_array[0])
    return(return_value)
