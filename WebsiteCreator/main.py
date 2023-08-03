"""Main module for generating markdown files to be utilised for Hugo site
generation.
"""

from maths_objects import (SiteHierarchies, DataSource,
                           IndexFile,  FormulaFile, HierarchyPaths,
                           Formulas, FormulaTable, FormulaTableTypeSimple,
                           FormulaTableTypeCalculus)
import utilities


def create_index_files(hierarchies, base_dir):
    """Recursively create _index.md file at each level of hieararchies

    Args:
        hierarchies (DirectoryHierarhies): Directory structure where
            _index.md files will be created prefixed by base_dir
        base_dir (string) : Start of direcctory for file saving
    """
    for path in hierarchies.all_path_levels():
        index_file = IndexFile(path)
        index_file.add_front_matter_property('bookCollapseSection', 'true')
        index_file.set_weight_based_on_hierarchies(hierarchies)
        index_file.save(base_dir)


def create_formula_pages(hierarchies, formulas, base_dir,
                         is_cumulative=False):
    """Creates 'simple' formulas pages per state, subjecta and category.
    Excludes the more complex 'formula summary' pages for example calcululs
    """

    for formula_group in formulas.group_by_columns(['State', 'Subject',
                                                    'Category']):
        formula_table = FormulaTable(formula_group)
        formula_table.set_type(FormulaTableTypeSimple)
        if formula_table.contains_content():
            hierarchy_paths = HierarchyPaths()
            path_in_hierarchy = hierarchy_paths.simple_formula_table(
                formula_group, is_cumulative)
            formula_file = FormulaFile(path_in_hierarchy)
            formula_file.set_weight_based_on_hierarchies(hierarchies)
            formula_file.add_formula_table(formula_table)
            formula_file.save(base_dir)


if __name__ == '__main__':

    data_source = DataSource()
    site_hierarchies = SiteHierarchies(data_source.site_hierarchies)

    # Delete previous directories and create new ones with .index.md files
    docs_dir = data_source.docs_directory
    utilities.delete_directory_if_it_exists(docs_dir)
    site_hierarchies.create_directories(docs_dir)
    create_index_files(site_hierarchies, docs_dir)

    # Create formula pages
    formulas_by_year = Formulas(data_source.formulas_by_year)
    create_formula_pages(site_hierarchies, formulas_by_year,
                         docs_dir)
    formulas_cumulative = Formulas(data_source.formulas_by_year_cumulative)
    create_formula_pages(site_hierarchies,
                         formulas_cumulative, docs_dir,
                         is_cumulative=True)
