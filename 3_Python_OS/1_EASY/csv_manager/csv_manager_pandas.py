import os
import sys
from pathlib import Path

import pandas as pd
from mixin_path_methods import MixinPathMethods


class CSVManager(MixinPathMethods):
    def __init__(self, *path_elements, file_name=""):
        self.abs_path = Path(os.path.join(*path_elements, file_name)).absolute()

    def read_csv(self):
        return pd.read_csv(self.abs_path)

    def set_data(self, columns, data):
        if isinstance(data, dict) or len(data) == 1:
            main_data = [data]
        else:
            main_data = data
        df = pd.DataFrame(main_data, columns=columns)
        df.to_csv(self.abs_path, index=False)

    def add_rows(self, columns, data):
        if isinstance(data, dict) or len(data) == 1:
            main_data = [data]
        else:
            main_data = data
        file_data = pd.read_csv(self.abs_path)
        df = pd.DataFrame(main_data, columns=columns)
        final_df = pd.concat([file_data, df], ignore_index=True)
        final_df.to_csv(self.abs_path, index=False)

    def update_csv(self, index, column, new_value):
        df = pd.read_csv(self.abs_path)
        df.loc[index, column] = new_value
        df.to_csv(self.abs_path, index=False)
