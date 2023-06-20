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


def lookup_list_in_df(df, list_to_find):
    """Looks up list_to find in each row of a modified version pandas dataframe
    df and returns the first index where a match is found.
    df is modified as follows before the lokup above is perforemed:
        -  list_len = len(list_to_find)
        - filtered on column number list_len == null and 
          column number list-len - 1 != null
        - restrict df to  the first list_len number of columns
        - the index is reset after the filter
    """
    
    list_len = len(list_to_find)
    if list_len > len(df.columns):
        return (None)
    elif list_len == len(df.columns):
        df = df[df.iloc[:,list_len-1].notnull()]
    else:
        df = df[(
            (df.iloc[:,list_len].isnull()) &
            (df.iloc[:,list_len-1].notnull())
        )].iloc[:, :list_len]
    df = df.reset_index(drop = True)
    
    for i in range(len(list_to_find)):
        df = df[(df.iloc[:, i].str.upper() == 
                           str(list_to_find[i]).upper())]
    filtered_index = df.index
    
    if len(filtered_index) == 0:
        return (None)
    else:
        return (filtered_index[0])
            

def create_sub_directories_from_df(base_dir, sub_paths_df):
    """Creates (potentially multi-level) directories under base_dir where 
    sub_paths_df is a pandas dataframe where each dataframe row contains 
    different levels of sub-directory path.  No action taken if the directory 
    already exists"""
    sub_paths_array=sub_paths_df.to_numpy(dtype = str)
    for path in sub_paths_array:
        fname = base_dir + os.path.sep + os.path.sep.join(path)
        os.makedirs(fname, exist_ok=True)


def create_index_files(base_dir, dirs_df,front_matter={}, 
                       sort_orders_df=None):
    """Creates _index.md files recursively at each level of the directory 
    strucutres formed by joining base_dir string and each row of pandas
    dataframe dirs_df.  The content of each file is set based  on the content
    of the front_matter dictionary and optionally includes a weight 
    (sort order) based on the order of each directory in sort_orders_df """

    for i in range(1, len(dirs_df.columns)+1):
        # Looping through various levels in directory structure
        subdirs_df = dirs_df.iloc[:, :i].drop_duplicates()
        for index, row in subdirs_df.iterrows():

            # Use a copy on each loop to start fresh and not 
            # carry over any details from previos loop
            front_matter_to_write = front_matter.copy()
                    
            file_name = (base_dir + os.path.sep + 
                         os.path.sep.join(+ row) + os.path.sep + '_index.md')

            if sort_orders_df is not None:
                sort_order = lookup_list_in_df(
                    sort_orders_df, list(row.values))
                if sort_order is not None:
                    front_matter_to_write['weight'] = sort_order + 1
            string_to_write = get_front_matter_string(front_matter_to_write)
            
            with open(file_name, "w") as text_file:
                text_file.write(string_to_write)


def create_files(base_dir, file_paths_df, file_extension, fn,
                 front_matter = {}, sort_orders_df = None, **kwargs):
    """Creates a file for each row in file_paths_df.  The file path is 
    base_dir combined with the path formed from the row of file_paths_df.
    The conent on the file is determined by passing each row of the 
    file_paths_df as well as **kwargs to function fn"""
    
    for index, row in file_paths_df.iterrows():

        # Use a copy on each loop to start fresh and not 
        # carry over any details from previos loop
        front_matter_to_write = front_matter.copy()
        
        # Get front matter portion of the string:
        if sort_orders_df is not None:
            sort_order = lookup_list_in_df(
                sort_orders_df, list(row.values))
            if sort_order is not None:
                front_matter_to_write['weight'] = sort_order + 1
        string_to_write = get_front_matter_string(front_matter_to_write)

        # Add other file content to the front matter
        string_to_write += fn(row, **kwargs)
        
        file_name = (base_dir + os.path.sep + 
                     os.path.sep.join(+ row) + file_extension)
        with open(file_name, "w") as text_file:
            text_file.write(string_to_write)


def get_front_matter_string(input_dict= {}):
    """Generates a front matter string for writing to a hugo .md file
    based on the values provided input_dict"""
    string_to_write = "---\n"                            
    for key in input_dict:
        string_to_write += key + ': ' + str(input_dict[key]) + '\n'
    string_to_write += "---\n\n"
    return(string_to_write)