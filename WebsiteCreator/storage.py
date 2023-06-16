import os
import shutil
import pandas as pd
import re


# def _convert_path_to_list(path, exclude_regex=None):
#     """Converts file path to a list where each component of path is converted to a seperate
#     item in the list.  Optionally exclude_regex is removed from path before converting to a list"""

#     if exclude_regex:
#         path_to_convert = re.sub(pattern=exclude_regex, repl='', string=path)
#     else:
#         path_to_convert = path
        
#     return_list = path_to_convert.split(sep=os.path.sep)
    
#     #Remove empty string that arises at start of list at first delimit
#     return_list = list(filter(lambda item:item!='', return_list))
    
#     return(return_list)



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
    'column_number+1' is null. The first 'column_number' number of columns are returned
    and the index is reset and started from one."""
    df_filtered = df_input[
        df_input.iloc[:,column_number+1].isnull() & 
        df_input.iloc[:,column_number]]
    df_select_cols = df_filtered.iloc[:,:column_number+1]
    df_reindex = df_select_cols.reset_index(drop=True)
    df_reindex.index +=1
    
    return(df_reindex)
            

def get_list_of_data_frames_by_populated_to_column_number(file_path):
    """Reads csv at file_path into a data frame and calls function
    _get_data_frame_populated_to_column_number for each column number and returns 
    results in a list"""  
    sort_orders_raw_inputs = pd.read_csv(file_path)
    sort_orders_by_level = []
    for level in range(0, len(sort_orders_raw_inputs.columns)-1):
        sort_orders_by_level.append(_get_data_frame_populated_to_column_number(sort_orders_raw_inputs, level))
    return (sort_orders_by_level)


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


# def _first_index_of_item_in_series(string_to_find, series_to_search):
#     """returns the first index where string_to_find is found in pandas series_to_search.
#     Case insensitive.  Return none if note found."""

#     matching_indices = series_to_search[series_to_search.str.upper() == string_to_find.upper()].index
#     if len(matching_indices):
#         return(matching_indices[0])
#     else:
#         return (None)


def _convert_df_to_series_of_paths(df):
    """Returns a series where each item in series is generated from each row in df dataframe
    by joining content of each column in row with a path seperator"""
    series_of_path_lists=df.apply(func  = lambda x:list(x), axis=1)
    series_of_paths = series_of_path_lists.str.join(os.path.sep)
    return (series_of_paths)

def create_index_files(base_dir, folder_regex='.*', book_collapse=False, sort_orders=None):
    """Creates _index.md files recursively inside base_dir when folder_regex is contained in the 
     folder name.  Optionally add content to the _index.md file based on other optional 
    parameters provided"""

    for root,dirs,files in os.walk(base_dir):
        index_to_be_generated = len(re.findall(base_dir + folder_regex, root))>0
        if index_to_be_generated:
            string_to_write = "---\n"            
            
            if book_collapse:
                string_to_write = string_to_write + "bookCollapseSection: true\n"
            
                # sort_order=_first_index_of_item_in_series(os.path.basename(root), sort_orders)
            # if sort_order:
            #     string_to_write = string_to_write + "weight: " + str(sort_order) + "\n"                
            
            string_to_write = string_to_write + "---"            
            
            with open(root + os.path.sep + '_index.md', "w") as text_file:
                text_file.write(string_to_write)