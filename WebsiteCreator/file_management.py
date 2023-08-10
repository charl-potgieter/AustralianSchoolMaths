"""This Module contains classes relating to file management"""

import os
from WebsiteCreator.data_validator import DataColumnValidator


class SiteHierarchies():
    """Stores, retrieves, filters and creates file directory (path) hierarchies
       as well as their indexed sort orders
    """

    def __init__(self, input_data):
        """Initiates class with data content

        Args:
            data (Pandas dataframe): input data
        """
        data_to_load = DataColumnValidator(input_data)
        # Do not error check column names as they vary dependent on depth
        # of hierarchy being created
        self._hierarchy_data = data_to_load.to_dataframe()
        self._error_check_sort_orders()

    def _error_check_sort_orders(self):
        """"Error checks thge hierarchy sort orders"""
        if self._first_hierarchy_with_inconsistent_sort_order():
            raise ValueError(
                'Inconsistent site hieriarchy file.  '
                + 'Out of order item: '
                + str(self._first_hierarchy_with_inconsistent_sort_order()))

    def _first_hierarchy_with_inconsistent_sort_order(self):
        """Checks for sort consistency in hieriarchies.  Returns a string
        containing the first inconsistent sort path found, othewise None.
        Example: Below is inconsistent as all the Path_A in
        first levels of the hierarchies below are not consecutive
            /path_A/path_B
            /path_A/path_C
            /path_B/Path_X
            /path_A/Path_Y
        """
        for i in range(len(self._hierarchy_data.columns)):
            current_level_data = self._hierarchy_data.iloc[:, :i+1].copy()
            current_level_data_last_path = current_level_data.iloc[:, i]
            current_level_data = current_level_data[
                current_level_data_last_path.notnull()]
            ordered_paths = list(
                # https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unnecessary-lambda.html
                current_level_data.apply(list, axis=1))
            inconsistent_item = (
                self._first_non_consecutive_like_item(ordered_paths))
            if inconsistent_item:
                return inconsistent_item
        return None

    def _first_non_consecutive_like_item(self, input_values):
        """Returns first item if it is an item in input_values that equals
        another item in input_values but they do not appear consecutively,
        otherwise returns None.

        Args:
            input_values (iterable): Values to test
        """

        values_ex_consecutive_duplicates = []
        for item in input_values:
            if not values_ex_consecutive_duplicates:
                values_ex_consecutive_duplicates.append(item)
            elif item != values_ex_consecutive_duplicates[-1]:
                values_ex_consecutive_duplicates.append(item)
                if values_ex_consecutive_duplicates.count(item) != 1:
                    return item
        return None

    def copy(self):
        """Creates a copy of the this object
        """
        new_hierarchy_data = self._hierarchy_data.copy()
        return SiteHierarchies(new_hierarchy_data)

    def to_dataframe(self):
        """Returns the full set of hierarhcies as a pandas dataframe"""
        return self._hierarchy_data.copy()

    def filter_by_function(self, filter_function):
        """Returns a new filtered WebPagHierarchies object where
        filter_function returns True when passed each item in
        WebPageHierarchies as a pandas series.

        Args:
            filter_function (function): Function taking a pandas series as a
            parameter and returns a Boolean value
        """
        return_rows = self.to_dataframe().apply(filter_function, axis=1)
        return_data = self.to_dataframe().copy()[return_rows]
        return SiteHierarchies(return_data)

    def get_sort_index(self, dir_to_find):
        """Returns sort index of dir_to_find relative to all paths in the
            hierarchies stored in this object

        Args:
            dir_to_find (string): The directory (path) for which the sort
                index is to be returned
        """
        dir_paths = dir_to_find.split(os.path.sep)
        matching_hierarchies = self.filter_by_path(dir_paths)
        if len(matching_hierarchies.to_dataframe()):
            return matching_hierarchies.to_dataframe().index[0]
        raise ValueError(dir_to_find + ' not found in hierarchy')

    def get_sort_index_in_parent_path(self, dir_to_find):
        """Returns sort_index of dir_to_find relative to other directories
        with the same parent path

        Args:
            dir_to_find (string): the directory to find
        """
        dir_paths = dir_to_find.split(os.path.sep)
        unique_truncated_hierarchies = (
            self.truncate_to_path_length(len(dir_paths)).unique())
        if len(dir_paths) > 1:
            hierarchies_with_same_parent = (
                unique_truncated_hierarchies
                .filter_by_path_start(dir_paths[:-1]))
        else:
            hierarchies_with_same_parent = unique_truncated_hierarchies
        hierarchies_with_same_parent = (
            hierarchies_with_same_parent.reset_sort_index())
        return hierarchies_with_same_parent.get_sort_index(
            os.path.sep.join(dir_paths))

    def truncate_to_path_length(self, path_length):
        """Restricts  hieararches to paths of path_length and returns as a
        new object

        Args:
            path_length (int): The path length restriction to apply when
                creating the object copy.
        """
        hierarchy_data_to_length = self._hierarchy_data.iloc[
            :, :path_length].copy()
        hierarchies_to_length = SiteHierarchies(hierarchy_data_to_length)
        return hierarchies_to_length

    def unique(self):
        """Restricts hierarchies to unique values and returns as a new object
        """
        unique_hierarchy_data = self._hierarchy_data.copy()
        unique_hierarchy_data = unique_hierarchy_data.drop_duplicates()
        return SiteHierarchies(unique_hierarchy_data)

    def reset_sort_index(self):
        """Resets the hiearatchy sort order to commence from zero and return
        as a new object
        """
        return SiteHierarchies(
            self._hierarchy_data.copy().reset_index(drop=True))

    def filter_by_path(self, path_to_filter):
        """filters hieararchies where each hierarchy equals value_to_filter
            and returns as a new object
        Args:
            value_to_filter (iterable): the value to filter on
        """
        filtered_hierarchy_data = self._hierarchy_data.copy()
        filtered_hierarchy_data = filtered_hierarchy_data[
            filtered_hierarchy_data.apply(tuple, axis=1)
            == tuple(path_to_filter)
        ]
        return SiteHierarchies(filtered_hierarchy_data)

    def filter_by_path_start(self, path_to_filter):
        """Filters hieararchies by value_to_filter where the
        start of each item (same length as value_to_filter) in
        hieararchies equals value_to_filter and returns hierarchies as a new
        object

        Args:
            value_to_filter (iterable): The value to filter by
        """
        hierarchies_to_filter = self._hierarchy_data.copy()
        hierarchies_to_search = hierarchies_to_filter.iloc[
            :, :len(path_to_filter)]
        filtered_hierarchies = hierarchies_to_filter[
            hierarchies_to_search.apply(
                tuple, axis=1) == tuple(path_to_filter)
        ]
        return SiteHierarchies(filtered_hierarchies)

    def create_directories(self, base_dir):
        """Creates directory by concatanating base_dir with the directories
        stored in this class

        Args:
            base_dir (string): The base directory to concentate with the
                directories stored in this classs
        """
        for hierarchy_path in self.directory_paths:
            dir_to_create = base_dir + os.path.sep + hierarchy_path
            if not os.path.isdir(dir_to_create):
                os.makedirs(dir_to_create)

    @property
    def file_paths(self):
        """Returns list of file paths in hieararchy as a list of strings"""
        return list(self._hierarchy_data.apply(
            lambda x: os.path.sep.join(list(x.dropna())),
            axis='columns'))

    @property
    def directory_paths(self):
        """Returns list of directory paths in hieararchy as a list of
        strings.  This exludes the last level in the hierarchy which
        represents a file"""
        paths = (self._hierarchy_data.apply(
            lambda x: os.path.sep.join(list(x.dropna()[:-1])),
            axis='columns'))
        # first convert to a set to get unique items only
        return list(set(paths))

    def _directory_paths_as_dataframe(self):
        """Returns list of directory paths in hieararchy as a dataframe.
        This exludes the last level in the hierarchy which represents a file
        """
        dir_paths = self._hierarchy_data.apply(
            lambda x: x.dropna()[:-1],
            axis='columns').drop_duplicates()
        return dir_paths

    @property
    def all_path_levels(self):
        """Returns a list of unique paths recursively at each directory level
        for the directory hierarchies stored in this class.  Excludes the
        last level in hieraarchy which represents the file name
        """
        dir_paths = self._directory_paths_as_dataframe()
        all_path_levels = []
        for column_index in range(len(dir_paths)):
            paths_at_current_level = dir_paths.iloc[
                :, :column_index+1]
            paths_at_current_level = (paths_at_current_level
                                      .drop_duplicates().dropna())
            paths_at_current_level = paths_at_current_level.apply(
                os.path.sep.join, axis=1)
            all_path_levels = all_path_levels + list(paths_at_current_level)
        all_path_levels = list(set(all_path_levels))
        return all_path_levels


