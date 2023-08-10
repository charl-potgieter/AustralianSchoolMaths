# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


class DataColumnValidator():

    def validate_column_names(self, column_names, expected_column_names):
        if not self.column_names_are_correct(column_names,
                                             expected_column_names):
            raise ValueError(
                self._column_mismatch_message(column_names,
                                              expected_column_names))

    def column_names_are_correct(self, column_names, expected_column_names):
        number_of_unexpected_columns = len(
            self._unexpected_column_names_in_data(column_names,
                                                  expected_column_names))
        number_of_missing_columns = len(
            self._missing_column_names_in_data(column_names,
                                               expected_column_names))
        return (number_of_unexpected_columns == 0
                and number_of_missing_columns == 0)

    def _column_mismatch_message(self, column_names, expected_column_names):
        if self.column_names_are_correct(column_names, expected_column_names):
            return None
        message = ''
        missing_column_names = (
            self._missing_column_names_in_data(column_names,
                                               expected_column_names))
        unexpected_column_names = (
            self._unexpected_column_names_in_data(column_names,
                                                  expected_column_names)
        )
        if missing_column_names:
            message += ('The following columns are missing from the data: '
                        + str(missing_column_names) + '\n')
        if unexpected_column_names:
            message += ('The following unexpected columns appear in the data: '
                        + str(unexpected_column_names))
        return message

    def _unexpected_column_names_in_data(self, column_names,
                                         expected_column_names):
        return list(
            set(column_names) - set(expected_column_names))

    def _missing_column_names_in_data(self, columns_names,
                                      expected_column_names):
        return list(
            set(expected_column_names) - set(columns_names))
