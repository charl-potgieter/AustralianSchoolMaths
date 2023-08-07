"""Main module for generating markdown files to be utilised for Hugo site
generation.
"""

import os
import shutil
import itertools
from data_management import DataSource
from file_management import (SiteHierarchies, IndexFile,  FormulaFile)
from formula_tables import (FormulaTable, FormulaTableType,
                            FormulaTableTypeSimple, FormulaTableTypeCalculus,
                            FormulaTableTypeFinancial)
from content import Formulas


def create_directory_structure():
    """Creates directory structure"""
    data_source = DataSource()
    docs_dir = data_source.docs_directory
    _delete_directory_if_it_exists(docs_dir)
    hierarchies = SiteHierarchies(data_source.site_hierarchies)
    hierarchies.create_directories(docs_dir)


def _delete_directory_if_it_exists(dir_to_delete):
    """Deletes directory dir_to_delete and its contents if it exists"""
    if os.path.isdir(dir_to_delete):
        shutil.rmtree(dir_to_delete)


def create_index_files():
    """Recursively create _index.md file at each level of hieararchies"""
    data_source = DataSource()
    docs_dir = data_source.docs_directory
    hierarchies = SiteHierarchies(data_source.site_hierarchies)
    for path in hierarchies.all_path_levels:
        index_file = IndexFile(hierarchies, path, docs_dir)
        index_file.markdown_content.add_front_matter_property(
            'bookCollapseSection', 'true')
        index_file.markdown_content.save()


def create_formula_pages():
    """Creates the formula pages"""
    data_source = DataSource()
    site_hierarchies = SiteHierarchies(data_source.site_hierarchies)
    formulas_by_year = Formulas(data_source.formulas_by_year)
    formulas_cumulative = Formulas(data_source.formulas_by_year_cumulative)
    formulas_cumulative.is_cumulative = True
    formulas_all = [formulas_by_year, formulas_cumulative]

    table_summary_types = [FormulaTableTypeSimple,
                           FormulaTableTypeCalculus, FormulaTableTypeFinancial]

    for current_formulas, current_table_type in itertools.product(
            formulas_all, table_summary_types):
        if current_table_type == FormulaTableTypeSimple:
            group_by_cols = ['State', 'Subject', 'Category']
        else:
            group_by_cols = ['State', 'Subject']
        _create_single_formula_page(table_type=current_table_type,
                                    group_by=group_by_cols,
                                    formulas=current_formulas,
                                    base_dir=data_source.docs_directory,
                                    hierarchies=site_hierarchies)


def _create_single_formula_page(table_type: FormulaTableType,
                                group_by: list,
                                formulas: Formulas,
                                base_dir: str,
                                hierarchies: SiteHierarchies):
    """Creates formula pages"""

    for formula_group in formulas.group_by_columns(group_by):
        formula_table = FormulaTable(formula_group)
        formula_table.type = table_type
        if formula_table.contains_content:
            formula_file = FormulaFile(hierarchies, base_dir,
                                       formulas.is_cumulative, formula_table)
            formula_file.markdown_content.save()


if __name__ == '__main__':
    create_directory_structure()
    create_index_files()
    create_formula_pages()
