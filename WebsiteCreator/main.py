"""Main module for generating markdown files to be utilised for Hugo site
generation.
"""

import os
from maths_objects import (SiteHierarchies, DataSource,
                           FrontMatter, MarkdownFile, Formulas, FormulaTable)
import utilities


def create_index_files(hierarchies, base_dir):
    """Recursively create _index.md file at each level of hieararchies

    Args:
        hierarchies (DirectoryHierarhies): Directory structure where
            _index.md files will be created
    """
    for path in hierarchies.all_path_levels():
        front_matter = FrontMatter()
        path_sort_order = hierarchies.get_sort_index_in_parent_path(
            path)
        # Hugo weight needs to start from 1 not zero therefore add 1 below
        front_matter.add_property('weight', path_sort_order+1)
        front_matter.add_property('bookCollapseSection', 'true')
        index_file = MarkdownFile()
        index_file.add_content(front_matter.to_string())
        index_file.save(base_dir + os.path.sep + path
                        + os.path.sep + '_index.md')


def create_formula_by_year_pages(hierarchies, formulas, base_dir):
    """Creates formulas by year pages ex ad-hoc summaries"""

    for formula_group in formulas.by_state_subject_category():
        path_in_hierarchy = os.path.sep.join([formula_group.state,
                                              formula_group.subject,
                                              'Formulas',
                                              'By year',
                                              formula_group.category])

        front_matter = FrontMatter()
        path_sort_order = hierarchies.get_sort_index_in_parent_path(
            path_in_hierarchy)
        front_matter.add_property('weight', path_sort_order+1)

        formula_table = FormulaTable(formula_group.formulas)

        formula_file = MarkdownFile()
        formula_file.add_content(front_matter.to_string())
        formula_file.add_content(formula_table.to_markdown())
        file_path = base_dir + os.path.sep + path_in_hierarchy + '.md'
        formula_file.save(file_path)


if __name__ == '__main__':

    data_source = DataSource()
    site_hierarchies = SiteHierarchies(data_source.site_hierarchies())
    formulas_by_year = Formulas(data_source.formulas_by_year())

    # Delete previous directories and create new ones with .index.md files
    docs_dir = data_source.docs_directory()
    utilities.delete_directory_if_it_exists(docs_dir)
    site_hierarchies.create_directories(docs_dir)
    create_index_files(site_hierarchies, docs_dir)

    # # Create formula pages
    create_formula_by_year_pages(site_hierarchies, formulas_by_year, docs_dir)
    # # create_formula_cumulative_pages(docs_dir)
