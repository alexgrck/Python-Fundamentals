import json
import os
import shutil
from pathlib import Path
from pprint import pprint
from unittest import TestCase

from json_manager import JsonManager

pp = pprint


class TestJsonManager(TestCase):
    def setUp(self):
        self.test_manager = JsonManager("test_dir", file_name="test_file.json")
        self.file_path = os.path.join(os.getcwd(), "test_dir", "test_file.json")
        self.folder_path = os.path.join(os.getcwd(), "test_dir")
        self.folder_path_pathlib = Path(self.folder_path)
        self.test_dict = {
            "first": {"1stfolder": {"2ndfolder": {"3rdfolder": {"file": "file.json"}}}},
            "second": {"1stfolder": {"2nd folder": {"file": "file.json"}}},
        }
        Path.mkdir(self.folder_path_pathlib, parents=True)

    def tearDown(self):
        if os.path.exists(self.folder_path):
            shutil.rmtree(self.folder_path)
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_create_file(self):
        self.test_manager.create_file(self.file_path)
        self.assertTrue(os.path.exists(self.file_path))

    def test_read_file(self):
        with open(self.file_path, "w") as file:
            json.dump(self.test_dict, file, indent=2)
        loaded = self.test_manager.read_file()
        self.assertEqual(self.test_dict, loaded)

    def test_set_data(self):
        with open(self.file_path, "w"):
            ...
            pass
        self.test_manager.set_data(self.test_dict)
        with open(self.file_path, "r") as file:
            loaded = json.load(file)
            self.assertEqual(self.test_dict, loaded)

    def test_update_file(self):
        new_data = {"first": ["test_name1", "test_name2"], "second": "file"}
        with open(self.file_path, "w") as file:
            json.dump(self.test_dict, file, indent=2)
        self.test_manager.update_file(new_data)
        with open(self.file_path, "r") as file:
            loaded = json.load(file)
        self.assertEqual(new_data, loaded)

    def test_append_data(self):
        with open(self.file_path, "w") as file:
            json.dump(self.test_dict, file, indent=2)
        appended_dict = {"third": {"1": {"2": {"3": "file"}}}}
        self.test_manager.append_data(appended_dict)
        dict_with_append = {
            "first": {"1stfolder": {"2ndfolder": {"3rdfolder": {"file": "file.json"}}}},
            "second": {"1stfolder": {"2nd folder": {"file": "file.json"}}},
            "third": {"1": {"2": {"3": "file"}}},
        }
        with open(self.file_path, "r") as file:
            loaded = json.load(file)
            self.assertEqual(dict_with_append, loaded)

    def test_scan_path(self):
        file1_path = Path(self.folder_path).joinpath("read.json")
        file2_path = Path(self.folder_path).joinpath("to_delete.json")
        file3_path = Path(self.folder_path).joinpath("with_header.json")
        file4_path = Path(self.folder_path).joinpath("test_sub", "test_file.json")
        Path.mkdir(Path(file4_path).parent)

        with open(file1_path, "w"), open(file2_path, "w"), open(file3_path, "w"), open(
            file4_path, "w"
        ):
            pass
        scan_depth_0 = self.test_manager.scan_path(0, self.folder_path, ext=".json")
        list_paths_depth_0 = [
            Path(file1_path),
            Path(file2_path),
            Path(file3_path),
            Path(file4_path),
        ]
        scan_depth_1 = self.test_manager.scan_path(1, self.folder_path, ext=".json")
        list_paths_depth_1 = [Path(file4_path)]
        scan_depth_2 = self.test_manager.scan_path(2, self.folder_path, ext=".json")
        list_paths_depth_2 = []
        self.assertEqual(scan_depth_0, list_paths_depth_0)
        self.assertEqual(scan_depth_1, list_paths_depth_1)
        self.assertEqual(scan_depth_2, list_paths_depth_2)

    def test_delete_file(self):
        with open(self.file_path, "w", newline=""):
            pass
        self.test_manager.delete_file(self.file_path)
        self.assertFalse(os.path.exists(self.file_path))
