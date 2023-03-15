from json_manager import JsonManager
import os
from unittest import TestCase
import json
from pathlib import Path
import shutil


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

    def tearDown(self):
        if os.path.exists(self.folder_path):
            shutil.rmtree(self.folder_path)
        elif os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_create_file(self):
        Path.mkdir(self.folder_path_pathlib, parents=True)
        self.test_manager.create_file(self.file_path)
        self.assertTrue(os.path.exists(self.file_path))

    def test_read_file(self):
        Path.mkdir(self.folder_path_pathlib, parents=True)
        with open(self.file_path, "w") as file:
            json.dump(self.test_dict, file, indent=2)
        loaded = self.test_manager.read_file()
        self.assertEqual(self.test_dict, loaded)

    def test_set_data(self):
        Path.mkdir(self.folder_path_pathlib, parents=True)
        with open(self.file_path, "w") as file:
            pass
        self.test_manager.set_data(self.test_dict)
        with open(self.file_path, "r") as file:
            loaded = json.load(file)
            self.assertEqual(self.test_dict, loaded)

    def test_update_file(self):
        new_data = {"first": ["test_name1", "test_name2"], "second": "file"}
        Path.mkdir(self.folder_path_pathlib, parents=True)
        with open(self.file_path, "w") as file:
            json.dump(self.test_dict, file, indent=2)
        self.test_manager.update_file(new_data)
        with open(self.file_path, "r") as file:
            loaded = json.load(file)
            self.assertEqual(new_data, loaded)

    def test_append_data(self):
        Path.mkdir(self.folder_path_pathlib, parents=True)
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
        Path.mkdir(self.folder_path_pathlib, parents=True)

        file1_path = os.path.join(self.folder_path, "read.json")
        file2_path = os.path.join(self.folder_path, "to_delete.json")
        file3_path = os.path.join(self.folder_path, "with_header.json")
        file4_path = os.path.join(self.folder_path, "test_sub", "test_file.json")
        Path.mkdir(Path(file4_path).parent)

        with open(file1_path, "w") as file1, open(file2_path, "w") as file2, open(
            file3_path, "w"
        ) as file3, open(file4_path, "w") as file4:
            pass
        scan_depth_0 = self.test_manager.scan_path(0, self.folder_path, ext=".json")
        list_paths_depth_0 = [
            "test_dir\\read.json",
            "test_dir\\to_delete.json",
            "test_dir\\with_header.json",
            "test_dir\\test_sub\\test_file.json",
        ]
        scan_depth_1 = self.test_manager.scan_path(1, self.folder_path, ext=".json")
        list_paths_depth_1 = ["test_dir\\test_sub\\test_file.json"]
        scan_depth_2 = self.test_manager.scan_path(2, self.folder_path, ext=".json")
        list_paths_depth_2 = []
        self.assertEqual(scan_depth_0, list_paths_depth_0)
        self.assertEqual(scan_depth_1, list_paths_depth_1)
        self.assertEqual(scan_depth_2, list_paths_depth_2)

    def test_delete_file(self):
        Path.mkdir(self.folder_path_pathlib, parents=True)
        with open(self.file_path, "w", newline="") as file:
            pass
        self.test_manager.delete_file(self.file_path)
        self.assertFalse(os.path.exists(self.file_path))
