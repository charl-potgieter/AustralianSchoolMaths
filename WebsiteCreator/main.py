"""Main module for generating markdown files to be utilised for Hugo site
generation.
"""

import os
from maths_objects import Formulas, WebPageSortOrders
import utilities


if __name__ == '__main__':
    # Get inputs
    website_creator_dir = os.path.dirname(__file__)
    docs_dir = utilities.get_docs_path(website_creator_dir)
    formula_file_path = website_creator_dir + os.path.sep + 'formulas.csv'
    order_file_path = website_creator_dir + os.path.sep + 'sort_orders.csv'
    syllabus_file_path = (website_creator_dir + os.path.sep +
                          'syllabus_topics.csv')

    page_sort_orders = WebPageSortOrders(order_file_path)
    formulas = Formulas(formula_file_path, syllabus_file_path,
                        page_sort_orders)

    # Delete previous directories and create new ones
    utilities.delete_directory_if_it_exists(docs_dir)
    utilities.create_subdirectories_from_df(
        base_dir=docs_dir,
        subpaths_df=formulas.by_year_dirs()
    )
    utilities.create_subdirectories_from_df(
        base_dir=docs_dir,
        subpaths_df=formulas.by_year_cumulative_dirs()
    )
