import json
import sys
from pathlib import Path
import os

sys.path.append("C:\\Ola\\LocalHost\\python-fundamentals-master\\3_Python_OS\\1_EASY")

from mixin_path_methods import MixinPathMethods


class JsonManager(MixinPathMethods):
    def __init__(self, *path_elements, file_name=""):
        self.folders_path = os.path.join(*path_elements)
        self.file_path = os.path.abspath(os.path.join(*path_elements, file_name))

    def read_file(self):
        """Reading json file."""
        with open(self.file_path, "r") as file:
            return json.load(file)

    def set_data(self, data: dict):
        """Setting data to json file."""
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=2)

    def update_file(self, data):
        """Updating json file by modifying value indicated by given key."""
        with open(self.file_path, "w") as file:
            file.seek(0)
            json.dump(data, file, indent=2)

    def append_data(self, data):
        """Updating json file by appending data at the end of the file."""
        with open(self.file_path, "r+") as file:
            file_data = json.load(file)
            file_data.update(data)
            file.seek(0)
            json.dump(file_data, file, indent=2)
