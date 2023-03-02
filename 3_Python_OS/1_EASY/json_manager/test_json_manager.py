from json_manager import JsonManager

from unittest import TestCase
import json
from pathlib import WindowsPath


class TestJsonManager(TestCase):
    def setUp(self):
        self.json_m = JsonManager(
            "C:\\Ola\\LocalHost\\python-fundamentals-master\\3_Python_OS\\1_EASY\\json_manager",
            file_name="test_file.json",
        )
        self.test_dict = {
            "first": {"1stfolder": {"2ndfolder": {"3rdfolder": {"file": "file.csv"}}}},
            "second": {"1stfolder": {"2nd folder": {"file": "file.csv"}}},
        }

    def tearDown(self):
        if self.json_m.abs_path.exists():
            self.json_m.abs_path.unlink()

    def test_create_file(self):
        file_path = self.json_m.path.joinpath("test_file.json")
        self.json_m.create_file(self.json_m.abs_path)
        self.assertEqual(self.json_m.abs_path, file_path)

    def test_read_file(self):
        self.json_m.create_file(self.json_m.abs_path)
        with open(self.json_m.abs_path, "w") as file:
            json.dump(self.test_dict, file, indent=2)
        loaded = self.json_m.read_file()
        self.assertEqual(self.test_dict, loaded)

    def test_set_data(self):
        self.json_m.create_file(self.json_m.abs_path)
        self.json_m.set_data(self.test_dict)
        with open(self.json_m.abs_path, "r") as file:
            loaded = json.load(file)
            self.assertEqual(self.test_dict, loaded)

    def test_update_file(self):
        new_data = {"first": ["test_name1", "test_name2"], "second": "file"}
        self.json_m.create_file(self.json_m.abs_path)
        self.json_m.set_data(self.test_dict)
        self.json_m.update_file(new_data)
        with open(self.json_m.abs_path, "r") as file:
            loaded = json.load(file)
            self.assertEqual(new_data, loaded)

    def test_append_data(self):
        self.json_m.create_file(self.json_m.abs_path)
        self.json_m.set_data(self.test_dict)
        appended_dict = {"third": {"1": {"2": {"3": "file"}}}}
        self.json_m.append_data(appended_dict)
        dict_with_append = {
            "first": {"1stfolder": {"2ndfolder": {"3rdfolder": {"file": "file.csv"}}}},
            "second": {"1stfolder": {"2nd folder": {"file": "file.csv"}}},
            "third": {"1": {"2": {"3": "file"}}},
        }
        with open(self.json_m.abs_path, "r") as file:
            loaded = json.load(file)
            self.assertEqual(dict_with_append, loaded)

    def test_scan_path(self):
        scan_m = JsonManager(
            "C:\\Ola\\LocalHost\\python-fundamentals-master\\3_Python_OS\\1_EASY\\json_manager\\test_folder"
        )
        scan_depth_0 = scan_m.scan_path(0, scan_m.path, ext=".json")
        list_paths_depth_0 = [
            WindowsPath(
                "C:/Ola/LocalHost/python-fundamentals-master/3_Python_OS/1_EASY/json_manager/test_folder/test_file1.json"
            ),
            WindowsPath(
                "C:/Ola/LocalHost/python-fundamentals-master/3_Python_OS/1_EASY/json_manager/test_folder/inner_folder/test_file2.json"
            ),
        ]
        scan_depth_1 = scan_m.scan_path(1, scan_m.path, ext=".json")
        list_paths_depth_1 = [
            WindowsPath(
                "C:/Ola/LocalHost/python-fundamentals-master/3_Python_OS/1_EASY/json_manager/test_folder/inner_folder/test_file2.json"
            )
        ]
        scan_depth_2 = scan_m.scan_path(2, scan_m.path, ext=".json")
        list_paths_depth_2 = []
        self.assertEqual(scan_depth_0, list_paths_depth_0)
        self.assertEqual(scan_depth_1, list_paths_depth_1)
        self.assertEqual(scan_depth_2, list_paths_depth_2)

    def test_delete_file(self):
        delete_cm = JsonManager(
            "C:\\Ola\\LocalHost\\python-fundamentals-master\\3_Python_OS\\1_EASY\\json_manager\\test_folder",
            file_name="test_file2.json",
        )
        delete_cm.create_file(delete_cm.abs_path)
        delete_cm.delete_file(delete_cm.abs_path)
        self.assertFalse(delete_cm.abs_path.exists())
