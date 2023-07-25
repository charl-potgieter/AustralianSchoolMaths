"""Main module for generating markdown files to be utilised for Hugo site
generation.
"""

import os
from maths_objects import DirectoryHierarchies, IndexFile
import utilities


def create_index_files(hierarchies):
    """Recursively create _index.md file at each level of hieararchies

    Args:
        hierarchies (DirectoryHierarhies): Directory structure where
            _index.md files will be created
    """
    for path in hierarchies.all_path_levels():
        index_file = IndexFile()
        path_sort_order = hierarchies.get_sort_index_in_parent_path(
            path.split(os.path.sep))
        index_file.add_property('bookCollapseSection', 'true')
        index_file.add_property('weight', path_sort_order)
        index_file.save(docs_dir + os.path.sep + path)


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
    create_index_files(site_hierarchies)
