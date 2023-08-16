# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import os
import shutil
import typing
from data_sources import DataSource
from file_management import (SiteHierarchies, IndexFile,  FormulaFile,
                             TopicFiles)
from formula_tables import (formula_table_types, FormulaTable,
                            FormulaTableTypeSimple, FormulaTableTypeCalculus,
                            FormulaTableTypeFinancial)
from site_content import Formulas, Syllabus


def get_data() -> typing.Dict[str, typing.Any]:
    """Reads and returns various reequired data objects as a dictionary"""
    data_source = DataSource()
    docs_dir = data_source.docs_directory
    hierarchies = SiteHierarchies(data_source.site_hierarchies)
    formulas_by_year = Formulas(data_source.formulas_by_year)
    formulas_cumulative = Formulas(data_source.formulas_by_year_cumulative)
    formulas_cumulative.is_cumulative = True
    syllabus_by_year = Syllabus(data_source.syllabus_by_year)
    syllabus_cumulative = Syllabus(data_source.syllabus_by_year_cumulative)
    syllabus_cumulative.is_cumulative = True
    return {'docs_dir': docs_dir,
            'hierarchies': hierarchies,
            'formulas_by_year': formulas_by_year,
            'formulas_cumulative': formulas_cumulative,
            'syllabus_by_year': syllabus_by_year,
            'syllabus_cumulative': syllabus_cumulative}


def create_directory_structure(docs_dir: str,
                               hierarchies: SiteHierarchies) -> None:
    _delete_directory_if_it_exists(docs_dir)
    hierarchies.create_directories(docs_dir)


def _delete_directory_if_it_exists(dir_to_delete: str) -> None:
    if os.path.isdir(dir_to_delete):
        shutil.rmtree(dir_to_delete)


def create_index_files(docs_dir: str, hierarchies: SiteHierarchies) -> None:
    """Recursively create _index.md file at each level of hieararchies"""
    for path in hierarchies.all_path_levels:
        index_file = IndexFile(hierarchies, path, docs_dir)
        index_file.markdown_content.add_front_matter_property(
            'bookCollapseSection', 'true')
        index_file.markdown_content.save()


def create_formula_pages(docs_dir: str, hierarchies: SiteHierarchies,
                         formulas: Formulas) -> None:

    for current_table_type in formula_table_types:
        if current_table_type == FormulaTableTypeSimple:
            group_by_cols = ['State', 'Subject', 'Category']
        else:
            group_by_cols = ['State', 'Subject']
        for formula_group in formulas.group_by_columns(group_by_cols):
            formula_table = FormulaTable(formula_group, current_table_type)
            if formula_table.contains_content:
                formula_file = FormulaFile(hierarchies, docs_dir,
                                           formulas.is_cumulative,
                                           formula_table)
                formula_file.markdown_content.save()


def create_topic_pages(docs_dir: str, hierarchies: SiteHierarchies,
                       syllabus: Syllabus, formulas: Formulas) -> None:
    topic_files = TopicFiles(syllabus, hierarchies, formulas, docs_dir)
    for topic_file in topic_files.iterate():
        topic_file.save()


if __name__ == '__main__':
    input_data = get_data()

    create_directory_structure(input_data['docs_dir'],
                               input_data['hierarchies'])

    # create_index_files(input_data['docs_dir'],
    #                    input_data['hierarchies'])

    # create_formula_pages(input_data['docs_dir'],
    #                      input_data['hierarchies'],
    #                      input_data['formulas_by_year'])

    # create_formula_pages(input_data['docs_dir'],
    #                      input_data['hierarchies'],
    #                      input_data['formulas_cumulative'])

    create_topic_pages(input_data['docs_dir'],
                       input_data['hierarchies'],
                       input_data['syllabus_by_year'],
                       input_data['formulas_by_year'])

    create_topic_pages(input_data['docs_dir'],
                       input_data['hierarchies'],
                       input_data['syllabus_cumulative'],
                       input_data['formulas_by_year'])
