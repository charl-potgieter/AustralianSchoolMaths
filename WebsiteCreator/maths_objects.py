"""This Module contains classes of maths objects including:
    -  formulas
    -  descriptions
"""

import os
import pandas as pd


class DataSource():
    """Gets file directories and data source from underlying files (sometimes
    requiring merging and filtering and returns data as pandas dataframes)
    """

    def website_creator_directory(self):
        """Returns the directory containing various files utilised to
        create the hugo website by relative reference to the directory
        of the file containgin this code"""
        this_file_path = os.path.dirname(__file__)
        return this_file_path

    def docs_directory(self):
        """Returns the docs directory used to generate Hugo website content.
        The directory path is determined by relative reference the file
        containing this code"""
        this_file_path = os.path.dirname(__file__)
        return (os.path.join(
            os.path.dirname(this_file_path),
            'content', 'docs'))

    def hierarchies_directory(self):
        """Returns directory string of site_hierarchy.csv file"""
        return (self.website_creator_directory()
                + os.path.sep
                + 'site_hierarchy.csv')

    def formulas_directory(self):
        """Returns directory string of formulas.csv file"""
        return (self.website_creator_directory() + os.path.sep
                + 'formulas.csv')

    def syllabus_directory(self):
        """Returns directory string of syllabus_topics.csv file"""
        return (self.website_creator_directory() + os.path.sep
                + 'syllabus_topics.csv')

    def site_hierarchies(self):
        """Returns the site hierarchy data as a pandas dataframe
        """
        hierarchy_data = pd.read_csv(self.hierarchies_directory())
        return hierarchy_data

    def _state_subject_sort_orders(self):
        """Returns subjects in order per state as a dataframe
        """
        return_data = self.site_hierarchies()
        return_data = return_data[
            (return_data['Content type'] == 'Formulas') &
            (return_data['Time period'] == 'By year')
        ]
        return_data = return_data[['State', 'Subject']].drop_duplicates()
        return_data = return_data.reset_index(drop=True)
        return_data = return_data.rename(
            columns={'State': 'Sort state', 'Subject': 'Sort subject'}
        )
        return_data['State subject sort order'] = return_data.index
        return return_data

    def formulas_by_year(self):
        """Returns dataframe of formulas and related fields by merging
        formulas (ex-syllabus) and syllabus files
        """

        # TODO Temporarily mark empty boolean fields as false to avoid type errors
        # Remove once all data capture is complete
        formulas_input_converter = {
            'Proof required': lambda x: True if x else False}
        formulas_ex_syllabus = pd.read_csv(
            filepath_or_buffer=self.formulas_directory(),
            converters=formulas_input_converter)
        syllabus = pd.read_csv(self.syllabus_directory())
        formulas = pd.merge(
            left=syllabus, right=formulas_ex_syllabus,
            left_on=['State', 'Subject', 'Syllabus subtopic code'],
            right_on=['State', 'Subject', 'Syllabus subtopic code'],
            how='right')
        return formulas

    def formulas_by_year_cumulative(self):
        """Returns formula details dataframe on a cumulative level by subject
        order  for a given state.
        For example if subject Year 12 is ordered after Year 10 and Year 9 for
        a given state then include the formula details for Year 10 and Year 9
        in the dataframe under subject Year 12.
        """

        formulas_by_year = self.formulas_by_year()
        state_subject_sort_orders = self._state_subject_sort_orders()

        # Add the subject Sort order (representing the sort order for the
        # subject by given state) to the formulas data
        return_data = state_subject_sort_orders.merge(
            right=formulas_by_year,
            how='inner',
            left_on=['Sort state', 'Sort subject'],
            right_on=['State', 'Subject']
        )
        return_data = return_data.rename(
            columns={
                'State subject sort order': 'Data sort index'})
        return_data = return_data.drop(columns=['Sort state',
                                                'Sort subject'])

        return_data = return_data.merge(
            right=state_subject_sort_orders,
            how='inner', left_on=['State'], right_on=['Sort state']
        )
        return_data = return_data[return_data['State subject sort order'] >=
                                  return_data['Data sort index']]
        return_data = return_data.drop(columns=['Data sort index',
                                                'State subject sort order',
                                                'Sort state', 'Subject'])
        return_data = return_data.rename(columns={
            'Sort subject': 'Subject'})
        return return_data


