import os
import shutil
from warnings import warn
from pathlib import Path


class FolderManager:
    def __init__(self, *path_elements):
        self.abs_path = Path(os.path.join(*path_elements)).absolute()

    def create_folders(self, *directories):
        path = os.path.join(self.abs_path, *directories)
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)

    def list_content_of_folder(self):
        return [
            folder
            for root, folders, files in os.walk(self.abs_path)
            for folder in folders
        ]

    def delete_folders(self, path):
        f_path = os.path.abspath(path)
        try:
            os.rmdir(f_path)
        except OSError:
            warn("The folder is not empty!")
            input_ = input("Do you want to delete all folders in this directory? Y/N ")
            if input_ in ("y", "Y"):
                shutil.rmtree(f_path)

    def create_folder_tree(self, tree_dict, path=None):
        for key, val in tree_dict.items():
            new_path = (
                os.path.join(self.abs_path, key)
                if path is None
                else os.path.join(path, key)
            )
            os.makedirs(new_path)
            if isinstance(val, dict):
                self.create_folder_tree(tree_dict=val, path=new_path)
