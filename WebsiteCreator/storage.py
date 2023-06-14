import os
import shutil
import pandas as pd


def get_docs_path():
    """Returns the docs directory used to generate hugo webiste content.  The directory 
    path is determined by relative reference to the file containing this code"""
    return(os.path.join(os.path.dirname(os.getcwd()), 'content', 'docs'))

           
def delete_directory_if_it_exists(dir_to_delete):
    """Deletes directory dir_to_delete and its contents if it exists"""
    if os.path.isdir(dir_to_delete):
        shutil.rmtree(dir_to_delete)