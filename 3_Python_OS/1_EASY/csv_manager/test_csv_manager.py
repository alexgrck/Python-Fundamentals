from unittest import TestCase
from csv_manager import CSVManager
import csv
from pathlib import Path
import shutil
import os


class TestCSVManager(TestCase):
    def setUp(self):
        self.test_manager = CSVManager("test_folder", file_name="test_file.csv")
        self.file_path = os.path.join(os.getcwd(), "test_folder", "test_file.csv")
        self.folder_path = os.path.join(os.getcwd(), "test_folder")
        self.folder_path_pathlib = Path(self.folder_path)

        self.test_data = [
            ["Name", "Surname", "Address", "City", "State", "Income"],
            ["John", "Doe", "120 jefferson st.", "Riverside", " NJ", "8075"],
            ["Jack", "McGinnis", "220 hobo Av.", "Phila", " PA", "9119"],
            [
                'John "Da Man"',
                "Repici",
                "120 Jefferson St.",
                "Riverside",
                " NJ",
                "8075",
            ],
            [
                "Stephen",
                "Tyler",
                '7452 Terrace "At the Plaza" road',
                "SomeTown",
                "SD",
                "91234",
            ],
        ]
        self.fieldnames = ["Name", "Surname", "Address", "City", "State", "Income"]
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
        with open(self.file_path, "w+", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(self.test_data)
        read = self.test_manager.read_csv()
        self.assertEqual(self.test_data, read)

    def test_add_rows_with_header(self):
        Path.mkdir(self.folder_path_pathlib, parents=True)
        with open(self.file_path, "w+", newline="") as file:
            self.test_manager.add_rows_with_header(
                fieldnames=self.fieldnames,
                row=self.test_dicts[0],
            )
            reader = [line for line in csv.reader(file)]
            self.assertEqual(reader, self.test_data[:2])

        with open(self.file_path, "w+", newline="") as file:
            self.test_manager.add_rows_with_header(
                fieldnames=self.fieldnames,
                rows=self.test_dicts,
            )
            reader = [line for line in csv.reader(file)]
            self.assertEqual(reader, self.test_data)

    def test_add_more_rows(self):
        Path.mkdir(self.folder_path_pathlib, parents=True)
        with open(self.file_path, "w", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(self.test_data[:2])
        with open(self.file_path, "r", newline="") as file:
            self.test_manager.add_more_rows(
                fieldnames=self.fieldnames, row=self.test_dicts[1]
            )
            reader = [line for line in csv.reader(file)]
            self.assertEqual(reader, self.test_data[:3])

        with open(self.file_path, "w", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(self.test_data[:3])
        with open(self.file_path, "r", newline="") as file:
            self.test_manager.add_more_rows(
                fieldnames=self.fieldnames, rows=self.test_dicts[2:]
            )
            reader = [line for line in csv.reader(file)]
            self.assertEqual(reader, self.test_data)

    def test_update_file(self):
        Path.mkdir(self.folder_path_pathlib, parents=True)
        with open(self.file_path, "w", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(self.test_data)

        with open(self.file_path, "r", newline="") as file:
            self.test_manager.update_csv(self.fieldnames, "City", 2, "Houston")
            new_line = ["Jack", "McGinnis", "220 hobo Av.", "Houston", " PA", "9119"]
            reader = [line for line in csv.reader(file)]
            self.assertEqual(reader[2], new_line)

    def test_scan_path(self):
        Path.mkdir(self.folder_path_pathlib, parents=True)

        file1_path = os.path.join(self.folder_path, "read.csv")
        file2_path = os.path.join(self.folder_path, "to_delete.csv")
        file3_path = os.path.join(self.folder_path, "with_header.csv")
        file4_path = os.path.join(self.folder_path, "test_sub", "test_file.csv")
        Path.mkdir(Path(file4_path).parent)
        with open(file1_path, "w", newline="") as file1, open(
            file2_path, "w", newline=""
        ) as file2, open(file3_path, "w", newline="") as file3, open(
            file4_path, "w", newline=""
        ) as file4:
            pass
        scan_depth_0 = self.test_manager.scan_path(0, self.folder_path)
        list_paths_depth_0 = [
            "test_folder\\read.csv",
            "test_folder\\to_delete.csv",
            "test_folder\\with_header.csv",
            "test_folder\\test_sub\\test_file.csv",
        ]
        scan_depth_1 = self.test_manager.scan_path(1, self.folder_path)
        list_paths_depth_1 = ["test_folder\\test_sub\\test_file.csv"]
        scan_depth_2 = self.test_manager.scan_path(2, self.folder_path)
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