class DataManager():
    """Validates, sets data types and returns data"""

    def __init__(self, data):
        """Initiates class with content of data

        Args:
            data (Pandas dataframe): Input data
        """
        self._data = data.copy()

    def set_column_types(self, column_types):
        """Sets the column types

        Args:
            column_types (dictionary): The column types to set
        """
        self._data = self._data.astype(column_types)

    def to_dataframe(self):
        """Returns data as a pandas dataframe"""
        return self._data

    def column_names_are_correct(self, expected_column_names):
        """Returns true if expected_column_names match the column names
        of the data stored by this object

        Args:
            expected_column_names (iterable): The expected colummn names to
            check against column names of data stored in this object
        """
        number_of_unexpected_columns = len(
            self._unexpected_column_names_in_data(expected_column_names))
        number_of_missing_columns = len(
            self._missing_column_names_in_data(expected_column_names))
        return (number_of_unexpected_columns == 0
                and number_of_missing_columns == 0)

    def column_mismatch_message(self, expected_column_names):
        """Returns a string listing any differences between
        expected_column_names and column_names of data stored in this object.
        Returns None if no differences

        Args:
            expected_column_names (iterable): The expected colummn names to
            check against column names of data stored in this object
        """
        if self.column_names_are_correct(expected_column_names):
            return None
        message = ''
        missing_column_names = (
            self._missing_column_names_in_data(expected_column_names))
        unexpected_column_names = (
            self._unexpected_column_names_in_data(expected_column_names)
        )
        if missing_column_names:
            message += ('The following columns are missing from the data: '
                        + str(missing_column_names) + '\n')
        if unexpected_column_names:
            message += ('The following unexpected columns appear in the data: '
                        + str(unexpected_column_names))
        return message

    def _unexpected_column_names_in_data(self, expected_column_names):
        """Returns a list of column names in this objects data that are not
        in the expected_column_names parameter

        Args:
            expected_column_names (iterable): column names to check
        """
        return list(
            set(self.to_dataframe().columns) - set(expected_column_names))

    def _missing_column_names_in_data(self, expected_column_names):
        """Returns a list of column names that are included in in the
        expected_column_names parameter but do not appear in this objects data

        Args:
            expected_column_names (iterable): column names to check
        """
        return list(
            set(expected_column_names) - set(self.to_dataframe().columns))


class SiteHierarchies():
    """Stores, retrieves, filters and creates file directory (path) hierarchies
       as well as their indexed sort orders
    """

    def __init__(self, input_data):
        """Initiates class with data content

        Args:
            data (Pandas dataframe): input data
        """
        data_to_load = DataManager(input_data)
        # Do not error check column names as they vary dependent on depth
        # of hierarchy being created
        self._hierarchy_data = data_to_load.to_dataframe()
        self._error_check_sort_orders()
        self._current_index = -1  # Utilised for iterator

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
        for hierarchy_path in self.directory_paths():
            dir_to_create = base_dir + os.path.sep + hierarchy_path
            if not os.path.isdir(dir_to_create):
                os.makedirs(dir_to_create)

    def file_paths(self):
        """Returns list of file paths in hieararchy as a list of strings"""
        return list(self._hierarchy_data.apply(
            lambda x: os.path.sep.join(list(x.dropna())),
            axis='columns'))

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

    def __init__(self, path_in_hierarchy):
        self._content = _MarkdownContent()
        self._front_matter = FrontMatter()
        self._path_in_hierarchy = path_in_hierarchy

    def add_front_matter_property(self, property_key, property_value):
        """Adds key / value  to front matter"""
        self._front_matter.add_property(property_key, property_value)

    def set_weight_based_on_hierarchies(self, hierarchies):
        """Adds weight property to front matter based on position of
        path in hierarchy"""
        weight = hierarchies.get_sort_index_in_parent_path(
            self._path_in_hierarchy) + 1
        self.add_front_matter_property('weight', weight)

    def save(self, base_dir):
        """Saves at base_dir + path_in_hierarcy"""
        self._content.add_content(self._front_matter.to_string())
        filename = (base_dir + os.path.sep
                    + self._path_in_hierarchy + os.path.sep
                    + '_index.md')
        self._content.save(filename)


