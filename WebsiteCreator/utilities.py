"""Various utilities to assist in generation of maths summary Hugo static
web pages.
"""

import os
import shutil
import pandas as pd


def delete_directory_if_it_exists(dir_to_delete):
    """Deletes directory dir_to_delete and its contents if it exists"""
    if os.path.isdir(dir_to_delete):
        shutil.rmtree(dir_to_delete)


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
