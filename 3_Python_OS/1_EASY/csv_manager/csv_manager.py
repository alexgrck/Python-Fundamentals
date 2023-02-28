import csv
from pathlib import Path
import sys

sys.path.append("C:\\Ola\\LocalHost\\python-fundamentals-master\\3_Python_OS\\1_EASY")

from path_methods import MixinPathMethods


class CSVManager(MixinPathMethods):
    def __init__(self, path_string, file_name="", depth=0):
        self.path = Path(path_string)
        self.file_name_path = self.path.joinpath(file_name)
        self.abs_path = (
            self.file_name_path
            if self.file_name_path.is_absolute()
            else Path.cwd().joinpath(self.file_name_path)
        )
        self.depth = depth

    def read_csv(self):
        with open(self.abs_path, "r", newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            return [row for row in reader]

    def add_rows_with_header(self, fieldnames: list, row=None, rows=None):
        with open(self.abs_path, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            if row:
                writer.writerow(row)
            elif rows:
                for row in rows:
                    writer.writerow(row)

    def add_more_rows(self, fieldnames: list, row=None, rows=None):
        with open(self.abs_path, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if row:
                writer.writerow(row)
            elif rows:
                for row in rows:
                    writer.writerow(row)

    def update_csv(self, fieldnames: list, column_name, row_index, new_value):
        with open(self.abs_path, "r", newline="") as csvfile:
            csv_reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            data = [line for line in csv_reader]
            data[row_index][column_name] = new_value
        with open(self.abs_path, "w", newline="") as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csv_writer.writerows(data)