class IndexFile():
    """._inded.md file utilised for Hugo site generation"""

    def __init__(self, hierarchies, path_in_hierarchy, base_dir):
        file_path = self._get_file_path(base_dir, path_in_hierarchy)
        self._markdown_content = _MarkdownContent(hierarchies,
                                                  path_in_hierarchy,
                                                  file_path)

    @property
    def markdown_content(self):
        """Returns the markdown_content object"""
        return self._markdown_content

    def _get_file_path(self, base_dir, path_in_hierarchy):
        """returns file path"""
        return (
            base_dir + os.path.sep
            + path_in_hierarchy + os.path.sep
            + '_index.md')


class FormulaFile():
    """..md file containing formula tables for Hugo site generation"""

    def __init__(self, hierarchies, base_dir, is_cumulative_by_year,
                 formula_table):
        path_in_hierarchy = self._get_path_in_hierarchy(formula_table,
                                                        is_cumulative_by_year)
        file_path = self._get_file_path(base_dir, path_in_hierarchy)
        self._markdown_content = _MarkdownContent(hierarchies,
                                                  path_in_hierarchy,
                                                  file_path)
        self.markdown_content.add_content(formula_table.to_markdown())

    @property
    def markdown_content(self):
        """Returns the markdown_content object"""
        return self._markdown_content

    def _get_path_in_hierarchy(self, formula_table, is_cumulative_by_year):
        """Gets the path in hierarchy (excluding any base directory)"""
        if is_cumulative_by_year:
            time_frame_portion_of_path = 'By year cumulative'
        else:
            time_frame_portion_of_path = 'By year'
        return os.path.sep.join([
            formula_table.state,
            formula_table.subject,
            formula_table.type.content_type,
            time_frame_portion_of_path,
            formula_table.type.display_name])

    def _get_file_path(self, base_dir, path_in_hierarchy):
        """Returns the file path"""
        return base_dir + os.path.sep + path_in_hierarchy + '.md'


