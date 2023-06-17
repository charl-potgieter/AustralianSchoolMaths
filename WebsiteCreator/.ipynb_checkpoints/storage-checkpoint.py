import os
import shutil
import pandas as pd
import re


def get_docs_path(website_creator_path):
    """Returns the docs directory used to generate hugo webiste content.  The directory 
    path is determined by relative reference to the website_creator_path"""
    return(os.path.join(os.path.dirname(website_creator_path), 'content', 'docs'))
           
def delete_directory_if_it_exists(dir_to_delete):
    """Deletes directory dir_to_delete and its contents if it exists"""
    if os.path.isdir(dir_to_delete):
        shutil.rmtree(dir_to_delete)


def get_formulas_by_year_df(filepath):
    """reads and returns formulas as pandas data frame from filepath"""
    return(pd.read_csv(filepath))


def _get_data_frame_populated_to_column_number(df_input, column_number):
    """Pandas dataframe df_input is filtered where 'column_number' is not null  and
    'column_number+1' is null or does not exist. The first 'column_number' number of 
    columns are returned and the index is reset and started from one.  If the 
    column number is out of range a datframe with headers and no rows is returned"""
    if column_number >= len(df_input.columns):
        empty_df_with_headers =  pd.DataFrame(columns= df_input.columns)
        return(empty_df_with_headers)
    elif column_number == len(df_input.columns) -1: 
        df_filtered = df_input[pd.notnull(df_input.iloc[:,column_number])]    
    else:
        df_filtered = df_input[
            df_input.iloc[:,column_number+1].isnull() & 
            pd.notnull(df_input.iloc[:,column_number])]
        df_filtered = df_filtered.iloc[:,:column_number+1]
    
    df_filtered = df_filtered.reset_index(drop=True)
    df_filtered.index +=1
    
    return(df_filtered)
            

def get_list_of_data_frames_by_populated_to_column_number(file_path):
    """Reads csv at file_path into a data frame and calls function
    _get_data_frame_populated_to_column_number for each column number and returns 
    results in a list"""  
    sort_orders_raw_inputs = pd.read_csv(file_path)
    sort_orders_by_level = []
    for level in range(0, len(sort_orders_raw_inputs.columns)):
        sort_orders_by_level.append(_get_data_frame_populated_to_column_number(sort_orders_raw_inputs, level))
    return (sort_orders_by_level)


def _get_sort_order_for_directory(dir, base_dir, sort_orders):
    """Returns a sort order for dir excluding base_dir by a lookup into sort_orders
    which ia a ordered list of dataframes containing sort orders for various directory
    path lengths (depths).  Returns None if no match found"""
    
    dir_ex_base = _directory_ex_base(dir, base_dir)
    number_of_levels_in_dir_ex_base = _number_of_levels_in_dir(dir_ex_base)

    if number_of_levels_in_dir_ex_base > len(sort_orders):
        return (None)
    
    sort_orders_for_level_number = sort_orders[number_of_levels_in_dir_ex_base-1]
    number_of_rows_of_sort_orders = len(sort_orders_for_level_number.index)

    if number_of_rows_of_sort_orders==0:
        return(None)

    sort_orders_as_series_of_paths = _convert_df_to_series_of_paths(sort_orders_for_level_number)
    index_of_matched_sort_orders = sort_orders_as_series_of_paths[
        sort_orders_as_series_of_paths.str.upper() == dir_ex_base.upper()].index

    display(dir_ex_base)
    display(sort_orders_as_series_of_paths)

    
    if len(index_of_matched_sort_orders)==0:
        sort_order = None
    else:
        sort_order = index_of_matched_sort_orders[0]
    return(sort_order)


def create_sub_directories(base_dir, sub_paths_df):
    """Creates (potentially multi-level) directories under base_dir where sub_paths_df is a pandas dataframe
    where each dataframe row contains different levels of sub-directory path.  No action taken if the
    directory already exists"""
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
    """Returns a series where each item in series is generated from each row in df dataframe
    by joining content of each column in row with a path seperator"""
    series_of_path_lists=df.apply(func  = lambda x:list(x), axis=1)
    series_of_paths = series_of_path_lists.str.join(os.path.sep)
    return (series_of_paths)


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


def _number_of_levels_in_dir(dir):
    """Returns number of levels (folders) in directory dir"""
    return (dir.count(os.path.sep)+1)
    
    


def create_index_files(base_dir, folder_regex='.*', book_collapse=False, sort_orders=None):
    """Creates _index.md files recursively inside base_dir when folder_regex is contained in the 
     folder name.  Optionally add content to the _index.md file based on other optional 
    parameters provided"""

    for root,dirs,files in os.walk(base_dir):
        index_to_be_generated_in_current_dir = len(re.findall(base_dir + folder_regex, root))>0
        if index_to_be_generated_in_current_dir:
            string_to_write = "---\n"                        
            if book_collapse:
                string_to_write = string_to_write + "bookCollapseSection: true\n"
            if sort_orders:
                sort_order = _get_sort_order_for_directory(root, base_dir, sort_orders)
                if sort_order:
                    string_to_write = string_to_write + "weight: " + str(sort_order) + "\n"                
            string_to_write = string_to_write + "---"            
            with open(root + os.path.sep + '_index.md', "w") as text_file:
                text_file.write(string_to_write)