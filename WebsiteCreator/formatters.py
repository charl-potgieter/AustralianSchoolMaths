"""This module implements a formatter for static website generators.  Code
currrently uses Hugo static website generator but abstracting into the
below class ensures that the core code is not tightly coupled with Hugo
code requirements and switch can be made to other static site generators if
required"""

from abc import ABC, abstractmethod


class TabFormatter(ABC):
    @abstractmethod
    def format_tabs_start(self, tab_id: str) -> str:
        pass

    @abstractmethod
    def format_tab_content(self, tab_name: str, tab_content: str) -> str:
        pass

    @abstractmethod
    def format_tabs_end(self) -> str:
        pass


class HugoTabFormatter(TabFormatter):
    def format_tabs_start(self, tab_id: str) -> str:
        return '{{< tabs "' + tab_id + '" >}}'

    def format_tab_content(self, tab_name: str, tab_content: str) -> str:
        # Note quadruple braces required to produce 2 braces in below f-string
        # Not clear why?
        return (
            f'\n\n{{{{< tab "{tab_name}" >}}}}\n\n'
            f"{tab_content}"
            f"{{{{< /tab >}}}}"
        )

    def format_tabs_end(self) -> str:
        return "\n{{< /tabs >}}"
