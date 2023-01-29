import json
from pathlib import Path

from mixin_path_methods import MixinPathMethods


class JsonManager(MixinPathMethods):
    def __init__(self, *path_segments, file_name="", depth=0):
        self.path = Path(*path_segments)
        self.file_name_path = self.path.joinpath(file_name)
        self.abs_path = (
            self.file_name_path
            if self.file_name_path.is_absolute()
            else Path.cwd().joinpath(self.file_name_path)
        )
        self.depth = depth

    def read_file(self):
        with open(self.abs_path, "r") as file:
            return json.load(file)

    def set_data(self, data: dict):
        with open(self.abs_path, "w") as file:
            json.dump(data, file, indent=2)

    def update_file(self, data, key=""):
        with open(self.abs_path, "r+") as file:
            file_data = json.load(file)
            for item in file_data:
                for k, val in file_data[item].items():
                    if k == key:
                        file_data[item][k] = data
            file.seek(0)
            json.dump(file_data, file, indent=2)

    def append_data(self, data, key=""):
        with open(self.abs_path, "r+") as file:
            file_data = json.load(file)
            file_data.update(data)
            file.seek(0)
            json.dump(file_data, file, indent=2)
