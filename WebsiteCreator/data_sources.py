import os
import pandas as pd


class DataSource:
    def _file_is_empty(self, filepath: str) -> bool:
        return os.stat(filepath).st_size == 0

    @property
    def website_creator_directory(self) -> str:
        """Returns the directory containing various code utilised to
        generate content in order to create the hugo website"""
        this_file_path = os.path.dirname(__file__)
        return this_file_path

    @property
    def formulas_file_path(self) -> str:
        return (
            self.website_creator_directory
            + os.path.sep
            + "data_files"
            + os.path.sep
            + "formulas.csv"
        )

    @property
    def syllabus_file_path(self) -> str:
        return (
            self.website_creator_directory
            + os.path.sep
            + "data_files"
            + os.path.sep
            + "syllabus_topics.csv"
        )

    @property
    def subject_dependencies_file_path(self) -> str:
        return (
            self.website_creator_directory
            + os.path.sep
            + "data_files"
            + os.path.sep
            + "subject_dependencies.csv"
        )

    @property
    def syllabus_by_year(self) -> pd.DataFrame:
        return pd.read_csv(self.syllabus_file_path)

    @property
    def subject_dependencies(self) -> pd.DataFrame:
        """Returns the subject dependencies (subjects which have assumed
        knowledge for given subject)
        """
        return pd.read_csv(self.subject_dependencies_file_path)

    @property
    def formulas_by_year(self) -> pd.DataFrame:
        formulas_ex_syllabus = pd.read_csv(
            filepath_or_buffer=self.formulas_file_path,
            converters={
                "On_formula_sheet": self._boolean_converter,
                "Proof_required": self._boolean_converter,
            },
        )
        formulas = pd.merge(
            left=self.syllabus_by_year,
            right=formulas_ex_syllabus,
            left_on=["State", "Code"],
            right_on=["State", "Code"],
            how="right",
        )
        return formulas

    def _boolean_converter(self, field_value: str):
        """Converts textual representations of boolean values to type bool"""
        if len(field_value) == 0:
            return False
        elif field_value.upper() == "FALSE":
            return False
        else:
            return True

    @property
    def formulas_by_year_cumulative(self) -> pd.DataFrame:
        """Returns formula details on a cumulative level by subject
        order  for a given state.  (includes the current subjects formulas
        as well as the formulas from a subjects dependencies)
        """
        return_value = self.formulas_by_year.copy()
        return_value = return_value.rename(columns={"Subject": "Dependency"})
        return_value = return_value.merge(
            right=self.subject_dependencies,
            left_on=["State", "Dependency"],
            right_on=["State", "Dependency"],
        )
        return_value = return_value.drop("Dependency", axis="columns")
        # Re-order cols
        return_value = return_value[
            [
                "State",
                "Subject",
                "Syllabus_topic",
                "Code",
                "Syllabus_subtopic",
                "Category",
                "Subcategory_1",
                "Subcategory_2",
                "Description",
                "Group",
                "Formula",
                "On_formula_sheet",
                "Proof_required",
                "Comment",
            ]
        ]
        return return_value
