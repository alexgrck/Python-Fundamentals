# def create_folder_tree(self, tree_dict, path=None):
#         for key, val in tree_dict.items():
#             new_path = (
#                 self.abs_path.joinpath(key) if path is None else path.joinpath(key)
#             )
#             Path.mkdir(new_path)
#             if isinstance(val, dict):
#                 self.create_folder_tree(tree_dict=val, path=new_path)

# def scan_path(self, depth, path, ext=".csv"):
#     if depth > 0:
#         str_depth = "*" + (r"\*" * depth) + ext
#         return [file for file in path.glob(str_depth)]
#     return [file for file in path.glob(f"**/*{ext}")]


import itertools
import os
from pathlib import Path
from pprint import pprint
from typing import List

# przypadek bazowy - gdy funkcja doda do drzewka ostatni plik/katalog pochodzący
# z którejkolwiek ze ścieżek


def file_counter(given_path, dict=""):
    path = Path(given_path)
    # --- DZIAŁA
    list_dirs = [item for item in path.rglob("**")]
    list_files = [file for file in path.rglob("*.*")]
    stringed_files = [str(file) for file in list_files]
    files_dict = {}
    for item in stringed_files:
        p = files_dict
        for x in item.split("\\"):
            p = p.setdefault(x, {})
    result_dict = {
        "files": len(list_files),
        "folders": len(list_dirs),
        "results": files_dict,
    }
    return result_dict
    # ---


class Folder:
    name = ""
    files = []
    folders: List[Folder]


path = Path(
    r"C:\Ola\LocalHost\python-fundamentals-master\2_Object-oriented_programming\1_EASY"
)
# print(path.name)
pprint(file_counter(path))

# JAK TO ZROBIĆ REKURENCYJNIE

# list_dirs = [item for item in path.glob("**")]
# list_dirs = [folder for root, folder, file in os.walk(path)]
# list_files = [file for root, folder, file in os.walk(path)]

# count_dirs = 0
# count_files = 0
# result_dict = {}
# list_ = [item for item in path.iterdir()]
# if len(list_) > 1:
#     result_dict.setdefault(path.name, [])
# for item in list_:
#     if item.is_dir():
#         count_dirs += 1
#         result_dict[path.name].append({item.name: "None"})
#     #         # file_counter(item)
#     elif item.is_file():
#         count_files += 1
#         result_dict[path.name].append(item.name)

# file_counter(item)
# for item in paths_to_recursive:
#     if item.is_dir():
#         file_counter(item)
# return len(list_dirs), len(list_files)

# list_files = [file.name for file in path.glob("*.*")]
# count_files += len(list_files)
# parts = [list(file.parts[len(path.parents) :]) for file in list_files]
# parts_lengths = [len(part) for part in parts]
# result_dict = {}

# for key in list_dirs:
#     for value in list_files:
#         result_dict[key] = value

# result = {
#     "files": len(list_files),
#     "folders": len(list_dirs),
#     "result": result_dict,
# }


# for x in range(len(paths_dirs)):
# pp = PrettyPrinter(indent=1, width=80)
# for part in file_counter(path):
#     print(part)

# file counter(path):
#   path
#   os.path.split(path)[1]

# new_path =


# easy_dict = {path.name: []}
# print(easy_dict)
