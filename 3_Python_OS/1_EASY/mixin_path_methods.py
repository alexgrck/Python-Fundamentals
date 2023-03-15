import os
from pathlib import Path


class MixinPathMethods:
    def scan_path(self, depth, path, ext=".csv"):
        if depth > 0:
            str_depth = "*" + (r"\*" * depth) + ext
            return [os.path.relpath(str(file)) for file in Path(path).glob(str_depth)]
        return [os.path.relpath(str(file)) for file in Path(path).glob(f"**/*{ext}")]

    def create_file(self, file_name):
        with open(file_name, "w") as file:
            pass

    def delete_file(self, abs_path):
        os.remove(abs_path)
