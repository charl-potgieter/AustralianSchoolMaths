import os
import shutil


class WebSite:
    @property
    def _this_file_dir(self) -> str:
        current_file_path = os.path.abspath(__file__)
        return_value = os.path.dirname(current_file_path)
        return return_value

    @property
    def _project_root(self) -> str:
        # Assumes project root is one directory higher than directory of file
        # containing this code.
        return_value = os.path.dirname(self._this_file_dir)
        return return_value

    @property
    def _content_dir(self) -> str:
        return_value = os.path.join(self._project_root, "content")
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
        return_value = os.path.join(self._project_root, "public")
        return return_value

    @property
    def _provisional_note_dir(self) -> str:
        return_value = os.path.join(self._this_file_dir, "docs_provisional")
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

    def add_notes(self):
        if self._content_dir_is_empty:
            self._copy_provisional_notes_to_content_docs_dir()
        else:
            raise Exception(
                self._content_dir + " needs to be empty before adding notes"
            )

    def _copy_provisional_notes_to_content_docs_dir(self):
        shutil.copytree(self._provisional_note_dir, self._content_docs_dir)


# TODO:delete main section once developmnent is complete
if __name__ == "__main__":
    maths_website = WebSite()
    maths_website.delete_content()
    maths_website.add_notes()
