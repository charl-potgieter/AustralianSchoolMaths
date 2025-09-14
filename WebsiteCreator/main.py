from website import WebSite
from data_sources import DataSource
from formulas import Formulas, TableType
from formatters import WebSiteFormatter, HugoWebSiteFormatter


def append_simple_formula_tables_to_notes(
    formulas: Formulas,
    site_formatter: WebSiteFormatter,
    maths_website: WebSite,
):
    table_type = TableType
    for state, topic in formulas.unique_state_and_topic_codes:
        selected_formulas = formulas.per_state_and_topic_code(state, topic)
        selected_web_page = maths_website.get_web_page_by_state_and_topic_code(
            state, topic
        )
        if selected_web_page:
            print("Adding formulas to " + topic + "\n")
            selected_web_page.append_content(
                "\n"
                + "### Formulas\n"
                + selected_formulas.to_formula_display(
                    table_type.SIMPLE, site_formatter
                )
            )
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

    site_formatter = HugoWebSiteFormatter()
    append_simple_formula_tables_to_notes(
        formulas_by_year, site_formatter, maths_website
    )
