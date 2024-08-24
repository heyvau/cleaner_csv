import pandas as pd
from utilities import FileReader

class CleanerCSV:
    def __init__(self, specsfile: str = "default_specs.json"):
        self.specs = FileReader.read_json(filename=specsfile)
        self.df_original = FileReader.read_csv(
            filename=self.specs.get("input_file"),
            sep=self.specs.get("delimiter")
        )
        self.df_copy = self.df_original.copy()

    
    def clean(self):
        if self.specs.get("drop_duplicates"):
            self._drop_duplicates()

        if self.specs.get("drop_na"):
            self._drop_na()

        if self.specs.get("clean_str_columns"):
            self._clean_str_columns()

        if self.specs.get("drop_row_title"):
            self._drop_row_title()

        if self.specs.get("replace_row_char"):
            self._replace_row_char()

        if self.specs.get("clean_outliers"):
            self._clean_outliers()

        if self.specs.get("export_output_file"):
            self._export_output_file()

    
    def _drop_duplicates(self):
        pass


    def _drop_na(self):
        pass

    
    def _clean_str_columns(self):
        pass


    def _drop_row_title(self):
        pass


    def _replace_row_char(self):
        pass


    def _clean_outliers(self):
        pass


    def _export_output_file(self):
        pass


    
if __name__ == "__main__":
    c = CleanerCSV()
