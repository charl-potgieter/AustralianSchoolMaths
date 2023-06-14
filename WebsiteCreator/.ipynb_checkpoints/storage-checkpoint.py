import os
import shutil
import pandas as pd


def get_docs_path(website_creator_path):
    """Returns the docs directory used to generate hugo webiste content.  The directory 
    path is determined by relative reference to the website_creator_path"""
    return(os.path.join(os.path.dirname(website_creator_path), 'content', 'docs'))

           
def delete_directory_if_it_exists(dir_to_delete):
    """Deletes directory dir_to_delete and its contents if it exists"""
    if os.path.isdir(dir_to_delete):
        shutil.rmtree(dir_to_delete)


def get_sort_orders(order_file_dir):
    """Returns a pandas series formed by the concatenation of all csv files in
    order_file_dir.  The index is not reset and is set to commence from 1 for each file that is concatenated"""
    order_file_paths = csv_files_in_dir(order_file_dir) 
    df_working = pd.DataFrame()
    for filepath in order_file_paths:
        df_read = pd.read_csv(filepath_or_buffer=filepath, header = 0, names = ['sort value'])
        df_working = pd.concat([df_working, df_read])
    df_working.index+=1
    return(df_working['sort value'])


def get_formulas(filepath):
    """reads and returns formulas as pandas data frame from filepath"""
    return(pd.read_csv(filepath))


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


def create_index_files(base_dir, book_collapse=False, sort_orders=None):
    """Creates _index.md files recursively inside base_dir optionally adding content dependent on
    optional parameters provided"""

    for root,dirs,files in os.walk(base_dir):
        string_to_write = "---\n"
        
        if book_collapse:
            string_to_write = string_to_write + "bookCollapseSection: true\n"
        
        if not sort_orders is None:
            sort_order = sort_orders[sort_orders == os.path.basename(root)].index[0]
            string_to_write = string_to_write + "weight: " + str(sort_order) + "\n"
            
        string_to_write = string_to_write + "---"
        
        with open(root + os.path.sep + '_index.md', "w") as text_file:
            text_file.write(string_to_write)