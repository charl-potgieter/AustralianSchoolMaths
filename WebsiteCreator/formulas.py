# prevents raising an error of a return value of type class before completing
# the class definition, for example per_topic_code returns type Formuals
# before the definition for Formulas is conmpelte
from __future__ import annotations
import pandas as pd


class Formulas:
    def __init__(self, formula_data: pd.DataFrame):
        self._data = formula_data

    @property
    def data(self) -> pd.DataFrame:
        return self._data

    @property
    def topic_codes(self) -> list:
        return_value = self.data["Syllabus_subtopic_code"]
        return_value = return_value.unique().tolist()
        return return_value

    def per_topic_code(self, code: str) -> Formulas:
        new_data = pd.DataFrame(
            self.data[self.data["Syllabus_subtopic_code"] == code].copy()
        )
        new_formulas = Formulas(new_data)
        return new_formulas

    @property
    def simple_table(self):
        # TODO: return styled pandas table
        return_value = "<br>\n<br>\n### Formulas"
