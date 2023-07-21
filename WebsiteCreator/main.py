"""Main module for generating markdown files to be utilised for Hugo site
generation.
"""

import os
from maths_objects import DirectoryHierarchies
import utilities


if __name__ == '__main__':
    # Get inputs
    website_creator_dir = os.path.dirname(__file__)
    docs_dir = utilities.get_docs_path(website_creator_dir)
    formula_file_path = website_creator_dir + os.path.sep + 'formulas.csv'
    hieararchy_file_path = (website_creator_dir + os.path.sep
                            + 'site_hierarchy.csv')
    syllabus_file_path = (website_creator_dir + os.path.sep +
                          'syllabus_topics.csv')

    site_hierarchies = DirectoryHierarchies(hieararchy_file_path)

    # Delete previous directories and create new ones
    utilities.delete_directory_if_it_exists(docs_dir)
    site_hierarchies.create_directories(docs_dir)