class FormulaFile():
    """..md file containing formula tables for Hugo site generation"""

    def __init__(self, path_in_hierarchy):
        self._content = _MarkdownContent()
        self._front_matter = FrontMatter()
        self._path_in_hierarchy = path_in_hierarchy
        self._formula_table = None

    def add_front_matter_property(self, property_key, property_value):
        """Adds key / value  to front matter"""
        self._front_matter.add_property(property_key, property_value)

    def set_weight_based_on_hierarchies(self, hierarchies):
        """Adds weight property to front matter based on position of
        path in hierarchy"""
        weight = hierarchies.get_sort_index_in_parent_path(
            self._path_in_hierarchy) + 1
        self.add_front_matter_property('weight', weight)

    def add_formula_table(self, formula_table):
        """Adds FormulaTable object to formula file"""
        self._formula_table = formula_table

    def save(self, base_dir):
        """Saves at base_dir + path_in_hierarcy"""
        self._content.add_content(self._front_matter.to_string())
        if not self._formula_table is None:
            self._content.add_content(self._formula_table.to_markdown())
        filename = (base_dir + os.path.sep
                    + self._path_in_hierarchy + '.md')
        self._content.save(filename)


class _MarkdownContent():
    """Markdown file utilised for creation of Hugo webiite
    """

    def __init__(self):
        self._content = None

    def add_content(self, content):
        """Adds content (string) to the object"""
        if self._content:
            self._content += ('\n\n' + content)
        else:
            self._content = content

    def save(self, file_path):
        """Saves the content of this object at file_path.

        Args:
            file_path (string): The directory excluding file name where
                the file will be saved.
        """
        if os.path.isfile(file_path):
            raise OSError('Cannot create ' + file_path + ' as it already ' +
                          'exists')
        else:
            with open(file_path, "w", encoding="utf-8") as text_file:
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


