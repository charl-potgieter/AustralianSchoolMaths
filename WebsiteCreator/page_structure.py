# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import uuid


class HiddenDetails():
    """Implements a hidden details section for Hugo website creation
    https://hugo-book-demo.netlify.app/docs/shortcodes/details/"""

    def __init__(self, visible_section: str, hidden_section: str):
        self._visibile_section = visible_section
        self._hidden_section = hidden_section

    def to_markdown(self) -> str:
        return (
            '{{< details title="'
            + self._visibile_section
            + '" open=false >}}\n'
            + self._hidden_section + '\n'
            + '{{< /details >}}\n'
        )


class PageTabs():
    """Manages page tabs for Hugo wesite creation"""

    def __init__(self):
        self._tabs = {}

    def add_tab(self, tab_name: str, tab_content: str) -> None:
        self._tabs[tab_name] = tab_content

    def to_markdown(self) -> str:
        unique_id = str(uuid.uuid4())
        return_value = '{{< tabs "' + unique_id + '" >}}'
        for tab_name, tab_content in self._tabs.items():
            return_value += '\n\n{{< tab "' + tab_name + '" >}}\n\n'
            return_value += tab_content
            return_value += '{{< /tab >}}'
        return_value += '\n{{< /tabs >}}'
        return return_value
