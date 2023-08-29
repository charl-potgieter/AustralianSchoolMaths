# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

"""This file handles the displaying of Notes of the web page"""

from site_content import Notes


class NoteDisplay():

    def __init__(self, notes: Notes):
        self._notes = notes

    def to_markdown(self) -> str:
        return_value = ''
        for note_item in self._notes.notes:
            return_value += '* ' + note_item.note + '\n'
        return return_value

    def to_markdown_with_heading(self) -> str:
        return ('### Notes'
                + '\n\n\n'
                + self.to_markdown())