class Formulas():
    """Contains the formulas object representing different views / slices
    of the given input set of formulas
    """

    # Enforces structure of fomulas csv when loaded along with the
    # _formula_input_converter
    _data_structure = {'State': 'object',
                       'Subject': 'object',
                       'Syllabus topic': 'object',
                       'Syllabus subtopic code': 'object',
                       'Syllabus subtopic': 'object',
                       'Category': 'object',
                       'Subcategory_1': 'object',
                       'Subcategory_2': 'object',
                       'Description': 'object',
                       'Group': 'object',
                       'Formula': 'object',
                       'On formula sheet': 'bool',
                       'Proof required': 'bool',
                       'Comment': 'object'}

    def __init__(self, input_data):
        """Initiates class with data from input_data

        Args:
            input_data (dataframe): formula data
        """
        data_to_load = DataManager(input_data)
        self._check_column_names(data_to_load)
        data_to_load.set_column_types(self._data_structure)
        self._formula_data = data_to_load.to_dataframe()

    def _check_column_names(self, data_to_load):
        """Check if column names in data_to_load match expecations as per
            self._data_structure.  Raise ValueError if not matching.

        Args:
            data_to_load (DataManager): The data to check
        """
        expected_columns = self._data_structure.keys()
        if not data_to_load.column_names_are_correct(expected_columns):
            raise ValueError(
                data_to_load.column_mismatch_message(expected_columns))

    def to_dataframe(self):
        """Returns formula data as a pandas dataframe
        """
        return self._formula_data

    def formula_sheet_items(self):
        """Returns a list of formulas where field 'On formula sheet'
        is True
        """
        formulas_on_sheet = (self._formula_data[
            (self._formula_data['On formula sheet']) &
            (self._formula_data['Formula'].notnull())
        ]['Formula'].drop_duplicates())
        return list(formulas_on_sheet)

    def have_formula_sheet_items(self):
        """Returns true if object has one or more non-null formula field
        items where field 'On formula sheet' is true"""
        return len(self.formula_sheet_items()) >= 1

    def proofs_required_items(self):
        """Returns a list of formulas where field 'Proof required'
         is True

        Args:
            state (string): filter to apply before returning items
        """
        proofs_required = (self._formula_data[
            (self._formula_data['Proof required']) &
            (self._formula_data['Formula'].notnull())
        ]['Formula'].drop_duplicates())
        return list(proofs_required)

    def have_proof_required_items(self):
        """Returns true if object has one or more non-null formula field
        items where field 'Proof required' is true"""
        return len(self.proofs_required_items()) >= 1

    def filter_by_function(self, filter_function):
        """Returns a new filtered Formulas object where
        filter_function returns True when passed each item in
        Formuls as a pandas series.

        Args:
            filter_function (function): Function taking a pandas series as a
            parameter and returns a Boolean value
        """
        return_rows = self._formula_data.apply(filter_function, axis=1)
        return_data = self._formula_data.copy()[return_rows]
        return Formulas(return_data)

    def field_value(self, field_name):
        """Returns the value in field_name.  If multiple non-unique values exist
        return 'Multiple Values'"""
        unique_values_in_field = (
            self._formula_data[field_name].drop_duplicates())
        if len(unique_values_in_field) == 1:
            return list(unique_values_in_field)[0]
        return 'Multiple values'

    def group_by_columns(self, columns):
        """Returns a generator of formulas object grouped by columns (iterable)
        """
        grouper = self._formula_data.groupby(columns)
        for _, data in grouper:
            yield Formulas(data)


class FormulaTable():
    """Summary table of formulas"""

    def __init__(self, formulas):
        """Initiates the class

        Args:
            formulas (Formulas object): the input data
        """
        self._formulas = formulas
        self._table_type = None

    def set_type(self, table_type):
        """Sets table type"""
        self._table_type = table_type(self._formulas)

    def _to_dataframe(self):
        """Returns FormulaTable as pandas dataframe"""
        return self._table_type.to_dataframe()

    def has_tabs(self):
        """Returns true if table has / requires tabs"""
        return (
            self._formulas.have_formula_sheet_items() or
            self._formulas.have_proof_required_items()
        )

    def _table_no_higlights(self):
        """Returns table with no highlights"""
        return_table = _StyledTable(self._to_dataframe())
        return_table.hide_column_headers()
        return_table.hide_row_headers()
        return return_table.to_html()

    def _table_formula_sheet_higlights(self):
        """Returns table with formulas on formula sheet higlighted"""
        return_table = _StyledTable(self._to_dataframe())
        return_table.hide_column_headers()
        return_table.hide_row_headers()
        return_table.highlight_values_in_list(
            self._formulas.formula_sheet_items(),
            columns_to_highlight=self._table_type.formula_columns())
        return return_table.to_html()

    def _table_proofs_required_higlights(self):
        """Returns table with formulas where proofs are required higlighted"""
        return_table = _StyledTable(self._to_dataframe())
        return_table.hide_column_headers()
        return_table.hide_row_headers()
        return_table.highlight_values_in_list(
            self._formulas.proofs_required_items(),
            columns_to_highlight=self._table_type.formula_columns(),
            rgba='0,150,200, 0.2')
        return return_table.to_html()

    def to_markdown(self):
        """Returns formula table in markdown format"""
        if not self.has_tabs():
            return_value = self._table_no_higlights()
        else:
            tabs = PageTabs()
            tabs.add_tab('Standard view', self._table_no_higlights())
            if self._formulas.have_formula_sheet_items():
                tabs.add_tab(
                    'Formula sheet',
                    'Items on formula sheet are highlighted \n<br>\n'
                    + self._table_formula_sheet_higlights())
            if self._formulas.have_proof_required_items():
                tabs.add_tab(
                    'Poofs required',
                    'Items where proofs required are highlighted \n<br>\n'
                    + self._table_proofs_required_higlights())
            return_value = tabs.to_markdown()
        return return_value


