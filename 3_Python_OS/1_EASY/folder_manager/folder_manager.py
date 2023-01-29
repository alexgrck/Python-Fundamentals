import shutil
from pathlib import Path
from warnings import warn


class FolderManager:
    def __init__(self, *path_segments):
        self.file_path = Path(*path_segments)
        self.abs_path = (
            self.file_path
            if self.file_path.is_absolute()
            else Path.cwd().joinpath(self.file_path)
        )

    def create_folders(self, *directories):
        path = self.abs_path.joinpath(*directories)
        if not Path.exists(path):
            Path.mkdir(path, parents=True)

    def list_content_of_folder(self, folder_path):
        f_path = Path(folder_path)
        return [path_object for path_object in f_path.iterdir()]

    def delete_folders(self, path):
        path_pathlib = Path(path)
        try:
            path_pathlib.rmdir()
        except OSError:
            warn("The folder is not empty!")
            input_ = input("Do you want to delete all folders in this directory? Y/N ")
            if input_ == "y" or input_ == "Y":
                shutil.rmtree(path_pathlib)

    def create_folder_tree(self, tree_dict, path=None):
        for key, val in tree_dict.items():
            new_path = (
                self.abs_path.joinpath(key) if path is None else path.joinpath(key)
            )
            Path.mkdir(new_path)
            if isinstance(val, dict):
                self.create_folder_tree(tree_dict=val, path=new_path)
