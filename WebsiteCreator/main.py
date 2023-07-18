"""Main module for generating markdown files to be utilised for Hugo site
generation.
"""

import os
import pandas as pd
import formulas
import utilities
import topics


if __name__ == '__main__':
    """Entry point to the maths site generation
    """
    # Get inputs
    website_creator_dir = os.path.dirname(__file__)
    docs_dir = utilities.get_docs_path(website_creator_dir)
    formula_file_path = website_creator_dir + os.path.sep + 'formulas.csv'
    order_file_path = website_creator_dir + os.path.sep + 'sort_orders.csv'
    syllabus_file_path = (website_creator_dir + os.path.sep +
                          'syllabus_topics.csv')
    sort_orders_df = pd.read_csv(order_file_path)
    syllabus_df = pd.read_csv(syllabus_file_path)
    formulas_input_df = pd.read_csv(formula_file_path)
    formula_sheet_items = (
        formulas.get_formulas_on_formula_sheet(formulas_input_df))
    formula_proof_required_items = (
        formulas.get_formulas_where_proofs_required(formulas_input_df))

    utilities.delete_directory_if_it_exists(docs_dir)

    # Create formula-related markdown documents
    formulas_df = formulas.get_formulas_df(formulas_input_df, syllabus_df,
                                           sort_orders_df)
    formulas.create_formulas_content(
        formulas_df, formula_sheet_items, formula_proof_required_items,
        sort_orders_df, docs_dir)
    formulas.create_calculus_summary_files(
        formulas_df, formula_sheet_items, formula_proof_required_items,
        sort_orders_df, docs_dir)
    formulas.create_financial_summary(
        formulas_df, formula_sheet_items, formula_proof_required_items,
        sort_orders_df, docs_dir)

    # Generate topic pages
    formulas_by_topic_df = formulas.get_formulas_by_topic_df(
        formulas_input_df, syllabus_df)

    topics.create_topic_content(formulas_by_topic_df, formula_sheet_items,
                                formula_proof_required_items, sort_orders_df,
                                docs_dir)
