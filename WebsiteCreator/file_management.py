# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import os
from site_hierarchies import SiteHierarchies
from formula_tables import (FormulaTable, FormulaTableType,
                            FormulaTableTypeSimple, formula_table_types)
from definition_display import DefinitionDisplay
from note_display import NoteDisplay
from site_content import Syllabus, Formulas, SyllabusTopic, Definitions, Notes


class _MarkdownContent():
    """Markdown file content utilised for creation of Hugo webiite
    """

    def __init__(self, file_path: str, weight: int):
        self._content = ''
        self._front_matter = FrontMatter()
        self._file_path = file_path
        self.add_front_matter_property('weight', weight)

    def add_front_matter_property(self, property_key: str | float,
                                  property_value: str | float) -> None:
        self._front_matter.add_property(property_key, property_value)

    def add_content(self, content: str) -> None:
        if self._content:
            self._content += ('\n\n' + content)
        else:
            self._content = content

    def _add_front_matter_to_content(self) -> None:
        if self._content:
            self._content = (self._front_matter.to_string()
                             + '\n\n' + self._content)
        else:
            self._content = self._front_matter.to_string()

    def save(self) -> None:
        """Saves the content of this object at file_path."""
        self._add_front_matter_to_content()
        if os.path.isfile(self._file_path):
            raise OSError('Cannot create ' + self._file_path + ' as it already ' +
                          'exists')
        else:
            with open(self._file_path, "w", encoding="utf-8") as text_file:
                text_file.write(self._content)


class IndexFile():
    """._index.md file utilised for Hugo site generation"""

    def __init__(self, file_path: str, weight: int):
        self._markdown_content = _MarkdownContent(file_path, weight)
        self._markdown_content.add_front_matter_property(
            'bookCollapseSection', 'true')

    def save(self) -> None:
        """Returns the markdown_content object"""
        return self._markdown_content.save()


class IndexFiles():

    def __init__(self, base_path: str, hierarchies: SiteHierarchies) -> None:
        self._base_path = base_path
        self._hierarchies = hierarchies

    def iterate(self):
        for path in self._hierarchies.all_path_levels:
            weight = self._get_weight_based_on_hierarchies(path)
            file_path = self._get_file_path(self._base_path, path)
            index_file = IndexFile(file_path, weight)
            yield index_file

    def _get_weight_based_on_hierarchies(self, path: str) -> int:
        weight = self._hierarchies.get_sort_index_in_parent_path(
            path) + 1
        return weight

    def _get_file_path(self, base_dir, path_in_hierarchy):
        """returns file path"""
        return (
            base_dir + os.path.sep
            + path_in_hierarchy + os.path.sep
            + '_index.md')


class FormulaFile():
    """..md file containing formula tables for Hugo site generation"""

    def __init__(self, file_path: str, weight: int,
                 formula_table: FormulaTable):
        self._markdown_content = _MarkdownContent(file_path, weight)
        self._markdown_content.add_content(formula_table.to_markdown())

    def save(self):
        self._markdown_content.save()


class FormulaFiles():

    def __init__(self, base_path: str, hierarchies: SiteHierarchies,
                 formulas: Formulas) -> None:
        self._base_path = base_path
        self._hierarchies = hierarchies
        self._formulas = formulas

    def iterate(self):
        for current_table_type in formula_table_types:
            group_by_cols = self._column_groups(current_table_type)
            for formula_group in self._formulas.group_by_columns(
                    group_by_cols):
                formula_table = FormulaTable(formula_group, current_table_type)
                if formula_table.contains_content:
                    path_in_hierarchy = self._get_path_in_hierarchy(
                        formula_table, formula_group.is_cumulative)
                    file_path = self._get_file_path(self._base_path,
                                                    path_in_hierarchy)
                    weight = self._get_weight_based_on_hierarchies(
                        path_in_hierarchy)
                    formula_file = FormulaFile(file_path, weight,
                                               formula_table)
                    yield formula_file

    def _column_groups(self, table_type: type[FormulaTableType]
                       ) -> list[str]:
        if table_type == FormulaTableTypeSimple:
            return ['State', 'Subject', 'Category']
        return ['State', 'Subject']

    def _get_file_path(self, base_dir: str, path_in_hierarchy: str) -> str:
        return base_dir + os.path.sep + path_in_hierarchy + '.md'

    def _get_path_in_hierarchy(self, formula_table: FormulaTable,
                               is_cumulative_by_year: bool) -> str:
        """Gets the path in hierarchy (excluding any base directory)"""
        if is_cumulative_by_year:
            time_frame_portion_of_path = 'By year cumulative'
        else:
            time_frame_portion_of_path = 'By year'
        return os.path.sep.join([
            formula_table.state,
            formula_table.subject,
            formula_table.table_type.content_type,
            time_frame_portion_of_path,
            formula_table.table_type.formula_menu_display_name])

    def _get_weight_based_on_hierarchies(self, path: str) -> int:
        weight = self._hierarchies.get_sort_index_in_parent_path(
            path) + 1
        return weight


