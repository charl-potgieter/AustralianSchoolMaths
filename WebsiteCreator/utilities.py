"""Various utilities to assist in generation of maths summary Hugo static
web pages.
"""

import os
import shutil
import pandas as pd


def get_docs_path(website_creator_path):
    """Returns the docs directory used to generate hugo webiste content.
    The directory path is determined by relative reference to the
    website_creator_path"""
    return (os.path.join(
        os.path.dirname(website_creator_path),
        'content', 'docs'))


def delete_directory_if_it_exists(dir_to_delete):
    """Deletes directory dir_to_delete and its contents if it exists"""
    if os.path.isdir(dir_to_delete):
        shutil.rmtree(dir_to_delete)


def lookup_list_in_df(df_source, list_to_find):
    """Looks up list_to find in each row of a modified version pandas
    dataframe df_source and returns the first index where a match is found.
    df_source is modified as follows before the lookup above is perforemed:
        -  list_len = len(list_to_find)
        - filtered on column index list_len == null and
          column number list-len - 1 != null
        - filter df_source where first n-1 columns equals the first n-1
          elements in the list
        - the index is reset after the filter
        - Find the index of the nth element in the list in the nth column of
          the data frame
    """

    list_len = len(list_to_find)
    if list_len > len(df_source.columns):
        return None

    if list_len < len(df_source.columns):
        df_source = df_source[df_source.iloc[:, list_len].isnull()]

    df_source = df_source[df_source.iloc[:, list_len-1].notnull()]

    for i in range(len(list_to_find)-1):
        df_source = df_source[(df_source.iloc[:, i].str.upper() ==
                               str(list_to_find[i]).upper())]
    df_source = df_source.reset_index(drop=True)

    df_source = df_source[(df_source.iloc[:, list_len-1].str.upper() ==
                           str(list_to_find[list_len-1]).upper())]
    filtered_index = df_source.index

    if len(filtered_index) == 0:
        return None
    else:
        return filtered_index[0]


def create_subdirectories_from_df(base_dir, subpaths_df):
    """Creates (potentially multi-level) directories under base_dir where
    subpaths_df is a pandas dataframe where each dataframe row contains
    different levels of sub-directory path.  No action taken if the directory
    already exists"""
    subpaths_array = subpaths_df.to_numpy(dtype=str)
    for path in subpaths_array:
        fname = base_dir + os.path.sep + os.path.sep.join(path)
        os.makedirs(fname, exist_ok=True)


def create_index_files(base_dir, dirs_df, front_matter=None,
                       sort_orders_df=None):
    """Creates _index.md files recursively at each level of the directory
    strucutres formed by joining base_dir string and each row of pandas
    dataframe dirs_df.  The content of each file is set based  on the content
    of the front_matter dictionary and optionally includes a weight
    (sort order) based on the order of each directory in sort_orders_df """
    if front_matter is None:
        front_matter = {}
    for i in range(1, len(dirs_df.columns)+1):
        # Looping through various levels in directory structure
        subdirs_df = dirs_df.iloc[:, :i].drop_duplicates()
        for _, row in subdirs_df.iterrows():
            file_name = (base_dir + os.path.sep +
                         os.path.sep.join(row) + os.path.sep + '_index.md')
            if not os.path.isfile(file_name):
                # Don't overwrite file if it exists
                # Use a copy on each loop to start fresh and not
                # carry over any details from previos loop
                front_matter_to_write = front_matter.copy()
                if sort_orders_df is not None:
                    sort_order = lookup_list_in_df(
                        sort_orders_df, list(row.values))
                    if sort_order is not None:
                        front_matter_to_write['weight'] = sort_order + 1
                string_to_write = get_front_matter_string(
                    front_matter_to_write)
                with open(file_name, "w", encoding="utf-8") as text_file:
                    text_file.write(string_to_write)


def create_files(base_dir, file_paths_df, file_extension, string_creator,
                 front_matter=None, sort_orders_df=pd.DataFrame(), **kwargs):
    """Creates a file for each row in file_paths_df.  The file path is
    base_dir combined with the path formed from the row of file_paths_df.
    The content on the file is determined by passing each row of the
    file_paths_df as well as **kwargs to function string_creator"""
    if front_matter is None:
        front_matter = {}
    for index, row in file_paths_df.iterrows():
        # Use a copy on each loop to start fresh and not
        # carry over any details from previos loop
        front_matter_to_write = front_matter.copy()

        # Get front matter portion of the string:
        if not sort_orders_df.empty:
            sort_order = lookup_list_in_df(
                sort_orders_df, list(row.values))
            if sort_order is not None:
                front_matter_to_write['weight'] = sort_order + 1
        string_to_write = get_front_matter_string(front_matter_to_write)

        # Add the row of the dataframe to kwargs to enable passing to the
        # string_creator function as keyword arguments
        for index, value in row.items():
            kwarg_keyword = index.lower().replace(' ', '_')
            kwargs[kwarg_keyword] = str(value)
        kwargs['sort_orders_df'] = sort_orders_df

        string_to_write += string_creator(**kwargs)

        file_name = (base_dir + os.path.sep +
                     os.path.sep.join(row) + file_extension)
        with open(file_name, "w", encoding="utf-8") as text_file:
            text_file.write(string_to_write)


def get_front_matter_string(input_dict=None):
    """Generates a front matter string for writing to a hugo .md file
    based on the values provided input_dict"""
    if input_dict is None:
        input_dict = {}
    string_to_write = "---\n"
    for key in input_dict:
        string_to_write += key + ': ' + str(input_dict[key]) + '\n'
    string_to_write += "---\n\n"
    return string_to_write


def series_intersect(first_series, *args):
    """Returns true if there is a common intersect of each pandas series
    in first_serries and *args.  Nulls are exluded"""
    current_intersect = set(first_series.loc[lambda x: x.notnull()])
    for current_series in args:
        if current_series is None or current_series.empty:
            return False
        else:
            current_series = current_series.loc[lambda x: x.notnull()]
        current_intersect = current_intersect & set(current_series)
    return len(current_intersect) > 0
