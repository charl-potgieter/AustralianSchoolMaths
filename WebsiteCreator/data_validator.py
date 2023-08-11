# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


class DataColumnValidator():

    def __init__(self, column_names: list[str],
                 expected_column_names: list[str]):
        self._column_names = column_names
        self._expected_column_names = expected_column_names

    def validate_column_names(self) -> None:
        if not self.column_names_are_correct:
            raise ValueError(
                self._column_mismatch_message())

    @property
    def column_names_are_correct(self) -> bool:
        return (
            self._number_of_unexpected_columns() == 0
            and self._number_of_missing_columns() == 0)

    def _number_of_unexpected_columns(self) -> int:
        return len(self._unexpected_column_names())

    def _number_of_missing_columns(self) -> int:
        return len(
            self._missing_column_names())

    def _missing_column_names(self) -> list[str]:
        return list(
            set(self._expected_column_names) - set(self._column_names))

    def _unexpected_column_names(self) -> list[str]:
        return list(
            set(self._column_names) - set(self._expected_column_names))

    def _column_mismatch_message(self) -> str:
        message = ''
        if self.column_names_are_correct:
            return message
        if self._missing_column_names():
            message += ('The following columns are missing from the data: '
                        + str(self._missing_column_names()) + '\n')
        if self._unexpected_column_names():
            message += ('The following unexpected columns appear in the data: '
                        + str(self._unexpected_column_names()))
        return message
