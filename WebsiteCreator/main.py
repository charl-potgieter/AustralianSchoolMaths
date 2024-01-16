# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import os
import shutil
import typing
from data_sources import DataSource
from file_management import (SiteHierarchies, IndexFiles,  FormulaFiles,
                             TopicFiles)
from site_content import Formulas, Syllabus, Notes, Spreadsheets


def get_data() -> typing.Dict[str, typing.Any]:
    """Reads and returns various reequired data objects as a dictionary"""
    data_source = DataSource()
    docs_dir = data_source.docs_directory
    hierarchies = SiteHierarchies(data_source.site_hierarchies)

    notes_by_year = Notes(data_source.notes_by_year)
    notes_cumulative = Notes(
        data_source.notes_by_year_cumulative)
    notes_cumulative.is_cumulative = True

    formulas_by_year = Formulas(data_source.formulas_by_year)
    formulas_cumulative = Formulas(data_source.formulas_by_year_cumulative)
    formulas_cumulative.is_cumulative = True

    syllabus_by_year = Syllabus(data_source.syllabus_by_year)
    syllabus_cumulative = Syllabus(data_source.syllabus_by_year_cumulative)
    syllabus_cumulative.is_cumulative = True

    spreadsheets_by_year = Spreadsheets(data_source.spreadsheets_by_year)
    spreadsheets_cumulative = Spreadsheets(
        data_source.spreadsheets_by_year_cumulative)
    spreadsheets_cumulative.is_cumulative = True

    return {'docs_dir': docs_dir,
            'hierarchies': hierarchies,
            'notes_by_year': notes_by_year,
            'notes_cumulative': notes_cumulative,
            'formulas_by_year': formulas_by_year,
            'formulas_cumulative': formulas_cumulative,
            'spreadsheets_by_year': spreadsheets_by_year,
            'spreadsheets_cumulative': spreadsheets_cumulative,
            'syllabus_by_year': syllabus_by_year,
            'syllabus_cumulative': syllabus_cumulative
            }


def create_directory_structure(docs_dir: str,
                               hierarchies: SiteHierarchies) -> None:
    _delete_directory_if_it_exists(docs_dir)
    hierarchies.create_directories(docs_dir)


def _delete_directory_if_it_exists(dir_to_delete: str) -> None:
    if os.path.isdir(dir_to_delete):
        shutil.rmtree(path=dir_to_delete)


def create_index_files(docs_dir: str, hierarchies: SiteHierarchies) -> None:
    """Recursively create _index.md file at each level of hieararchies"""
    index_files = IndexFiles(docs_dir, hierarchies)
    for index_file in index_files.iterate():
        index_file.save()


def create_formula_pages(docs_dir: str, hierarchies: SiteHierarchies,
                         formulas: Formulas) -> None:
    formula_files = FormulaFiles(docs_dir, hierarchies, formulas)
    for formula_file in formula_files.iterate():
        formula_file.save()


def create_topic_pages(docs_dir: str, hierarchies: SiteHierarchies,
                       syllabus: Syllabus,
                       notes: Notes, formulas: Formulas,
                       spreadsheets: Spreadsheets) -> None:
    topic_files = TopicFiles(syllabus, hierarchies, notes,
                             formulas, spreadsheets, docs_dir)
    for topic_file in topic_files.iterate():
        topic_file.save()


if __name__ == '__main__':
    input_data = get_data()

    print('creating directory strucutre...')
    create_directory_structure(input_data['docs_dir'],
                               input_data['hierarchies'])

    print('creating index files...')
    create_index_files(input_data['docs_dir'],
                       input_data['hierarchies'])

    print('creating formulas by year pages...')
    create_formula_pages(input_data['docs_dir'],
                         input_data['hierarchies'],
                         input_data['formulas_by_year'])

    print('creating formulas cumulative pages...')
    create_formula_pages(input_data['docs_dir'],
                         input_data['hierarchies'],
                         input_data['formulas_cumulative'])

    print('creating topics by year pages...')
    create_topic_pages(input_data['docs_dir'],
                       input_data['hierarchies'],
                       input_data['syllabus_by_year'],
                       input_data['notes_by_year'],
                       input_data['formulas_by_year'],
                       input_data['spreadsheets_by_year'])

    print('creating topics cumulative pages...')
    create_topic_pages(input_data['docs_dir'],
                       input_data['hierarchies'],
                       input_data['syllabus_cumulative'],
                       input_data['notes_cumulative'],
                       input_data['formulas_cumulative'],
                       input_data['spreadsheets_cumulative'])
