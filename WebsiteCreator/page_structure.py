import hashlib


class HiddenDetails:
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
            + self._hidden_section
            + "\n"
            + "{{< /details >}}\n"
        )


class PageTabs:
    """Manages page tabs for Hugo website creation"""

    def __init__(self):
        self._tabs = {}

    def add_tab(self, tab_name: str, tab_content: str) -> None:
        self._tabs[tab_name] = tab_content

    def to_markdown(self) -> str:
        return_value = '{{< tabs "' + self._stable_id + '" >}}'
        for tab_name, tab_content in self._tabs.items():
            return_value += '\n\n{{< tab "' + tab_name + '" >}}\n\n'
            return_value += tab_content
            return_value += "{{< /tab >}}"
        return_value += "\n{{< /tabs >}}"
        return return_value

    @property
    def _stable_id(self) -> str:
        """Creates a stable unique id to use for the tab.  Utilising something
        like uuid.uuid4 triggers unecessary git differences and is best
        avoided
        """
        hasher = hashlib.md5()
        for tab_name, tab_content in self._tabs.items():
            hasher.update(tab_name.encode())
            hasher.update(tab_content.encode())
        stable_id = hasher.hexdigest()[:8]
        return stable_id
