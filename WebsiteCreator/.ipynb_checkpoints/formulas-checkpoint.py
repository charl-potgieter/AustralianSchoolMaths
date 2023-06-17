import pandas as pd
import numpy as np
import os
import shutil
from IPython.display import Markdown, clear_output


def get_formula_by_year_summary_df(df_formulas):
    """Returns a dataframe summary of df_formulas containing unique set of below columns
    in order:
         - df_formulas['State']
         - new column 'Sub category 1' containing text 'Formulas'
         - new column 'Sub category 2' containing text 'By Year'
         - df['Subject code']
         - df['Category']"""
    return_df = df_formulas[['State', 'Subject code', 'Category']].drop_duplicates()
    return_df['Sub category 1'] = 'Formulas'
    return_df['Sub category 2'] = 'By Year'
    return_df = return_df[['State', 'Sub category 1', 'Sub category 2', 'Subject code', 'Category']]
    return(return_df)


def create_formula_index_files(docs_dir, df_sort_orders):
    """Creates _index.md files in relevant folder under root_dir to manage nested website menu """
    
    formulas_by_year_path = docs_dir + os.path.sep + 'formulas by year'
    formulas_cumulative_path = docs_dir + os.path.sep + 'formulas cumulative'
    
    with open(formulas_by_year_path + os.path.sep + '_index.md', "w") as text_file:
        text_file.write("---\n" + 
                        "bookCollapseSection: true\n" +
                        "weight: 1\n" +
                        "---\n\n" +
                       "This section of the website includes current year / course formulas only.")

    with open(formulas_cumulative_path + os.path.sep + '_index.md', "w") as text_file:
        text_file.write("---\n" + 
                        "bookCollapseSection: true\n" +
                        "weight: 2\n" +
                        "---\n\n" +
                       "This section of the website includes both formulas covered in current and previous years \ courses")

    for root,dirs,files in os.walk(formulas_by_year_path):
        #Exclude formulas_by_year_path as index file is already created above
        if root != formulas_by_year_path:
            sort_order = df_sort_orders[df_sort_orders['sort value'] == os.path.basename(root)].index.tolist()[0]
            with open(root + os.path.sep + '_index.md', "w") as text_file:
                text_file.write("---\n" + 
                                "bookCollapseSection: true\n" + 
                                "weight: " + str(sort_order) + "\n" +
                                "---")

    for root,dirs,files in os.walk(formulas_cumulative_path):
        #Exclude formulas_cumulative_path as index file is already created above
        if root!=formulas_cumulative_path:
            sort_order = df_sort_orders[df_sort_orders['sort value'] == os.path.basename(root)].index.tolist()[0]
            with open(root + os.path.sep + '_index.md', "w") as text_file:
                text_file.write("---\n" + 
                                "bookCollapseSection: true\n" + 
                                "weight: " + str(sort_order) + "\n" +
                                "---")

def create_formula_files(docs_dir, df_formulas):
    """Creates formula files in markdown format.  Files are created per state / subject  / category
    combination and stored in folders under docs_path according to this same combination"""

    formula_combination = df_formulas[['State', 'Subject code', 'Category']].drop_duplicates()

    for index, row in formula_combination.iterrows():
        formula_set_df = formulas_by_state_subject_category_df(df_formulas, row['State'], row['Subject code'], row['Category'])
        formula_set_styler = df_to_formula_styled_table(df=formula_set_df,col_widths={'Formula_1':300, 'Formula_2':400},
                                                        display_col_headers = False)
        output_string =  '#  \n<br>\n' + formula_set_styler.to_html()
        file_name = docs_dir + os.path.sep +'formulas by year' \
            + os.path.sep  + row['State'] \
            + os.path.sep  + str(row['Subject code']) \
            + os.path.sep  + row['Category']  + '.md'
        with open(file_name, "w") as text_file:
            text_file.write(output_string)


def formulas_by_state_subject_category_df(df_formulas, state, subject_code, category):
    """returns all formulas for given state, subject and category, returns formula_1 column and formula_2 column if not empty
    The return value is a pandas dataframe"""

    df_filtered =  df_formulas[
        (df_formulas['State'] == state) &
        (df_formulas['Subject code'] == str(subject_code)) & 
        (df_formulas['Category'] == category)]   
    formula_2_col_is_empty = df_filtered['Formula_2'].dropna().empty
    
    if formula_2_col_is_empty:
        df_filtered = df_filtered[['Formula_1']]
    else:
        df_filtered = df_filtered[['Formula_1', 'Formula_2']]

    return (df_filtered)
        

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


