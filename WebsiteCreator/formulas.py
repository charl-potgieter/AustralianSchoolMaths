import pandas as pd
import numpy as np
import os
import shutil
from IPython.display import Markdown, clear_output



def get_formulas_by_year_df(filepath):
    """Reads dataframe from csv at filepath   Returns a dataframe summary 
    containing below columns in order:
         - 'State'
         - new column 'Sub category 1' containing text 'Formulas'
         - new column 'Sub category 2' containing text 'By Year'
         - 'Subject code'
         - 'Category'
         - 'Formula_1'
         - 'Formula_2"""

    df = pd.read_csv(filepath)
    df = (
        df[['State', 'Subject code', 'Category', 'Formula_1', 'Formula_2']])
    df['Sub category 1'] = 'Formulas'
    df['Sub category 2'] = 'By Year'
    df = (df[['State', 'Sub category 1', 'Sub category 2', 
                            'Subject code', 'Category', 'Formula_1', 'Formula_2']])
    return(df)


def get_formula_display_string(input_series, **kwarg):
    """Returns a summmary formula table in markdown format with embedded
    html.  Input series is a pandas series with Indices State, Subec code
    and category.  **Kwarg must be called with parameter  = df_formulas
    where df_Formulas contains fields State, Subject code, Category, 
    Formula_1, Formula_2"""
    
    df_formulas = kwarg['df_formulas']
    df = df_formulas[(
        (df_formulas['State'] == str(input_series['State'])) &
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

    

# def create_formula_files(docs_dir, df_formulas):
#     """Creates formula files in markdown format.  Files are created per state /
#     subject  / category combination and stored in folders under docs_path
#     according to this same combination.  Folders need to already exist"""

#     formula_combinations = (df_formulas
#                             [['State', 'Sub category 1', 'Sub category 2',
#                               'Subject code', 'Category']].
#                             drop_duplicates())
    
#     for index, row in formula_combinations.iterrows():
#         df = df_formulas[(
#             (df_formulas['State'] == row['State']) &
#             (df_formulas['Subject code'] == str(row['Subject code'])) & 
#             (df_formulas['Category'] == row['Category']))]
        
#         formula_2_col_is_empty = df['Formula_2'].dropna().empty    
#         if formula_2_col_is_empty:
#             df = df[['Formula_1']]
#         else:
#             df = df[['Formula_1', 'Formula_2']]
            
#         formula_set_styler = (df_to_formula_styled_table(
#             df=df, col_widths={'Formula_1':300, 'Formula_2':400},
#             display_col_headers = False))
#         output_string =  '#  \n<br>\n' + formula_set_styler.to_html()
#         file_name = (docs_dir + os.path.sep +
#                      row['State'] + os.path.sep + 
#                      row['Sub category 1'] + os.path.sep +
#                      row['Sub category 2'] + os.path.sep  + 
#                      str(row['Subject code']) + os.path.sep  + 
#                      row['Category']  + '.md')
#         with open(file_name, "w") as text_file:
#             text_file.write(output_string)
        

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


def styler_calculus_summary(df_calculus, formula_sheet=[]):
    """Returns a pandas styler version of the df_calculus dataframe as returned by df_calculus_summary function"""

    if len(formula_sheet):
        styler_calculus = df_to_formula_styled_table(df=df_calculus, 
                                                     col_widths={'Function': 200, 'Derivative': 300,'Equivalent integral': 400,'Comment':600},
                                                     cols_to_highlight_if_in_formula_sheet= {'Derivative', 'Equivalent integral'},
                                                     formula_sheet=formula_sheet)
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


def df_to_formula_styled_table(df, col_widths={}, cols_to_highlight_if_in_formula_sheet=[], formula_sheet=[], display_col_headers = True):
    """Converts pandas dataframe to a styler and applies various formatting"""

    styled_table = df.fillna('').style
    styled_table = set_styled_table_widths(styled_table, col_widths)

    if not display_col_headers:
        styled_table = styled_table.hide().hide(axis='columns')

    for col in cols_to_highlight_if_in_formula_sheet:
        styled_table = styled_table.applymap(is_on_formula_sheet_formatting, subset=[col], formula_sheet=formula_sheet) 
    
    styled_table = styled_table.set_table_styles ([
        {'selector': 'th.col_heading', 'props': 'text-align: left; font-size:1em;'},
        {'selector': 'td', 'props': 'text-align: left; font-size:1em;padding: 1.5em;'}]) 

    # below allows newlines in the csv, outside of the latex dollar signs to be reflected on display
    styled_table= styled_table.set_properties(**{'white-space': 'pre-wrap'})
    
    return (styled_table)


def formulas_on_formula_sheet(df_formulas):
    """Returns a list of formulas on formula sheet that returns all fields Formula_1 and Formula_2 of 
    df_Formulas where field 'On formula sheet' is True"""
    formulas_one_on_sheet = df_formulas[df_formulas['On formula sheet'] == True]['Formula_1'].values.tolist()
    formulas_two_on_sheet = df_formulas[df_formulas['On formula sheet'] == True]['Formula_2'].values.tolist()
    formulas_on_sheet = formulas_one_on_sheet + formulas_two_on_sheet
    return (formulas_on_sheet)


def is_on_formula_sheet_formatting(formula, formula_sheet):
    """Returns formatting for pandas styler object based on whether formulas is contained in formula_sheet list"""
    if formula in formula_sheet:
        return ('background-color:rgba(255,194,10, 0.2);')
    else:
        return (None)



