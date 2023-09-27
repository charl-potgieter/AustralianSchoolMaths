# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

"""This file handles the displaying of spreadsheet links of the web page"""

from site_content import Spreadsheets


class SpreadsheetLinkDisplay():

    def __init__(self, spreadsheets: Spreadsheets):
        self._spreadsheets = spreadsheets

    def to_markdown(self) -> str:
        return_value = ''
        for spreadsheet in self._spreadsheets.spreadsheets:
            return_value += '* ' + spreadsheet.name + '\n'
        return return_value

    def to_markdown_with_heading(self) -> str:
        return ('### <span style="color:RGB(139,69,19)"> Spreadsheets  </span>'
                + '\n\n\n'
                + self.to_markdown())
