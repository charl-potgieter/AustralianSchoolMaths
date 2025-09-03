import os
import shutil


class WebSite:
    @property
    def _this_file_dir(self) -> str:
        current_file_path = os.path.abspath(__file__)
        current_file_dir = os.path.dirname(current_file_path)
        return current_file_dir

    @property
    def _project_root(self) -> str:
        # Assumes project root is one directory higher than directory of file
        # containing this code.
        project_root = os.path.dirname(self._this_file_dir)
        return project_root

    @property
    def _content_dir(self) -> str:
        content_dir = os.path.join(self._project_root, "content")
        return content_dir

    @property
    def _public_dir(self) -> str:
        content_dir = os.path.join(self._project_root, "public")
        return content_dir

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


if __name__ == "__main__":
    maths_website = WebSite()
    maths_website.delete_content()
