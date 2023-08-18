# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

"""This file handles the displaying of definitions of the web page"""

from site_content import Definitions
from page_structure import HiddenDetails


class DefinitionDisplay():

    def __init__(self, definitions: Definitions):
        self._definitions = definitions

    def to_markdown(self) -> str:
        return_value = ''
        for definition in self._definitions.definitions:
            return_value += HiddenDetails(definition.term,
                                          definition.definition).to_markdown()
        return return_value

    def to_markdown_with_heading(self) -> str:
        return ('### Definitions'
                + '\n<br>\n'
                + self.to_markdown())
