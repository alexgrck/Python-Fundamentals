from pathlib import Path
import sys
import pandas as pd

sys.path.append("C:\\Ola\\LocalHost\\python-fundamentals-master\\3_Python_OS\\1_EASY")

from path_methods import MixinPathMethods


class CSVManager(MixinPathMethods):
    def __init__(self, path_string, file_name=""):
        self.path = Path(path_string)
        self.file_name_path = self.path.joinpath(file_name)
        self.abs_path = (
            self.file_name_path
            if self.file_name_path.is_absolute()
            else Path.cwd().joinpath(self.file_name_path)
        )

    def read_csv(self):
        return pd.read_csv(self.abs_path)

    def set_data(self, columns, data):
        df = pd.DataFrame(data, columns=columns)
        df.to_csv(self.abs_path, index=False)

    def add_rows(self, columns, data):
        file_data = pd.read_csv(self.abs_path)
        df = pd.DataFrame(data, columns=columns)
        final_df = pd.concat([file_data, df], ignore_index=True)
        final_df.to_csv(self.abs_path, index=False)

    def update_csv(self, index, column, new_value):
        df = pd.read_csv(self.abs_path)
        df.loc[index, column] = new_value
        df.to_csv(self.abs_path, index=False)
