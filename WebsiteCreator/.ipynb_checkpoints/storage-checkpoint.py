import os
import shutil
import pandas as pd
import re

 
def get_docs_path(website_creator_path):
    """Returns the docs directory used to generate hugo webiste content.  
    The directory path is determined by relative reference to the 
    website_creator_path"""
    return(os.path.join(
        os.path.dirname(website_creator_path), 
        'content', 'docs'))


def delete_directory_if_it_exists(dir_to_delete):
    """Deletes directory dir_to_delete and its contents if it exists"""
    if os.path.isdir(dir_to_delete):
        shutil.rmtree(dir_to_delete)


def get_formulas_by_year_df(filepath):
    """reads and returns formulas as pandas data frame from filepath"""
    return(pd.read_csv(filepath))


def _get_data_frame_filtered_to_column_number(df_input, column_number):
    """Pandas dataframe df_input is filtered where 'column_number' is not null
    and 'column_number+1' is null or does not exist. The first 'column_number'
    number of columns are returned and the index is reset and started from one.
    If the column number is out of range or the filtered result is empty then 
    None is returned"""
    
    if column_number >= len(df_input.columns):
        return(None)
    elif column_number == len(df_input.columns) -1: 
        df_filtered = df_input[pd.notnull(df_input.iloc[:,column_number])]    
    else:
        df_filtered = df_input[
            df_input.iloc[:,column_number+1].isnull() & 
            pd.notnull(df_input.iloc[:,column_number])]
        df_filtered = df_filtered.iloc[:,:column_number+1]

    if len(df_filtered.index) ==0:
        # There is no data after filter is apppled
        return (None)
    else:
        df_filtered = df_filtered.reset_index(drop=True)
        df_filtered.index +=1    
        return(df_filtered)
            

def create_sub_directories(base_dir, sub_paths_df):
    """Creates (potentially multi-level) directories under base_dir where 
    sub_paths_df is a pandas dataframe where each dataframe row contains 
    different levels of sub-directory path.  No action taken if the directory 
    already exists"""
    sub_paths_array=sub_paths_df.to_numpy(dtype = str)
    for path in sub_paths_array:
        fname = base_dir + os.path.sep + os.path.sep.join(path)
        os.makedirs(fname, exist_ok=True)


def csv_files_in_dir(dir):
    """Returns a list of csv files in dir (non-recursive)"""
    return_list = []
    for item in os.listdir(dir):
        file_ext = os.path.splitext(item)[1]
        if file_ext.upper() == '.CSV':
            return_list.append(dir + os.path.sep + item)
    return(return_list)


def _convert_df_to_series_of_paths(df):
    """Returns a series where each item in series is generated from each row in
    df dataframe by joining content of each column in row with a path 
    seperator.  If df has no data an empty series is returned"""
    if (df is not None) and len(df.index):
        series_of_path_lists=df.apply(func  = lambda x:list(x), axis=1)
        series_of_paths = series_of_path_lists.str.join(os.path.sep)
        return (series_of_paths)
    else:
        return(pd.Series(dtype=object))


def _directory_ex_base(dir, base_dir):
    """returns a sub-dir calcualted from dir with the removal of 
    base_dir from the start of dir.  Any path seperator is removed 
    from start and end of the resulting path before it is returned"""
    dir_ex_base = re.sub(pattern='^'+base_dir, repl='', string=dir)
    if dir_ex_base[0] == os.path.sep:
        dir_ex_base = dir_ex_base[1:]
    if dir_ex_base[-1] == os.path.sep:
        dir_ex_base = dir_ex_base[:-1]
    return(dir_ex_base)

def _series_index_based_on_string_lookup(series, value):
    """Looks up string in pandas series and returns the first index found.
    Returns None if not found.  Case insensitive"""
    index_of_matched_values = series[series.str.upper() == value.upper()].index
    if len (index_of_matched_values)==0:
        return(None)
    else:
        return (index_of_matched_values[0])


def _number_of_levels_in_dir(dir):
    """Returns number of levels (folders) in directory dir"""
    return (dir.count(os.path.sep)+1)
    
    
def create_index_files(base_dir, folder_regex='.*', book_collapse=False, 
                       df_sort_orders=pd.DataFrame()):
    """Creates _index.md files recursively inside base_dir when base_dir + 
    folder_regex iscontained in the folder name.  Optionally add content to
    the _index.md file based on other optional parameters provided"""

    for root,dirs,files in os.walk(base_dir):
        index_to_be_generated_in_current_dir = (
            len(re.findall(base_dir + folder_regex, root))>0)
        if index_to_be_generated_in_current_dir:
            string_to_write = "---\n"                        
            
            if book_collapse:
                string_to_write = (string_to_write + 
                                   "bookCollapseSection: true\n")
            
            # Add page weight if a sort order has been set
            sub_dir = _directory_ex_base(root, base_dir)
            number_of_sub_dir_levels = _number_of_levels_in_dir(sub_dir)
            df_sort_orders_for_level = (
                _get_data_frame_filtered_to_column_number(
                    df_sort_orders, number_of_sub_dir_levels-1))
            sort_orders_as_series_of_paths = (
                _convert_df_to_series_of_paths(df_sort_orders_for_level))
            sort_order = (
                _series_index_based_on_string_lookup(
                    sort_orders_as_series_of_paths, sub_dir))
            if sort_order:
                string_to_write = (string_to_write + 
                                   "weight: " + str(sort_order) + "\n")
                
            string_to_write = string_to_write + "---"
            
            with open(root + os.path.sep + '_index.md', "w") as text_file:
                text_file.write(string_to_write)
