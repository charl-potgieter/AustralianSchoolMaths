# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import os
from site_hierarchies import SiteHierarchies
from formula_tables import FormulaTable


class _MarkdownContent():
    """Markdown file content utilised for creation of Hugo webiite
    """

    def __init__(self, hierarchies: SiteHierarchies, path_in_hierarchy: str,
                 file_path: str):
        self._content = ''
        self._front_matter = FrontMatter()
        self._hierarchies = hierarchies
        self._path_in_hierarchy = path_in_hierarchy
        self._file_path = file_path
        self._set_weight_based_on_hierarchies()

    def add_front_matter_property(self, property_key: str | float,
                                  property_value: str | float) -> None:
        self._front_matter.add_property(property_key, property_value)

    def add_content(self, content: str) -> None:
        if self._content:
            self._content += ('\n\n' + content)
        else:
            self._content = content

    def _set_weight_based_on_hierarchies(self) -> None:
        """Adds weight property to front matter based on position of
        path in hierarchy"""
        weight = self._hierarchies.get_sort_index_in_parent_path(
            self._path_in_hierarchy) + 1
        self.add_front_matter_property('weight', weight)

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

    def __init__(self, hierarchies: SiteHierarchies, path_in_hierarchy: str,
                 base_path: str):
        file_path = self._get_file_path(base_path, path_in_hierarchy)
        self._markdown_content = _MarkdownContent(hierarchies,
                                                  path_in_hierarchy,
                                                  file_path)

    def _get_file_path(self, base_dir, path_in_hierarchy):
        """returns file path"""
        return (
            base_dir + os.path.sep
            + path_in_hierarchy + os.path.sep
            + '_index.md')

    @property
    def markdown_content(self) -> _MarkdownContent:
        """Returns the markdown_content object"""
        return self._markdown_content


class FormulaFile():
    """..md file containing formula tables for Hugo site generation"""

    def __init__(self, hierarchies: SiteHierarchies, base_path: str,
                 is_cumulative_by_year: bool, formula_table: FormulaTable):
        path_in_hierarchy = self._get_path_in_hierarchy(formula_table,
                                                        is_cumulative_by_year)
        file_path = self._get_file_path(base_path, path_in_hierarchy)
        self._markdown_content = _MarkdownContent(hierarchies,
                                                  path_in_hierarchy,
                                                  file_path)
        self.markdown_content.add_content(formula_table.to_markdown())

    def _get_file_path(self, base_dir: str, path_in_hierarchy: str) -> str:
        return base_dir + os.path.sep + path_in_hierarchy + '.md'

    @property
    def markdown_content(self) -> _MarkdownContent:
        return self._markdown_content

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
            formula_table.table_type.display_name])


class TopicFile():
    """..md file containing topic for Hugo site generation"""

    def __init__(self, state: str, subject: str, syllabus_topic: str,
                 hierarchies: SiteHierarchies, base_path: str,
                 is_cumulative_by_year: bool):
        path_in_hierarchy = self._get_path_in_hierarchy(
            is_cumulative_by_year, state, subject, syllabus_topic)
        file_path = self._get_file_path(base_path, path_in_hierarchy)
        self._markdown_content = _MarkdownContent(hierarchies,
                                                  path_in_hierarchy,
                                                  file_path)

    def _get_file_path(self, base_dir: str, path_in_hierarchy: str) -> str:
        return base_dir + os.path.sep + path_in_hierarchy + '.md'

    @property
    def markdown_content(self) -> _MarkdownContent:
        return self._markdown_content

    def add_text(self, input_text: str) -> None:
        self._markdown_content.add_content(input_text)

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
