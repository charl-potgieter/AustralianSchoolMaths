# prevents raising an error of a return value of type class before completing
# the class definition,
from __future__ import annotations
import os
import shutil
import re


class WebSite:
    def __init__(self):
        self._webpages = []

    @property
    def _this_file_dir(self) -> str:
        current_file_path = os.path.abspath(__file__)
        return_value = os.path.dirname(current_file_path)
        return return_value

    @property
    def web_pages(self) -> list[WebPage]:
        return self._webpages

    @property
    def _project_root_dir(self) -> str:
        """Returns project root, one directory higher than directory of file
        containing this code."""
        return_value = os.path.dirname(self._this_file_dir)
        return return_value

    @property
    def _content_dir(self) -> str:
        return_value = os.path.join(self._project_root_dir, "content")
        return return_value

    @property
    def _content_docs_dir(self) -> str:
        return_value = os.path.join(self._content_dir, "docs")
        return return_value

    @property
    def _content_dir_is_empty(self) -> bool:
        return_value = not os.listdir(self._content_dir)
        return return_value

    @property
    def _public_dir(self) -> str:
        return_value = os.path.join(self._project_root_dir, "public")
        return return_value

    @property
    def _provisional_note_dir(self) -> str:
        return_value = os.path.join(self._this_file_dir, "content_provisional")
        return return_value

    def _delete_folder_contents(self, dir_to_delete):
        for item in os.listdir(dir_to_delete):
            file_path = os.path.join(dir_to_delete, item)
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.remove(file_path)

    def delete_content(self):
        self._delete_folder_contents(self._content_dir)
        self._delete_folder_contents(self._public_dir)

    def copy_provisional_notes_to_web_pages(self):
        if self._content_dir_is_empty:
            shutil.copytree(
                src=self._provisional_note_dir,
                dst=self._content_dir,
                dirs_exist_ok=True,
            )
            self._refresh_web_pages_from_content_dir()
        else:
            raise Exception(
                self._content_dir + " needs to be empty before adding notes"
            )

    def _refresh_web_pages_from_content_dir(self):
        for root, dirs, _ in os.walk(self._content_docs_dir):
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                self._webpages.append(WebPage(dir_path))

    def get_web_page_by_topic_code(self, code: str) -> WebPage | None:
        """Web page file is named index.md and is stored inside a directory
        with name from which topic code can be extracted"""
        for web_page in self.web_pages:
            if web_page.topic_code == code:
                return web_page
        return None


class WebPage:
    def __init__(self, dir: str):
        # dir is the directory containing the web page markdown content
        self._dir = dir
        self._basedir = os.path.basename(os.path.normpath(self._dir))

    @property
    def local_dir(self):
        return self._dir

    @property
    def _index_markdown_file_path(self) -> str:
        return os.path.join(self._dir, "index.md")

    @property
    def _underscore_index_markdown_file_path(self) -> str:
        return os.path.join(self._dir, "_index.md")

    @property
    def markdown_file_path(self) -> str | None:
        if os.path.isfile(self._index_markdown_file_path):
            return self._index_markdown_file_path
        elif os.path.isfile(self._underscore_index_markdown_file_path):
            return self._underscore_index_markdown_file_path
        else:
            return None

    def append_content(self, content: str | None):
        if self.markdown_file_path and content:
            with open(self.markdown_file_path, "a") as f:
                f.write(content)
                f.write("\n")

    @property
    def topic_code(self):
        """Returns the web page topic code if one exists.  The code is
        stored in the pages local directory in the below format
        prefix_TopicCode_postfix"""
        match = re.search(r"_([^_]+)_", self._basedir)
        if match:
            return match.group(1)
        return None
