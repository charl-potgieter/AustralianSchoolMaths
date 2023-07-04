import utilities


def get_topics_by_year_df(sort_orders_df):
    """Makes a copy of sort_orders_df and filters to return a dataframe
    of sorted topics by year
    """

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
    of sorted topics by year cumulative
    """

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