class TopicFile():
    """..md file containing topic for Hugo site generation"""

    def __init__(self, state, subject, syllabus_topic, hierarchies, base_dir,
                 is_cumulative_by_year):
        path_in_hierarchy = self._get_path_in_hierarchy(
            is_cumulative_by_year, state, subject, syllabus_topic)
        file_path = self._get_file_path(base_dir, path_in_hierarchy)
        self._markdown_content = _MarkdownContent(hierarchies,
                                                  path_in_hierarchy,
                                                  file_path)

    @property
    def markdown_content(self):
        """Returns the markdown_content object"""
        return self._markdown_content

    def add_text(self, input_text):
        """Adds input_text to the file"""
        self._markdown_content.add_content(input_text)

    def _get_path_in_hierarchy(self, is_cumulative_by_year, state, subject,
                               syllabus_topic):
        """Gets the path in hierarchy (excluding any base directory)"""
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

    def _get_file_path(self, base_dir, path_in_hierarchy):
        """Returns the file path"""
        return base_dir + os.path.sep + path_in_hierarchy + '.md'


class _MarkdownContent():
    """Markdown file utilised for creation of Hugo webiite
    """

    def __init__(self, hierarchies, path_in_hierarchy, file_path):
        self._content = None
        self._front_matter = FrontMatter()
        self._hierarchies = hierarchies
        self._path_in_hierarchy = path_in_hierarchy
        self._file_path = file_path

    def add_front_matter_property(self, property_key, property_value):
        """Adds key / value  to front matter"""
        self._front_matter.add_property(property_key, property_value)

    def add_content(self, content):
        """Adds content (string) to the object"""
        if self._content:
            self._content += ('\n\n' + content)
        else:
            self._content = content

    def _set_weight_based_on_hierarchies(self):
        """Adds weight property to front matter based on position of
        path in hierarchy"""
        weight = self._hierarchies.get_sort_index_in_parent_path(
            self._path_in_hierarchy) + 1
        self.add_front_matter_property('weight', weight)

    def _add_front_matter_to_content(self):
        """Adds front matter to the start of content"""
        if self._content:
            self._content = (self._front_matter.to_string()
                             + '\n\n' + self._content)
        else:
            self._content = self._front_matter.to_string()

    def save(self):
        """Saves the content of this object at file_path."""
        self._set_weight_based_on_hierarchies()
        self._add_front_matter_to_content()
        if os.path.isfile(self._file_path):
            raise OSError('Cannot create ' + self._file_path + ' as it already ' +
                          'exists')
        else:
            with open(self._file_path, "w", encoding="utf-8") as text_file:
                text_file.write(self._content)


class FrontMatter():
    """Front matter strings for markdown files utilised to generate Hugo
    webstites
    """

    def __init__(self):
        self._content = {}

    def add_property(self, property_key, property_value):
        """Adds property_value for corresponding property_key in the
        front matter"""
        self._content[property_key] = property_value

    def to_string(self):
        """Returns the front matter as a string
        """
        return_value = '---\n'
        if self._content:
            for key, value in self._content.items():
                return_value += str(key) + ': ' + str(value) + '\n'
        return_value += '---'
        return return_value
