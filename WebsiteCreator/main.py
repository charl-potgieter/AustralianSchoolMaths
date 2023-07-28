"""Main module for generating markdown files to be utilised for Hugo site
generation.
"""

import os
from maths_objects import (DirectoryHierarchies, DataSource,
                           FrontMatter, MarkdownFile)
import utilities


def create_index_files(hierarchies):
    """Recursively create _index.md file at each level of hieararchies

    Args:
        hierarchies (DirectoryHierarhies): Directory structure where
            _index.md files will be created
    """
    for path in hierarchies.all_path_levels():
        front_matter = FrontMatter()
        path_sort_order = hierarchies.get_sort_index_in_parent_path(
            path.split(os.path.sep))
        front_matter.add_property('weight', path_sort_order)
        front_matter.add_property('bookCollapseSection', 'true')
        index_file = MarkdownFile()
        index_file.add_content(front_matter.to_string())
        index_file.save(docs_dir + os.path.sep + path
                        + os.path.sep + '_index.md')


if __name__ == '__main__':

    data_source = DataSource()
    site_hierarchies = DirectoryHierarchies(data_source.site_hierarchies())
    # Delete previous directories and create new ones
    docs_dir = data_source.docs_directory()
    utilities.delete_directory_if_it_exists(docs_dir)
    site_hierarchies.create_directories(docs_dir)
    create_index_files(site_hierarchies)
