# - [ ] Write class that will be responsible for managing csv files with
# singleton pattern
# - [ ] Class should have methods for: creating, reading, deleting and
# updating csv files
# - [ ] Class should be able to scan given path for csv files with given
# depth or without (all folders in given location)

import csv
from pathlib import Path
from csv_manager import CSVMixin
import pandas as pd

# muszę pisać w 3.10
# scan?


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CSVManager(CSVMixin, metaclass=SingletonMeta):
    # def __init__(self, *path_segments, file_name="", depth=None):
    #     self.path = Path(*path_segments)
    #     self.depth = depth
    #     self.file_name_path = self.path.joinpath(file_name)

    # def create_csv(self):
    #     # self.file_name = file_name
    #     self.file_name_path.touch()

    def read_csv(self):
        # with open(self.file_name_path, "r", newline="") as csvfile:
        return pd.read_csv(self.file_name_path)
        # return reader
        # with open(self.file_name_path, "r", newline="") as csvfile:
        #     reader = pd.read_csv(csvfile)
        #     return reader
        # for row in reader:
        #     # yield row
        #     # return row
        #     print(row)

        # przenieść skanowanie ścieżek, bez kopiowania kodu

    def update_csv(self, dictionary):
        with open(self.file_name_path, "a", newline="") as csvfile:
            # self.columns = [] if columns is None else columns
            # self.rows = [] if rows is None else rows
            writer = pd.DataFrame(dictionary)
            # writer.columns = columns_names
            writer.to_csv(csvfile)
        # !!! wykorzystać to co już napisałam (gdzieś)
        # traktować tak jak excela

    #         if row:
    #             writer.writerow(row)
    #         elif rows:
    #             writer.writerows(rows)

    # def delete_csv(self):
    #     self.file_name_path.unlink()


csv_manager = CSVManager(
    "C:/",
    "Ola",
    "LocalHost",
    "python-fundamentals-master",
    "3_Python_OS",
    "1. EASY",
    "csv_manager",
    file_name="pandas.csv",
)
# csv_manager.create_file()
# print(csv_manager.file_name_path)
dict1 = {"City": ["Sacramento", "Miami"], "State": ["California", "Florida"]}
csv_manager.update_csv(dict1)

dict2 = {"City": ["Chicago", "Las Vegas"], "State": ["Illinois", "Nevada"]}
csv_manager.update_csv(dict2)
print(csv_manager.read_csv())
