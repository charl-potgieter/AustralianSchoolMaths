# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import os
import pandas as pd
from traitlets.config import Config
from nbconvert.exporters import MarkdownExporter
from nbconvert.preprocessors import TagRemovePreprocessor

class DataSource():

    def _jupyter_notebook_to_markdown(
        self,
        input_file_path:str,
        exclude_tags:list[str]|None = None,
        exclude_input_tags:list[str]|None = None)->str:

        # code adapted from here:
        # https://nbconvert.readthedocs.io/en/latest/removing_cells.html

        if not exclude_tags:
            exclude_tags=[]
        if not exclude_input_tags:
            exclude_input_tags=[]

        c = Config()
        c.TagRemovePreprocessor.remove_cell_tags = exclude_tags
        c.TagRemovePreprocessor.remove_input_tags = exclude_input_tags
        c.TagRemovePreprocessor.enabled = True

        # Not sure why below 3 steps are needed but are included in official docs
        # so have left this in place
        c.MarkdownExporter.preprocessors = (
            ["nbconvert.preprocessors.TagRemovePreprocessor"])
        exporter = MarkdownExporter(config=c)
        exporter.register_preprocessor(TagRemovePreprocessor(config=c), True)

        output = MarkdownExporter(config=c).from_filename(input_file_path)

        return output[0]


    @property
    def website_creator_directory(self) -> str:
        """Returns the directory containing various code utilised to
        generate content in order to create the hugo website"""
        this_file_path = os.path.dirname(__file__)
        return this_file_path

    @property
    def docs_directory(self) -> str:
        """Returns the docs directory containinng content of Hugo website"""
        this_file_path = os.path.dirname(__file__)
        return (os.path.join(
            os.path.dirname(this_file_path),
            'content', 'docs'))

    @property
    def static_images_directory(self) -> str:
        """Returns the docs directory containinng content of Hugo website"""
        this_file_path = os.path.dirname(__file__)
        return (os.path.join(
            os.path.dirname(this_file_path),
            'static', 'images'))

    @property
    def spreadsheets_directory(self) -> str:
        """Returns directory containing spreadsheets to be included as
        links on web pages"""
        return (self.website_creator_directory + os.path.sep
                + 'spreadsheets')

    @property
    def hierarchies_file_path(self) -> str:
        return (self.website_creator_directory
                + os.path.sep
                + 'data_files'
                + os.path.sep
                + 'site_hierarchy.csv')

    @property
    def formulas_file_path(self) -> str:
        return (self.website_creator_directory + os.path.sep
                + 'data_files'
                + os.path.sep
                + 'formulas.csv')

    @property
    def definitions_file_path(self) -> str:
        return (self.website_creator_directory + os.path.sep
                + 'data_files'
                + os.path.sep
                + 'definitions.csv')

    @property
    def notes_folder_path(self) -> str:
        return (self.website_creator_directory + os.path.sep
                + 'data_files_notes')

    @property
    def syllabus_file_path(self) -> str:
        return (self.website_creator_directory + os.path.sep
                + 'data_files'
                + os.path.sep
                + 'syllabus_topics.csv')

    @property
    def spreadhsheet_inventory_file_path(self) -> str:
        return (self.website_creator_directory + os.path.sep
                + 'data_files'
                + os.path.sep
                + 'spreadsheet_inventory.csv')

    @property
    def subject_dependencies_file_path(self) -> str:
        return (self.website_creator_directory + os.path.sep
                + 'data_files'
                + os.path.sep
                + 'subject_dependencies.csv')

    @property
    def syllabus_by_year(self) -> pd.DataFrame:
        return pd.read_csv(self.syllabus_file_path)

    @property
    def syllabus_by_year_cumulative(self) -> pd.DataFrame:
        """Returns syllabus details dataframe on a cumulative level by subject
        order  for a given state.  (includes the current subject syllabus
        as well as the syllabus from a subjects dependencies)
        """
        return_value = self.syllabus_by_year.copy()
        return_value = return_value.rename(columns={'Subject': 'Dependency'})
        return_value = return_value.merge(
            right=self.subject_dependencies,
            left_on=['State', 'Dependency'],
            right_on=['State', 'Dependency'])
        return_value = return_value.drop('Dependency', axis='columns')
        # Re-order cols
        return_value = return_value[['State', 'Subject', 'Syllabus_topic',
                                     'Syllabus_subtopic_code',
                                     'Syllabus_subtopic']]
        return return_value

    @property
    def _state_subtopic_codes(self)->list[str]:
        state_subtopic = list(
            self.syllabus_by_year['State'] + "|" +
            self.syllabus_by_year['Syllabus_subtopic_code'])
        return state_subtopic

    @property
    def subject_dependencies(self) -> pd.DataFrame:
        """Returns the subject dependencies (subjects which have assumed
        knowledge for given subject)
        """
        return pd.read_csv(self.subject_dependencies_file_path)

    @property
    def site_hierarchies(self) -> pd.DataFrame:
        return pd.read_csv(self.hierarchies_file_path)

    @property
    def formulas_by_year(self) -> pd.DataFrame:
        # TODO Temporarily mark empty boolean fields as false to avoid type errors
        # Remove once all data capture is complete
        formulas_input_converter = {
            'Proof_required': lambda x: True if x else False}
        formulas_ex_syllabus = pd.read_csv(
            filepath_or_buffer=self.formulas_file_path,
            converters=formulas_input_converter)
        formulas = pd.merge(
            left=self.syllabus_by_year, right=formulas_ex_syllabus,
            left_on=['State', 'Syllabus_subtopic_code'],
            right_on=['State', 'Syllabus_subtopic_code'],
            how='right')
        return formulas

    @property
    def formulas_by_year_cumulative(self) -> pd.DataFrame:
        """Returns formula details on a cumulative level by subject
        order  for a given state.  (includes the current subjects formulas
        as well as the formulas from a subjects dependencies)
        """
        return_value = self.formulas_by_year.copy()
        return_value = return_value.rename(columns={'Subject': 'Dependency'})
        return_value = return_value.merge(
            right=self.subject_dependencies,
            left_on=['State', 'Dependency'],
            right_on=['State', 'Dependency'])
        return_value = return_value.drop('Dependency', axis='columns')
        # Re-order cols
        return_value = return_value[['State', 'Subject', 'Syllabus_topic',
                                     'Syllabus_subtopic_code',
                                     'Syllabus_subtopic', 'Category',
                                     'Subcategory_1', 'Subcategory_2',
                                     'Description', 'Group', 'Formula',
                                     'On_formula_sheet', 'Proof_required',
                                     'Comment', ]]
        return return_value

    @property
    def definitions_by_year(self) -> pd.DataFrame:
        definitions_data = pd.read_csv(self.definitions_file_path)

        definitions_data = pd.merge(
            left=self.syllabus_by_year, right=definitions_data,
            left_on=['State', 'Syllabus_subtopic_code'],
            right_on=['State', 'Syllabus_subtopic_code'],
            how='right')
        return definitions_data

    @property
    def definitions_by_year_cumulative(self) -> pd.DataFrame:
        """Returns definition details on a cumulative level by subject
        order  for a given state.  (includes the current subjects definitions
        as well as the definitions from a subjects dependencies)
        """
        return_value = self.definitions_by_year.copy()
        return_value = return_value.rename(columns={'Subject': 'Dependency'})
        return_value = return_value.merge(
            right=self.subject_dependencies,
            left_on=['State', 'Dependency'],
            right_on=['State', 'Dependency'])
        return_value = return_value.drop('Dependency', axis='columns')
        # Re-order cols
        return_value = return_value[['State', 'Subject', 'Syllabus_topic',
                                     'Syllabus_subtopic_code',
                                     'Syllabus_subtopic', 'Term',
                                     'Definition']]
        return return_value

    @property
    def  notes_by_year(self) -> pd.DataFrame:
        notes_data = pd.read_csv(self.notes_file_path)

        notes_data = pd.merge(
            left=self.syllabus_by_year, right=notes_data,
            left_on=['State', 'Syllabus_subtopic_code'],
            right_on=['State', 'Syllabus_subtopic_code'],
            how='right')
        return notes_data

    @property
    def notes_by_year_cumulative(self) -> pd.DataFrame:
        """Returns note details on a cumulative level by subject
        order  for a given state.  (includes the current subjects notes
        as well as the notes from a subjects dependencies)
        """
        return_value = self.notes_by_year.copy()
        return_value = return_value.rename(columns={'Subject': 'Dependency'})
        return_value = return_value.merge(
            right=self.subject_dependencies,
            left_on=['State', 'Dependency'],
            right_on=['State', 'Dependency'])
        return_value = return_value.drop('Dependency', axis='columns')
        # Re-order cols
        return_value = return_value[['State', 'Subject', 'Syllabus_topic',
                                     'Syllabus_subtopic_code',
                                     'Syllabus_subtopic', 'Note']]
        return return_value

    @property
    def spreadsheets_by_year(self) -> pd.DataFrame:
        spreadsheets_data = pd.read_csv(self.spreadhsheet_inventory_file_path)

        spreadsheets_data = pd.merge(
            left=self.syllabus_by_year, right=spreadsheets_data,
            left_on=['State', 'Syllabus_subtopic_code'],
            right_on=['State', 'Syllabus_subtopic_code'],
            how='right')
        return spreadsheets_data

    @property
    def spreadsheets_by_year_cumulative(self) -> pd.DataFrame:
        """Returns definition details on a cumulative level by subject
        order  for a given state.  (includes the current subjects definitions
        as well as the definitions from a subjects dependencies)
        """
        return_value = self.spreadsheets_by_year.copy()
        return_value = return_value.rename(columns={'Subject': 'Dependency'})
        return_value = return_value.merge(
            right=self.subject_dependencies,
            left_on=['State', 'Dependency'],
            right_on=['State', 'Dependency'])
        return_value = return_value.drop('Dependency', axis='columns')
        # Re-order cols
        return_value = return_value[['State', 'Subject', 'Syllabus_topic',
                                     'Syllabus_subtopic_code',
                                     'Syllabus_subtopic', 'Spreadsheet']]

        return return_value
