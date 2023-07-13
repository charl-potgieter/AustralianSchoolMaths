import utilities
import pandas as pd
import os
from IPython import embed


def create_topics_content(topics_df, sort_orders_df, docs_dir, topics_dir):
    """Creates markdown files containing topic tables as input for static 
    web page creation via Hugo
    """
    dirs_df = (
        topics_df[['State', 'Topic sub category 1', 
                             'Topic sub category 2',
                             'Subject code']].drop_duplicates())
    file_paths_df = (
        topics_df[['State', 'Topic sub category 1', 
                             'Topic sub category 2',
                             'Subject code', 'Topic']].drop_duplicates())
    utilities.create_sub_directories_from_df(base_dir = docs_dir, 
                                             sub_paths_df = dirs_df)
    front_matter_index_files = {'bookCollapseSection' : True}
    utilities.create_index_files(base_dir=docs_dir, dirs_df=dirs_df, 
                                 front_matter=front_matter_index_files,
                                 sort_orders_df = sort_orders_df)
    utilities.create_files(base_dir = docs_dir, file_paths_df= file_paths_df, 
                           file_extension='.md', 
                           fn=get_topic_display_string, 
                           sort_orders_df=sort_orders_df,
                           topics_df=topics_df,
                           topics_dir=topics_dir)


def get_topic_display_string(topic, topics_dir,  topic_sub_category_1, 
                             topic_sub_category_2, subject_code, 
                             sort_orders_df, topics_df, state):
    """ Returns a topic summary in markdown forma. """  
    file_name = topic.lower().replace(' ', '_') + '.ipynb'
    file_path = topics_dir + os.path.sep + file_name
    if os.path.isfile(file_path):
        if topic_sub_category_2.upper() == 'BY YEAR':
            tags = [subject_code]
        elif (topic_sub_category_2.upper() == 
              'BY YEAR CUMULATIVE'):                  
            tags = previous_subject_codes(sort_orders_df, 
                                         subject_code)
        else:
            tags = []
        output_str = utilities.filtered_notebook_md_string(
            input_notebook_path=file_path, include_tags=tags, 
            remove_input_tags=['hide_code'])                                          
    return(output_str)


def get_topics_df(sort_orders_df):
    """Returns a combined pandas dataframe from sort_orders_df
    containging topics by year (subject code) as well as cumululative
    topics by year (subject code)"""
    by_year_df =  (
        get_topics_by_year_df(sort_orders_df))
    cumulative_df = (
        get_topics_cumulative_df(sort_orders_df))
    topics_df = pd.concat([by_year_df, cumulative_df])
    return(topics_df)


def get_topics_by_year_df(sort_orders_df):
    """Makes a copy of sort_orders_df and filters to return a dataframe
    of sorted topics by year."""
    df = sort_orders_df.copy()
    df = df.rename(
        columns={'Level_0':'State', 'Level_1':'Topic sub category 1',
                 'Level_2':'Topic sub category 2', 'Level_3':'Subject code',
                 'Level_4':'Topic'})
    df = (df[
          (df['Topic sub category 1'].str.upper()=='TOPICS') & 
          (df['Topic sub category 2'].str.upper()=='BY YEAR') & 
          (df['Topic'].notnull())
          ])
    df = df[['State', 'Topic sub category 1',  'Topic sub category 2',
             'Subject code', 'Topic']]
    return(df)


def get_topics_cumulative_df(sort_orders_df):
    """Makes a copy of sort_orders_df and filters to return a dataframe
    of sorted topics by year cumulative"""

    df = sort_orders_df.copy()
    df = df.rename(
        columns={'Level_0':'State', 'Level_1':'Topic sub category 1',
                 'Level_2':'Topic sub category 2', 'Level_3':'Subject code',
                 'Level_4':'Topic'})
    df = (df[
          (df['Topic sub category 1'].str.upper()=='TOPICS') & 
          (df['Topic sub category 2'].str.upper()=='BY YEAR CUMULATIVE') & 
          (df['Topic'].notnull())
          ])
    df = df[['State', 'Topic sub category 1',  'Topic sub category 2',
             'Subject code', 'Topic']]
    return(df)


def previous_subject_codes(sort_orders_df, subject_code):
    """Returns a list of subject codes ups to and including subject_code
    based on the order in df_sort_orders and the logic below"""

    sorted_subject_codes = list(sort_orders_df[
        (sort_orders_df['Level_1'].str.upper()=='TOPICS') & 
        (sort_orders_df['Level_2'].str.upper()=='BY YEAR') & 
        (sort_orders_df['Level_3'].notnull()) &                                 
        (sort_orders_df['Level_4'].isnull())
    ]['Level_3'])
    subject_code_index = sorted_subject_codes.index(subject_code)
    return(sorted_subject_codes[:subject_code_index+1])