class SimpleFormulaTableType():
    """Sets type attributes for simple one column formula table"""

    def __init__(self, formulas):
        self._formulas = formulas

    def formula_columns(self):
        """Returns the names of columns containing formulas as a list"""
        return ['Formula']

    def to_dataframe(self):
        """Returns the table as a dataframe"""
        return self._formulas.to_dataframe()[['Formula']]


class _StyledTable():
    """Implements a dataframe styler customised for maths formula display"""

    def __init__(self, input_df):
        """Initialises the class with pandas input dataframe with
        default table formatting"""
        self._table = input_df.fillna('').style
        self._table = self._table.set_table_styles([
            {'selector': 'th.col_heading',
             'props': 'text-align: left; font-size:1em;'},
            {'selector': 'td', 'props':
             'text-align: left; font-size:1em;padding: 1.5em;'}])

    def _raw(self):
        """Returns the pandas styler"""
        return self._table

    def to_html(self):
        """Returns the styled table object in html format"""
        return self._table.to_html()

    def hide_column_headers(self):
        """Hides headers"""
        self._table = self._table.hide(axis='columns')

    def hide_row_headers(self):
        """Hides headers"""
        self._table = self._table.hide(axis='index')

    def highlight_values_in_list(self, value_list,
                                 columns_to_highlight=None,
                                 rgba='255,194,10, 0.2'):
        """Highlights values in columns_to_highlight if they appear in
        value_list.  Values in all columns are highlighted if
        colums_to_higlight is None
        """
        format_value = 'background-color:rgba(' + rgba + ');'
        self._table = self._table.applymap(
            func=lambda x: format_value if x in value_list else None,
            subset=columns_to_highlight, )


class PageTabs():
    """Manages page tabs for Hugo wesite creation"""

    def __init__(self):
        self._tabs = None

    def add_tab(self, tab_name, tab_content):
        """Adds tab with name and content"""
        if not self._tabs:
            self._tabs = {}
        self._tabs[tab_name] = tab_content

    def to_markdown(self):
        """Returns the tabs as markdown string"""
        return_value = '{{< tabs "uniqueid" >}}'
        for tab_name, tab_content in self._tabs.items():
            return_value += '\n\n{{< tab "' + tab_name + '" >}}\n\n'
            return_value += tab_content
            return_value += '{{< /tab >}}'
        return_value += '\n{{< /tabs >}}'
        return return_value


class HierarchyPaths():
    """Calculates and returns file paths in heriarchy (ex any base dir)"""

    def simple_formula_table_pages(self, formulas, is_cumulative):
        """Returns hierarchy path for simple formula table pages
        """

        if is_cumulative:
            time_frame_portion_of_path = 'By year cumulative'
        else:
            time_frame_portion_of_path = 'By year'

        path_in_hierarchy = os.path.sep.join([formulas.field_value('State'),
                                              formulas.field_value('Subject'),
                                              'Formulas',
                                              time_frame_portion_of_path,
                                              formulas.field_value('Category')
                                              ])
        return path_in_hierarchy
