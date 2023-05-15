import os
import shutil
from pathlib import Path, WindowsPath
from unittest import TestCase

import pandas as pd
from csv_manager_pandas import CSVManager


class TestCSVManager(TestCase):
    def setUp(self):
        self.maxDiff = None
        self.test_manager = CSVManager("test_folder", file_name="test_file.csv")
        self.folder_path = Path.cwd().joinpath("test_folder")
        self.file_path = self.folder_path.joinpath("test_file.csv")
        # os.path.join(os.getcwd(), "test_folder", "test_file.csv")
        self.file_path2 = self.folder_path.joinpath("test_file2.csv")
        self.test_sub = self.folder_path.joinpath("test_sub")
        self.test_file = self.test_sub.joinpath("test_file.csv")
        # os.path.join(os.getcwd(), "test_folder", "test_file2.csv")
        # Path(os.path.join(os.getcwd(), "test_folder"))
        Path.mkdir(self.folder_path)
        # Path.mkdir(self.folder_path, parents=True)
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
        self.df_read = pd.DataFrame(pd.read_csv(self.file_path2), columns=self.columns)

    def tearDown(self):
        shutil.rmtree(self.folder_path)

    def test_read_file(self):
        read_from_manager = self.test_manager.read_csv()[:3]

        read_from_file_path = pd.read_csv(self.file_path)[:3]

        self.assertTrue(read_from_manager.equals(read_from_file_path))

    def test_set_data(self):
        self.test_manager.set_data(self.columns, self.test_dicts[:2])

        read_from_manager = pd.read_csv(self.test_manager.abs_path)
        read_from_file_path = pd.read_csv(self.file_path2)

        self.assertTrue(read_from_manager.equals(read_from_file_path))

    def test_add_multiple_rows(self):
        df3 = pd.DataFrame(self.test_dicts[2:], columns=self.columns)
        final1 = pd.concat([self.df_read, df3], ignore_index=True)
        final1.to_csv(self.file_path2, index=False)

        self.test_manager.add_rows(self.columns, self.test_dicts[2:])

        read_from_manager = pd.read_csv(self.test_manager.abs_path)
        read_from_file_path = pd.read_csv(self.file_path2)
        self.assertTrue(read_from_manager.equals(read_from_file_path))

    def test_add_one_row(self):
        df3 = pd.DataFrame([self.test_dicts[2]], columns=self.columns)
        final1 = pd.concat([self.df_read, df3], ignore_index=True)
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

        df = pd.DataFrame(new_data, columns=self.columns)
        df.to_csv(self.file_path2, index=False)

        self.test_manager.update_csv(1, "City", "Las Vegas")

        read_from_manager = pd.read_csv(self.test_manager.abs_path)
        read_from_file_path = pd.read_csv(self.file_path2)
        self.assertTrue(read_from_manager.equals(read_from_file_path))

    def test_scan_path(self):
        files_list = ["read.csv", "to_delete.csv", "with_header.csv"]
        paths_list = []
        for file in files_list:
            self.folder_path.joinpath(file).touch()
            paths_list.append(self.folder_path.joinpath(file))
        self.test_sub.mkdir()
        self.test_file.touch()
        paths_list.append(self.test_file)
        paths_list.append(self.file_path)
        paths_list.append(self.file_path2)

        scan_depth_0 = self.test_manager.scan_path(0, self.folder_path)
        list_paths_depth_0 = sorted(paths_list)
        scan_depth_1 = self.test_manager.scan_path(1, self.folder_path)
        list_paths_depth_1 = [self.test_file]
        scan_depth_2 = self.test_manager.scan_path(2, self.folder_path)
        list_paths_depth_2 = []

        self.assertEqual(sorted(scan_depth_0), list_paths_depth_0)
        self.assertEqual(scan_depth_1, list_paths_depth_1)
        self.assertEqual(scan_depth_2, list_paths_depth_2)
