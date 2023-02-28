import os
import shutil
from pathlib import WindowsPath
from unittest import TestCase
from unittest.mock import patch

from folder_manager import FolderManager


class TestFolderManager(TestCase):
    def setUp(self):
        self.fm = FolderManager(
            "C://Ola//LocalHost//python-fundamentals-master//3_Python_OS//1_EASY//folder_manager",
        )

    def tearDown(self):
        try:
            for root, dirs, files in os.walk(self.fm.abs_path):
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
        except OSError:
            for root, dirs, files in os.walk(self.fm.abs_path):
                for name in dirs:
                    shutil.rmtree(os.path.join(root, name))

    def test_create_folders(self):
        self.fm.create_folders("folder1", "folder2")
        folders_path = self.fm.abs_path.joinpath("folder1", "folder2")
        self.assertTrue(folders_path)

    def test_list_content_of_folder(self):
        list_content = self.fm.list_content_of_folder(
            r"C:\Ola\LocalHost\python-fundamentals-master\3_Python_OS\1_EASY\folder_manager"
        )
        test_list = [
            WindowsPath(
                "C:/Ola/LocalHost/python-fundamentals-master/3_Python_OS/1_EASY/folder_manager/folder_manager-easy.md"
            ),
            WindowsPath(
                "C:/Ola/LocalHost/python-fundamentals-master/3_Python_OS/1_EASY/folder_manager/folder_manager.py"
            ),
            WindowsPath(
                "C:/Ola/LocalHost/python-fundamentals-master/3_Python_OS/1_EASY/folder_manager/folder_manager_with_comments.py"
            ),
            WindowsPath(
                "C:/Ola/LocalHost/python-fundamentals-master/3_Python_OS/1_EASY/folder_manager/test_folder_manager.py"
            ),
        ]

        self.assertEqual(list_content, test_list)

    def test_delete_1_folder(self):
        self.fm.create_folders("folder1", "folder2")
        folder_path = self.fm.abs_path.joinpath("folder1", "folder2")
        path_after_deletion = self.fm.abs_path.joinpath("folder1")
        self.fm.delete_folders(folder_path)
        self.assertTrue(path_after_deletion)

    @patch("builtins.input", return_value="y")
    def test_delete_folder_with_subdirectories_yes_input(self, mocked_input):
        self.fm.create_folders("folder1", "folder2")
        folder_path = self.fm.abs_path.joinpath("folder1")
        with self.assertWarns(Warning):
            self.fm.delete_folders(folder_path)
        self.assertTrue(folder_path)

    @patch("builtins.input", return_value="y")
    def test_delete_folder_with_subdirectories_no_input(self, mocked_input):
        self.fm.create_folders("folder1", "folder2")
        folder_path = self.fm.abs_path.joinpath("folder1", "folder2")
        folder_to_delete = self.fm.abs_path.joinpath("folder1")
        with self.assertWarns(Warning):
            self.fm.delete_folders(folder_to_delete)
        self.assertTrue(folder_path)

    def test_create_folder_tree(self):
        test_dict = {
            "first": {"1stfolder": {"2ndfolder": {"3rdfolder": {"file": "file.csv"}}}},
            "second": {"1stfolder": {"2nd folder": {"file": "file.csv"}}},
        }
        self.fm.create_folder_tree(test_dict)
        path_first = self.fm.abs_path.joinpath(
            "first", "1stfolder", "2ndfolder", "3rdfolder", "file"
        )
        path_second = self.fm.abs_path.joinpath(
            "second", "1stfolder", "2ndfolder", "file", "file.csv"
        )
        self.assertTrue(path_first)
        self.assertTrue(path_second)