class TopicFile():
    """..md file containing topic for Hugo site generation"""

    def __init__(self,
                 syllabus_topic: SyllabusTopic,
                 file_path,
                 weight,
                 definitions: Definitions,
                 notes: Notes,
                 formulas: Formulas):
        self._syllabus_topic = syllabus_topic
        self._definitions = definitions
        self._notes = notes
        self._formulas = formulas
        self._markdown_content = _MarkdownContent(file_path, weight)
        self._generate_file()

    def save(self) -> None:
        self._markdown_content.save()

    def _generate_file(self):
        for subtopic in self._syllabus_topic.subtopics:
            self._add_subtopic_heading(subtopic)
            definitions_by_subtopic = self._defintions_by_subtopic(subtopic)
            notes_by_subtopic = self._notes_by_subtopic(subtopic)
            formulas_by_subtopic = self._formulas_by_subtopic(subtopic)
            self._add_definitions(definitions_by_subtopic)
            self._add_notes(notes_by_subtopic)
            self._add_formula_tables(formulas_by_subtopic)

    def _formulas_by_subtopic(self, subtopic):
        return self._formulas.filter_by_dict({
            'Syllabus_subtopic': subtopic})

    def _defintions_by_subtopic(self, subtopic):
        return self._definitions.filter_by_dict({
            'Syllabus_subtopic': subtopic})

    def _notes_by_subtopic(self, subtopic):
        return self._notes.filter_by_dict({
            'Syllabus_subtopic': subtopic})

    def _add_subtopic_heading(self, subtopic: str) -> None:
        self._markdown_content.add_content(
            '## <span style="color:RGB(0,32,96"> ' +
            subtopic + ' </span> \n<br>'
        )

    def _add_definitions(self, definitions_by_subtopic: Definitions) -> None:
        if len(definitions_by_subtopic.data):
            definition_display = DefinitionDisplay(definitions_by_subtopic)
            self._markdown_content.add_content(
                definition_display.to_markdown_with_heading())

    def _add_notes(self, notes_by_subtopic: Notes) -> None:
        if len(notes_by_subtopic.data):
            note_display = NoteDisplay(notes_by_subtopic)
            self._markdown_content.add_content(
                note_display.to_markdown_with_heading())

    def _add_formula_tables(self, formulas_by_subtopic: Formulas) -> None:
        for table_type in formula_table_types:
            formula_table = FormulaTable(formulas_by_subtopic,
                                         table_type)
            if formula_table.contains_content:
                self._markdown_content.add_content('\n<br>\n')
                self._markdown_content.add_content(
                    formula_table.to_markdown_with_heading())


class TopicFiles():

    def __init__(self,
                 syllabus: Syllabus,
                 hierarchies: SiteHierarchies,
                 definitions: Definitions,
                 notes: Notes,
                 formulas: Formulas,
                 base_path: str):
        self._syllabus = syllabus
        self._hierarchies = hierarchies
        self._definitions = definitions
        self._notes = notes
        self._formulas = formulas
        self._base_path = base_path

    def iterate(self):
        for syllabus_topic in self._syllabus.topics():
            definitions_by_topic = self._definitions.filter_by_dict({
                'State': syllabus_topic.state,
                'Subject': syllabus_topic.subject,
                'Syllabus_topic': syllabus_topic.name
            })
            notes_by_topic = self._notes.filter_by_dict({
                'State': syllabus_topic.state,
                'Subject': syllabus_topic.subject,
                'Syllabus_topic': syllabus_topic.name
            })
            formulas_by_topic = self._formulas.filter_by_dict({
                'State': syllabus_topic.state,
                'Subject': syllabus_topic.subject,
                'Syllabus_topic': syllabus_topic.name
            })
            path_in_hierarchy = self._get_path_in_hierarchy(
                syllabus_topic.is_cumulative, syllabus_topic.state,
                syllabus_topic.subject, syllabus_topic.name)
            file_path = self._get_file_path(self._base_path, path_in_hierarchy)
            weight = self._get_weight_based_on_hierarchies(path_in_hierarchy)
            topic_file = TopicFile(syllabus_topic, file_path, weight,
                                   definitions_by_topic, notes_by_topic,
                                   formulas_by_topic)
            yield topic_file

    def _get_path_in_hierarchy(self, is_cumulative_by_year: bool, state: str,
                               subject: str, syllabus_topic: str) -> str:
        if is_cumulative_by_year:
            time_frame_portion_of_path = 'By year cumulative'
        else:
            time_frame_portion_of_path = 'By year'
        return os.path.sep.join([
            state,
            subject,
            'Topics',
            time_frame_portion_of_path,
            syllabus_topic])

    def _get_file_path(self, base_dir: str, path_in_hierarchy: str) -> str:
        return base_dir + os.path.sep + path_in_hierarchy + '.md'

    def _get_weight_based_on_hierarchies(self, path: str) -> int:
        weight = self._hierarchies.get_sort_index_in_parent_path(
            path) + 1
        return weight


class FrontMatter():
    """Front matter strings for markdown files utilised to generate Hugo
    webstites
    """

    def __init__(self):
        self._content = {}

    def add_property(self, property_key: str | float,
                     property_value: str | float) -> None:
        self._content[property_key] = property_value

    def to_string(self) -> str:
        return_value = '---\n'
        if self._content:
            for key, value in self._content.items():
                return_value += str(key) + ': ' + str(value) + '\n'
        return_value += '---'
        return return_value
