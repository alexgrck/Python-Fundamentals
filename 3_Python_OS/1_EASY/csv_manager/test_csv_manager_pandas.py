import os
import shutil

from pathlib import Path, WindowsPath
from unittest import TestCase

import pandas as pd
from csv_manager_pandas import CSVManager


class TestCSVManager(TestCase):
    def setUp(self):
        self.test_manager = CSVManager("test_folder", file_name="test_file.csv")
        self.file_path = os.path.join(os.getcwd(), "test_folder", "test_file.csv")
        self.file_path2 = os.path.join(os.getcwd(), "test_folder", "test_file2.csv")
        self.folder_path = Path(os.path.join(os.getcwd(), "test_folder"))
        Path.mkdir(self.folder_path, parents=True)
        self.columns = ["Name", "Surname", "Address", "City", "State", "Income"]
        self.test_dicts = [
            {
                "Name": "John",
                "Surname": "Doe",
                "Address": "120 jefferson st.",
                "City": "Riverside",
                "State": " NJ",
                "Income": "8075",
            },
            {
                "Name": "Jack",
                "Surname": "McGinnis",
                "Address": "220 hobo Av.",
                "City": "Phila",
                "State": " PA",
                "Income": "9119",
            },
            {
                "Name": 'John "Da Man"',
                "Surname": "Repici",
                "Address": "120 Jefferson St.",
                "City": "Riverside",
                "State": " NJ",
                "Income": "8075",
            },
            {
                "Name": "Stephen",
                "Surname": "Tyler",
                "Address": '7452 Terrace "At the Plaza" road',
                "City": "SomeTown",
                "State": "SD",
                "Income": "91234",
            },
        ]

        df1 = pd.DataFrame(self.test_dicts[:2], columns=self.columns)
        df1.to_csv(self.file_path, index=False)
        df2 = pd.DataFrame(self.test_dicts[:2], columns=self.columns)
        df2.to_csv(self.file_path2, index=False)

    def tearDown(self):
        if os.path.exists(self.folder_path):
            shutil.rmtree(self.folder_path)
        elif os.path.exists(self.file_path):
            os.remove(self.file_path)
        elif os.path.exists(self.file_path2):
            os.remove(self.file_path2)

    def test_create_file(self):
        os.remove(self.file_path)
        self.test_manager.create_file(self.file_path)
        self.assertTrue(os.path.exists(self.file_path))

    def test_read_file(self):
        read_from_manager = self.test_manager.read_csv()
        read_from_file_path = pd.read_csv(self.file_path)
        self.assertTrue(read_from_manager.equals(read_from_file_path))

    def test_set_data(self):
        with open(self.file_path, "w", newline=""):
            pass
        self.test_manager.set_data(self.columns, self.test_dicts[:2])
        read_from_manager = pd.read_csv(self.test_manager.abs_path)
        read_from_file_path = pd.read_csv(self.file_path2)
        self.assertTrue(read_from_manager.equals(read_from_file_path))

    def test_add_multiple_rows(self):
        df_read = pd.DataFrame(pd.read_csv(self.file_path2), columns=self.columns)
        df3 = pd.DataFrame(self.test_dicts[2:], columns=self.columns)
        final1 = pd.concat([df_read, df3], ignore_index=True)
        final1.to_csv(self.file_path2, index=False)
        self.test_manager.add_rows(self.columns, self.test_dicts[2:])
        read_from_manager = pd.read_csv(self.test_manager.abs_path)
        read_from_file_path = pd.read_csv(self.file_path2)
        self.assertTrue(read_from_manager.equals(read_from_file_path))

    def test_add_one_row(self):
        df_read = pd.DataFrame(pd.read_csv(self.file_path2), columns=self.columns)
        df3 = pd.DataFrame([self.test_dicts[2]], columns=self.columns)
        final1 = pd.concat([df_read, df3], ignore_index=True)
        final1.to_csv(self.file_path2, index=False)
        self.test_manager.add_rows(self.columns, self.test_dicts[2])
        read_from_manager = pd.read_csv(self.test_manager.abs_path)
        read_from_file_path = pd.read_csv(self.file_path2)
        self.assertTrue(read_from_manager.equals(read_from_file_path))

    def test_update_csv(self):
        new_data = [
            {
                "Name": "John",
                "Surname": "Doe",
                "Address": "120 jefferson st.",
                "City": "Riverside",
                "State": " NJ",
                "Income": "8075",
            },
            {
                "Name": "Jack",
                "Surname": "McGinnis",
                "Address": "220 hobo Av.",
                "City": "Las Vegas",
                "State": " PA",
                "Income": "9119",
            },
        ]
        with open(self.file_path2, "w"):
            df = pd.DataFrame(new_data, columns=self.columns)
            df.to_csv(self.file_path2, index=False)
        self.test_manager.update_csv(1, "City", "Las Vegas")
        read_from_manager = pd.read_csv(self.test_manager.abs_path)
        read_from_file_path = pd.read_csv(self.file_path2)
        self.assertTrue(read_from_manager.equals(read_from_file_path))

    def test_scan_path(self):
        os.remove(self.file_path)
        os.remove(self.file_path2)
        file1_path = Path(self.folder_path).joinpath("read.csv")
        file2_path = Path(self.folder_path).joinpath("to_delete.csv")
        file3_path = Path(self.folder_path).joinpath("with_header.csv")
        file4_path = Path(self.folder_path).joinpath("test_sub", "test_file.csv")
        Path.mkdir(Path(file4_path).parent)
        with open(file1_path, "w", newline=""), open(file2_path, "w", newline=""), open(
            file3_path, "w", newline=""
        ), open(file4_path, "w", newline=""):
            pass
        scan_depth_0 = self.test_manager.scan_path(0, self.folder_path)
        list_paths_depth_0 = [
            Path(file1_path),
            Path(file2_path),
            Path(file3_path),
            Path(file4_path),
        ]
        scan_depth_1 = self.test_manager.scan_path(1, self.folder_path)
        list_paths_depth_1 = [Path(file4_path)]
        scan_depth_2 = self.test_manager.scan_path(2, self.folder_path)
        list_paths_depth_2 = []
        self.assertEqual(scan_depth_0, list_paths_depth_0)
        self.assertEqual(scan_depth_1, list_paths_depth_1)
        self.assertEqual(scan_depth_2, list_paths_depth_2)

    def test_delete_file(self):
        with open(self.file_path, "w", newline=""):
            pass
        self.test_manager.delete_file(self.file_path)
        self.assertFalse(os.path.exists(self.file_path))
