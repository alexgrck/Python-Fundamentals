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
        # sprawdzić pierwsze 3 wiersze, czy są poprawne
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
        # wyprintować krok po kroku wszystkie etapy

        # powinno być with, scenariusz
        # akcja
        # print("DELETING FILES")
        # print(os.remove(self.file_path))
        # print(os.remove(self.file_path2))
        # tu dopier jest with
        files_list = ["read.csv", "to_delete.csv", "with_header.csv"]
        print("INITIAL FILES LIST")
        print(files_list)
        print("CREATING FILES FROM PATHS")
        paths_list = []
        for file in files_list:
            print(self.folder_path.joinpath(file).touch())
            paths_list.append(self.folder_path.joinpath(file))
        print("PATHS_LIST AFTER APPENDING")
        print(paths_list)
        # self.folder_path.joinpath("read.csv").touch()
        # self.folder_path.joinpath("to_delete.csv").touch()
        # self.folder_path.joinpath("with_header.csv").touch()

        # za dużo powtórzeń - self.folder_path.joinpath("test_sub")
        print("CREATING TEST_SUB DIR")
        # print(self.folder_path.joinpath("test_sub").mkdir())
        print(self.test_sub.mkdir())
        print("CREATING FILE IN TEST_SUB")
        # print(self.test_sub.joinpath("test_file.csv").touch())
        print(self.test_file.touch())
        # print("CREATING PATHS FROM FILES LIST - 3 PATHS")
        # paths_list = [self.folder_path.joinpath(file) for file in files_list]
        # print(paths_list)
        paths_list.append(self.test_file)
        print("PATHS LIST AFTER APPENDING NEW FILE")
        print(paths_list)
        # paths_list.extend(
        #     [
        #         self.folder_path.joinpath("test_sub", "test_file.csv"),
        #         self.file_path,
        #         self.file_path2,
        #     ])
        # file1_path = self.folder_path.joinpath("read.csv")
        # file2_path = self.folder_path.joinpath("to_delete.csv")
        # file3_path = self.folder_path.joinpath("with_header.csv")
        # # Path.mkdir(folder_file4_path)
        # file4_path = self.folder_path.joinpath("test_sub", "test_file.csv")
        paths_list.append(self.file_path)
        paths_list.append(self.file_path2)
        scan_depth_0 = self.test_manager.scan_path(0, self.folder_path)
        print("SCAN 0")
        print(scan_depth_0)
        list_paths_depth_0 = sorted(paths_list)
        print("LIST_PATHS_DEPTH_0")
        print(list_paths_depth_0)
        # list_paths_depth_0 = [
        #     self.file_path,
        #     self.file_path2,
        #     file1_path,
        #     file2_path,
        #     file3_path,
        #     file4_path,
        # ]
        # NIE DZIAŁA Z DODANIEM ŚCIEŻEK DO LISTY
        scan_depth_1 = self.test_manager.scan_path(1, self.folder_path)
        print("SCAN 1")
        print(scan_depth_1)
        # list_paths_depth_1 = [self.folder_path.joinpath("test_sub", "test_file.csv")]
        list_paths_depth_1 = [self.test_file]
        print("LIST_PATHS_DEPTH_1")
        print(list_paths_depth_1)
        scan_depth_2 = self.test_manager.scan_path(2, self.folder_path)
        print("SCAN 2")
        print(scan_depth_2)
        list_paths_depth_2 = []
        print("LIST_PATHS_DEPTH_2")
        print(list_paths_depth_2)
        print(self.assertEqual(scan_depth_0, list_paths_depth_0))
        # print(self.assertEqual(scan_depth_1, list_paths_depth_1))
        # print(self.assertEqual(scan_depth_2, list_paths_depth_2))
