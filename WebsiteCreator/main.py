"""Main module for generating markdown files to be utilised for Hugo site
generation.
"""

import os
import shutil
from maths_objects import (SiteHierarchies, DataSource,
                           IndexFile,  FormulaFile,
                           Formulas, FormulaTable, FormulaTableType,
                           FormulaTableTypeSimple,  FormulaTableTypeCalculus)


def delete_directory_if_it_exists(dir_to_delete):
    """Deletes directory dir_to_delete and its contents if it exists"""
    if os.path.isdir(dir_to_delete):
        shutil.rmtree(dir_to_delete)


def create_index_files(hierarchies, base_dir):
    """Recursively create _index.md file at each level of hieararchies

    Args:
        hierarchies (DirectoryHierarhies): Directory structure where
            _index.md files will be created prefixed by base_dir
        base_dir (string) : Start of direcctory for file saving
    """
    for path in hierarchies.all_path_levels:
        index_file = IndexFile(path)
        index_file.add_front_matter_property('bookCollapseSection', 'true')
        index_file.set_weight_based_on_hierarchies(hierarchies)
        index_file.save(base_dir)


def create_formula_pages(table_type: FormulaTableType,
                         group_by: list,
                         formulas: Formulas,
                         base_dir: str,
                         hierarchies: SiteHierarchies,
                         is_cumulative_by_year: bool = False):
    """Creates formula pages"""

    for formula_group in formulas.group_by_columns(group_by):
        formula_table = FormulaTable(formula_group)
        formula_table.type = table_type
        if formula_table.contains_content:
            formula_file = FormulaFile()
            formula_file.is_cumulative_by_year = is_cumulative_by_year
            formula_file.add_formula_table(formula_table)
            formula_file.set_weight_based_on_hierarchies(hierarchies)
            formula_file.save(base_dir)


if __name__ == '__main__':

    data_source = DataSource()
    site_hierarchies = SiteHierarchies(data_source.site_hierarchies)

    # Delete previous directories and create new ones with .index.md files
    docs_dir = data_source.docs_directory
    delete_directory_if_it_exists(docs_dir)
    site_hierarchies.create_directories(docs_dir)
    create_index_files(site_hierarchies, docs_dir)

    formulas_by_year = Formulas(data_source.formulas_by_year)
    formulas_cumulative = Formulas(data_source.formulas_by_year_cumulative)

    create_formula_pages(table_type=FormulaTableTypeSimple,
                         group_by=['State', 'Subject', 'Category'],
                         formulas=formulas_by_year,
                         base_dir=data_source.docs_directory,
                         hierarchies=site_hierarchies,
                         is_cumulative_by_year=False)

    create_formula_pages(table_type=FormulaTableTypeSimple,
                         group_by=['State', 'Subject', 'Category'],
                         formulas=formulas_cumulative,
                         base_dir=data_source.docs_directory,
                         hierarchies=site_hierarchies,
                         is_cumulative_by_year=True)

    create_formula_pages(table_type=FormulaTableTypeCalculus,
                         group_by=['State', 'Subject'],
                         formulas=formulas_by_year,
                         base_dir=data_source.docs_directory,
                         hierarchies=site_hierarchies,
                         is_cumulative_by_year=False)

    create_formula_pages(table_type=FormulaTableTypeCalculus,
                         group_by=['State', 'Subject'],
                         formulas=formulas_cumulative,
                         base_dir=data_source.docs_directory,
                         hierarchies=site_hierarchies,
                         is_cumulative_by_year=True)
