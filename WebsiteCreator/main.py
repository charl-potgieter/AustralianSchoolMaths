from website import WebSite
from data_sources import DataSource
from formulas import Formulas, FormulaTableSimple


def append_simple_formula_tables_to_notes(
    formulas: Formulas, maths_website: WebSite
):
    for state, topic in formulas.unique_state_and_topic_codes:
        formulas_by_state_topic = formulas.per_state_and_topic_code(
            state, topic
        )
        web_page = maths_website.get_web_page_by_state_and_topic_code(
            state, topic
        )
        if web_page:
            print("Adding formulas to " + topic + "\n")
            table = FormulaTableSimple(formulas_by_state_topic)
            web_page.append_content(table.to_html())
        else:
            # TODO: Change below to error handling once all web pages are
            # created
            print(
                "note: no web page exists for "
                + state
                + " "
                + topic
                + ".There are formulas recorded against this syllabus code"
            )


if __name__ == "__main__":
    data_source = DataSource()
    formulas_by_year = Formulas(data_source.formulas_by_year)
    maths_website = WebSite()
    maths_website.delete_content()
    maths_website.copy_provisional_notes_to_web_pages()
    append_simple_formula_tables_to_notes(formulas_by_year, maths_website)

    formulas_temp = formulas_by_year.per_state_and_topic_code("NSW", "MA-C4")
    print(formulas_temp.contains_data)

    # for state, topic in formulas_by_year.state_and_topic_codes:
    #     print(state + " " + topic)

    # for web_page in maths_website.web_pages:
    #     if web_page.state and web_page.topic_code:
    #         print(web_page.state + " " + web_page.topic_code)

# import os
# import shutil
# import typin
# from data_sources import DataSource
# from file_management import (
#     SiteHierarchies,
#     IndexFiles,
#     FormulaFiles,
#     TopicFiles,
# )
# from site_content import Formulas, Syllabus, Notes
#
#
# def get_data() -> typing.Dict[str, typing.Any]:
#     """Reads and returns various reequired data objects as a dictionary"""
#     data_source = DataSource()
#     docs_dir = data_source.docs_directory
#     hierarchies = SiteHierarchies(data_source.site_hierarchies)
#
#     notes_by_year = Notes(data_source.notes_by_year)
#     notes_cumulative = Notes(data_source.notes_by_year_cumulative)
#     notes_cumulative.is_cumulative = True
#
#     formulas_by_year = Formulas(data_source.formulas_by_year)
#     formulas_cumulative = Formulas(data_source.formulas_by_year_cumulative)
#     formulas_cumulative.is_cumulative = True
#
#     syllabus_by_year = Syllabus(data_source.syllabus_by_year)
#     syllabus_cumulative = Syllabus(data_source.syllabus_by_year_cumulative)
#     syllabus_cumulative.is_cumulative = True
#
#     return {
#         "docs_dir": docs_dir,
#         "hierarchies": hierarchie,
#         "notes_by_year": notes_by_year,
#         "notes_cumulative": notes_cumulative,
#         "formulas_by_year": formulas_by_year,
#         "formulas_cumulative": formulas_cumulative,
#         "syllabus_by_year": syllabus_by_year,
#         "syllabus_cumulative": syllabus_cumulative,
#     }
#
#
# def create_directory_structure(
#     docs_dir: str, hierarchies: SiteHierarchies
# ) -> None:
#     _delete_directory_if_it_exists(docs_dir)
#     hierarchies.create_directories(docs_dir)
#
#
# def _delete_directory_if_it_exists(dir_to_delete: str) -> None:
#     if os.path.isdir(dir_to_delete):
#         shutil.rmtree(path=dir_to_delete)
#
#
# def create_index_files(docs_dir: str, hierarchies: SiteHierarchies) -> None:
#     """Recursively create _index.md file at each level of hieararchies"""
#     index_files = IndexFiles(docs_dir, hierarchies)
#     for index_file in index_files.iterate():
#         index_file.save()
#
#
# def create_formula_pages(
#     docs_dir: str, hierarchies: SiteHierarchies, formulas: Formulas
# ) -> None:
#     formula_files = FormulaFiles(docs_dir, hierarchies, formulas)
#     for formula_file in formula_files.iterate():
#         formula_file.save()
#
#
# def create_topic_pages(
#     docs_dir: str,
#     hierarchies: SiteHierarchies,
#     syllabus: Syllabus,
#     notes: Notes,
#     formulas: Formulas,
# ) -> None:
#     topic_files = TopicFiles(syllabus, hierarchies, notes, formulas, docs_dir)
#     for topic_file in topic_files.iterate():
#         topic_file.save()
#
#
# if __name__ == "__main__":
#     input_data = get_data()
#
#     print("creating directory structure...")
#     create_directory_structure(
#         input_data["docs_dir"], input_data["hierarchies"]
#     )
#
#     print("creating index files...")
#     create_index_files(input_data["docs_dir"], input_data["hierarchies"])
#
#     print("creating formulas by year pages...")
#     create_formula_pages(
#         input_data["docs_dir"],
#         input_data["hierarchies"],
#         input_data["formulas_by_year"],
#     )
#
#     print("creating formulas cumulative pages...")
#     create_formula_pages(
#         input_data["docs_dir"],
#         input_data["hierarchies"],
#         input_data["formulas_cumulative"],
#     )
#
#     print("creating topics by year pages...")
#     create_topic_pages(
#         input_data["docs_dir"],
#         input_data["hierarchies"],
#         input_data["syllabus_by_year"],
#         input_data["notes_by_year"],
#         input_data["formulas_by_year"],
#     )
#
#     print("creating topics cumulative pages...")
#     create_topic_pages(
#         input_data["docs_dir"],
#         input_data["hierarchies"],
#         input_data["syllabus_cumulative"],
#         input_data["notes_cumulative"],
#         input_data["formulas_cumulative"],
#     )
