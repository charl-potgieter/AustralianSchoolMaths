"""Module for generating topic related markdown files to be utilised for Hugo
site generation.
"""

import utilities
import formulas


def create_topic_content(formulas_by_topic_df, formula_sheet_items,
                         formula_proof_required_items, sort_orders_df,
                         docs_dir):
    """Creates markdown files containing topic summary for static
    web page creation via Hugo
    """
    dirs_df = formulas_by_topic_df[[
        'State', 'Topic subcategory 1', 'Subject code']].drop_duplicates()
    file_paths_df = formulas_by_topic_df[[
        'State', 'Topic subcategory 1', 'Subject code', 'Syllabus subtopic'
    ]].drop_duplicates()
    utilities.create_subdirectories_from_df(base_dir=docs_dir,
                                            subpaths_df=dirs_df)
    front_matter_index_files = {'bookCollapseSection': True}
    utilities.create_index_files(base_dir=docs_dir, dirs_df=dirs_df,
                                 front_matter=front_matter_index_files,
                                 sort_orders_df=sort_orders_df)
    utilities.create_files(base_dir=docs_dir, file_paths_df=file_paths_df,
                           file_extension='.md',
                           string_creator=generate_topic_page,
                           sort_orders_df=sort_orders_df,
                           formulas_df=formulas_by_topic_df,
                           formula_sheet_items=formula_sheet_items,
                           formula_proof_required_items=(
                               formula_proof_required_items),
                           cols_to_highlight=[
                               'Formula'])


def generate_topic_page(formulas_df, state, syllabus_subtopic,
                        subject_code, formula_sheet_items,
                        formula_proof_required_items,
                        cols_to_highlight, **kwargs):
    """TBA"""

    # kwargs only exist in the event they are passed by wrapper.  Ignore
    # https://stackoverflow.com/questions/13944234/how-to-suppress-unused-\variable-warnings-in-eclipse-pydev
    _ = kwargs

    formulas_df = formulas_df[
        (formulas_df['State'] == state) &
        (formulas_df['Syllabus subtopic'] == syllabus_subtopic) &
        (formulas_df['Subject code'] == subject_code)]
    formulas_df = formulas_df[['Formula']]
    formula_string = formulas.generate_formula_string(
        formulas_df,
        formula_sheet_items,
        formula_proof_required_items,
        cols_to_highlight)
    definitions_string = formulas.generate_definition_string()
    page_string = ('# ' + syllabus_subtopic + '\n\n<br>\n\n'
                   + '## Definitions' + '\n\n'
                   + definitions_string + '\n\n<br>\n\n'
                   + '## Formulas' + '\n\n'
                   + formula_string + '\n\n'
                   )

    return page_string
