import os
from pathlib import Path
import json


def convert_jupyter_notebook_to_markdown(src):
    for subdir, dirs, files in os.walk(src):
        # Exclude hidden directories in-place
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for file in files:
            filepath = os.path.join(subdir, file)
            if not file_is_empty(filepath):
                note = ""
                notebook_content = read_json_from_notebook(filepath)
                for cell in notebook_content["cells"]:
                    if note != "":
                        note = note + "\n"
                    note = note + convert_notebook_markdown_content_to_string(
                        cell["source"]
                    )
                save_new_file(note, new_file_path(filepath))


def new_file_path(old_file_path: str) -> str:
    new_path = old_file_path.replace(".ipynb", ".md")
    new_path = new_path.replace("_old", "")
    return new_path


def read_json_from_notebook(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        notebook_content = json.load(file)
    return notebook_content


def convert_notebook_markdown_content_to_string(cell_content) -> str:
    # Jupyter markdown cell is saved to json as a list of strings.
    # This function returns content as a single string.
    return "".join(cell_content)


def file_is_empty(filepath: str) -> bool:
    return os.stat(filepath).st_size == 0


def save_new_file(note: str, filepath: str) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(note)


if __name__ == "__main__":
    src_dir = (
        Path("/home/charl/Documents_Charl_Server/Computer_Technical")
        / "Programming_GitHub/PublicRepos/AustralianSchoolMaths"
        / "WebsiteCreator/data_files_notes_old"
    )

    convert_jupyter_notebook_to_markdown(src_dir)
