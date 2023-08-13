# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import os
from typing import Callable, Self, cast
import pandas as pd


class SiteHierarchies():
    """Stores, retrieves, filters and creates file directory (path) hierarchies
       as well as their indexed sort orders
    """

    def __init__(self, input_data: pd.DataFrame):
        # Do not error check column names as they vary dependent on depth
        # of hierarchy being created
        self._hierarchy_data = input_data
        self._error_check_sort_orders()

    def _error_check_sort_orders(self) -> None:
        """"Error checks thge hierarchy sort orders"""
        if self._first_hierarchy_with_inconsistent_sort_order():
            raise ValueError(
                'Inconsistent site hieriarchy file.  '
                + 'Out of order item: '
                + str(self._first_hierarchy_with_inconsistent_sort_order()))

    def _first_hierarchy_with_inconsistent_sort_order(self) -> list[str]:
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
                current_level_data.apply(list, axis=1))
            inconsistent_item = (
                self._first_non_consecutive_like_item(ordered_paths))
            if inconsistent_item:
                return inconsistent_item
        return []

    def _first_non_consecutive_like_item(self, input_values: list[list[str]]
                                         ) -> list[str]:
        """Returns first item if it is an item in input_values that equals
        another item in input_values but they do not appear consecutively,
        otherwise returns empty list.
        """

        values_ex_consecutive_duplicates = []
        for item in input_values:
            if not values_ex_consecutive_duplicates:
                values_ex_consecutive_duplicates.append(item)
            elif item != values_ex_consecutive_duplicates[-1]:
                values_ex_consecutive_duplicates.append(item)
                if values_ex_consecutive_duplicates.count(item) != 1:
                    return item
        return []

    def copy(self) -> Self:
        new_hierarchy_data = self._hierarchy_data.copy()
        return SiteHierarchies(new_hierarchy_data)

    @property
    def data(self) -> pd.DataFrame:
        return self._hierarchy_data.copy()

    def filter_by_function(self, filter_function: Callable) -> Self:
        """Returns a new filtered WebPagHierarchies object where
        filter_function returns True when passed each item in
        WebPageHierarchies as a pandas series.
        """
        return_rows = self.data.apply(filter_function, axis=1)
        return_data = pd.DataFrame(self.data[return_rows])
        return SiteHierarchies(return_data)

    def get_sort_index(self, dir_to_find: str) -> int:
        """Returns sort index of dir_to_find relative to all paths in the
            hierarchies stored in this object
        """
        dir_paths = dir_to_find.split(os.path.sep)
        matching_hierarchies = self.filter_by_path(dir_paths)
        if len(matching_hierarchies.data):
            return cast(int, matching_hierarchies.data.index[0])
        raise ValueError(dir_to_find + ' not found in hierarchy')

    def get_sort_index_in_parent_path(self, dir_to_find: str) -> int:
        """Returns sort_index of dir_to_find relative to other directories
        with the same parent path
        """
        dir_paths = dir_to_find.split(os.path.sep)
        unique_truncated_hierarchies = (
            self.truncate_to_path_length(len(dir_paths)).unique)
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

    def truncate_to_path_length(self, path_length: int) -> Self:
        """Restricts  hieararches to paths of path_length and returns as a
        new object"""
        hierarchy_data_to_length = self._hierarchy_data.iloc[
            :, :path_length].copy()
        hierarchies_to_length = SiteHierarchies(hierarchy_data_to_length)
        return hierarchies_to_length

    @property
    def unique(self) -> Self:
        """Restricts hierarchies to unique values and returns as a new object
        """
        unique_hierarchy_data = self._hierarchy_data.copy()
        unique_hierarchy_data = unique_hierarchy_data.drop_duplicates()
        return SiteHierarchies(unique_hierarchy_data)

    def reset_sort_index(self) -> Self:
        """Resets the hiearatchy sort order to commence from zero and return
        as a new object
        """
        return SiteHierarchies(
            self._hierarchy_data.copy().reset_index(drop=True))

    def filter_by_path(self, path_to_filter: list[str]) -> Self:
        """filters hieararchies where each hierarchy equals value_to_filter
            and returns as a new object
        """
        filtered_hierarchy_data = self._hierarchy_data.copy()
        filtered_hierarchy_data = filtered_hierarchy_data[
            filtered_hierarchy_data.apply(tuple, axis=1)
            == tuple(path_to_filter)
        ]
        return SiteHierarchies(filtered_hierarchy_data)

    def filter_by_path_start(self, path_to_filter: list[str]) -> Self:
        """Filters hieararchies by path_to_filter where the
        start of each item (same length as value_to_filter) in
        hieararchies equals path_to_filter and returns hierarchies as a new
        object
        """
        hierarchies_to_filter = self._hierarchy_data.copy()
        hierarchies_to_search = hierarchies_to_filter.iloc[
            :, :len(path_to_filter)]
        filtered_hierarchies = hierarchies_to_filter[
            hierarchies_to_search.apply(
                tuple, axis=1) == tuple(path_to_filter)
        ]
        return SiteHierarchies(filtered_hierarchies)

    def create_directories(self, base_dir: str) -> None:
        """Creates directory by concatanating base_dir with the directories
        stored in this class
        """
        for hierarchy_path in self.directory_paths:
            dir_to_create = base_dir + os.path.sep + hierarchy_path
            if not os.path.isdir(dir_to_create):
                os.makedirs(dir_to_create)

    @property
    def file_paths(self) -> list[str]:
        """Returns list of file paths in hieararchy"""
        return list(self._hierarchy_data.apply(
            lambda x: os.path.sep.join(list(x.dropna())),
            axis='columns'))

    @property
    def directory_paths(self) -> list[str]:
        """Returns list of directory paths in hieararchy.  This exludes the
        last level in the hierarchy which represents a file"""
        paths = (self._hierarchy_data.apply(
            lambda x: os.path.sep.join(list(x.dropna()[:-1])),
            axis='columns'))
        return list(set(paths))

    @property
    def _directory_paths_as_dataframe(self) -> pd.DataFrame:
        """Returns list of directory paths in hieararchy as a dataframe.
        This exludes the last level in the hierarchy which represents a file
        """
        dir_paths = pd.DataFrame(self._hierarchy_data.apply(
            lambda x: x.dropna()[:-1],
            axis='columns').drop_duplicates())
        return dir_paths

    @property
    def all_path_levels(self) -> list[str]:
        """Returns a list of unique paths recursively at each directory level
        for the directory hierarchies stored in this class.  Excludes the
        last level in hierarchy which represents the file name
        """
        dir_paths = self._directory_paths_as_dataframe
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
