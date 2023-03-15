import os
import shutil
from itertools import chain
from unittest import TestCase
from unittest.mock import patch

from folder_manager import FolderManager


class TestFolderManager(TestCase):
    def setUp(self):
        self.fm = FolderManager("5_test_folder")
        self.full_path = os.path.join(
            os.getcwd(), "5_test_folder", "test_1", "test2", "test3"
        )
        self.middle_path = os.path.join(os.getcwd(), "5_test_folder", "test_1", "test2")

    def tearDown(self):
        shutil.rmtree(os.path.join(os.getcwd(), "5_test_folder"))

    def test_create_folders(self):
        self.fm.create_folders("test_1", "test2", "test3")
        self.assertTrue(os.path.exists(self.full_path))

    def test_list_content_of_folder(self):
        os.makedirs(self.full_path)
        path = os.path.join(os.getcwd(), "5_test_folder")
        list_content = self.fm.list_content_of_folder()
        result_list = list(
            chain.from_iterable([dirs for root, dirs, files in os.walk(path)])
        )
        self.assertEqual(list_content, result_list)

    def test_delete_1_folder(self):
        os.makedirs(self.full_path)
        self.fm.delete_folders(self.full_path)
        self.assertFalse(os.path.exists(self.full_path))
        self.assertTrue(os.path.exists(self.middle_path))

    @patch("builtins.input", return_value="y")
    def test_delete_folder_with_subdirectories_yes_input(self, mocked_input):
        os.makedirs(self.full_path)
        with self.assertWarns(Warning):
            self.fm.delete_folders(self.middle_path)
        path_after_deletion = os.path.join(os.getcwd(), "5_test_folder/test_1")
        self.assertFalse(os.path.exists(self.full_path))
        self.assertTrue(os.path.exists(path_after_deletion))

    @patch("builtins.input", return_value="n")
    def test_delete_folder_with_subdirectories_no_input(self, mocked_input):
        os.makedirs(self.full_path)
        with self.assertWarns(Warning):
            self.fm.delete_folders(self.middle_path)
        self.assertTrue(os.path.exists(self.full_path))

    def test_create_folder_tree(self):
        test_dict = {
            "first": {"1stfolder": {"2ndfolder": {"3rdfolder": {"file": "file.csv"}}}},
            "second": {"1stfolder": {"2nd folder": {"file": "file.csv"}}},
        }
        self.fm.create_folder_tree(test_dict)
        path_first = os.path.join(
            os.getcwd(), "first/1stfolder/2ndfolder/3rdfolder/file"
        )
        path_second = os.path.join(
            os.getcwd(), "second/1stfolder/2ndfolder/file/file.csv"
        )
        for root, dirs, files in os.walk(path_first):
            self.assertTrue(dirs)
            self.assertTrue(files)
        for root, dirs, files in os.walk(path_second):
            self.assertTrue(dirs)
            self.assertTrue(files)


# /home/user/root_folder

# root folder -> main.py -> import FolderManager
## folder1 -> folder_manager.py -> definicja FolderManager()

# NAJPIERW trzeba zaimportować w root_folder/folder1/folder_manager.py
# A NASTĘPNIE w root_folder/main.py importować z folder1.folder_manager definicję FolderManager


### subfolder1
### subfolder2
### subfolder3
## folder2
## folder3
