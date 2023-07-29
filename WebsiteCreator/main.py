"""Main module for generating markdown files to be utilised for Hugo site
generation.
"""

import os
from maths_objects import (SiteHierarchies, DataSource,
                           FrontMatter, MarkdownFile, Formulas)
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
            path)
        # Hugo weight needs to start from 1 not zero therefore add 1 below
        front_matter.add_property('weight', path_sort_order+1)
        front_matter.add_property('bookCollapseSection', 'true')
        index_file = MarkdownFile()
        index_file.add_content(front_matter.to_string())
        index_file.save(docs_dir + os.path.sep + path
                        + os.path.sep + '_index.md')


def create_formula_by_year_pages(base_dir):
    """Creates formula by year pages in base_dir directory"""
    formulas = Formulas(data_source.formulas_by_year())
    for formula_table in formulas.formula_tables():
        target_dir = os.path.sep.join([
            base_dir, formula_table.state, 'Formulas', 'By year',
            formula_table.subject
        ])
        target_filename = (target_dir + os.path.sep
                           + formula_table.category + '.md')
        if not os.path.isdir(target_dir):
            raise ValueError(target_dir.replace(base_dir, '')
                             + ' does not exist in site_hierarchy.csv')
        with open(target_filename, "w", encoding="utf-8") as text_file:
            text_file.write(formula_table.to_markdown())


def create_formula_cumulative_pages(base_dir):
    """Creates formula by year cumulative pages in base_dir directory"""
    formulas = Formulas(data_source.formulas_by_year_cumulative())
    for formula_table in formulas.formula_tables():
        target_dir = os.path.sep.join([
            base_dir, formula_table.state, 'Formulas', 'By year cumulative',
            formula_table.subject
        ])
        target_filename = (target_dir + os.path.sep
                           + formula_table.category + '.md')
        if not os.path.isdir(target_dir):
            raise ValueError(target_dir.replace(base_dir, '')
                             + ' does not exist in site_hierarchy.csv')
        with open(target_filename, "w", encoding="utf-8") as text_file:
            text_file.write(formula_table.to_markdown())


if __name__ == '__main__':

    data_source = DataSource()
    site_hierarchies = SiteHierarchies(data_source.site_hierarchies())

    # Delete previous directories and create new ones with .index.md files
    docs_dir = data_source.docs_directory()
    utilities.delete_directory_if_it_exists(docs_dir)
    site_hierarchies.create_directories(docs_dir)
    create_index_files(site_hierarchies)

    # Create formula pages
    create_formula_by_year_pages(docs_dir)
    create_formula_cumulative_pages(docs_dir)
