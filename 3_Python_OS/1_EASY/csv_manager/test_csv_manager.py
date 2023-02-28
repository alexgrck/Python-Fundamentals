from unittest import TestCase
from csv_manager import CSVManager
import csv


class TestCSVManager(TestCase):
    def setUp(self):
        self.csv_m = CSVManager(
            "C:\\Ola\\LocalHost\\python-fundamentals-master\\3_Python_OS\\1_EASY\\csv_manager",
            "test_csv.csv",
        )
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
        ]
        self.fieldnames = ["Name", "Surname", "Address", "City", "State", "Income"]

    def tearDown(self):
        self.csv_m.abs_path.unlink()

    def test_create_file(self):
        file_path = self.csv_m.path.joinpath("test_csv.csv")
        self.csv_m.create_file(self.csv_m.abs_path)
        self.assertEqual(self.csv_m.abs_path, file_path)

    def test_read_file(self):
        self.csv_m.create_file(self.csv_m.abs_path)
        with open(self.csv_m.abs_path, "w", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(self.test_data)
        read = self.csv_m.read_csv()
        self.assertEqual(self.test_data, read)

    def add_one_row_with_header(self):
        self.csv_m.create_file(self.csv_m.abs_path)
        self.csv_m.add_rows_with_header(
            fieldnames=self.fieldnames,
            row={
                "Name": "John",
                "Surname": "Doe",
                "Address": "120 jefferson st.",
                "City": "Riverside",
                "State": " NJ",
                "Income": "8075",
            },
        )
        final_data = self.test_data[:2]
        with open(self.csv_m.abs_path, "r", newline="") as file:
            reader = [line for line in csv.reader(file)]
            self.assertEqual(reader, final_data)

    def test_add_rows_with_header(self):
        self.csv_m.create_file(self.csv_m.abs_path)
        self.csv_m.add_rows_with_header(
            fieldnames=self.fieldnames,
            rows=[
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
            ],
        )
        with open(self.csv_m.abs_path, "r", newline="") as file:
            reader = [line for line in csv.reader(file)]
            self.assertEqual(reader, self.test_data)

    def add_one_more_row(self):
        self.csv_m.create_file(self.csv_m.abs_path)
        self.csv_m.add_rows_with_header(
            fieldnames=self.fieldnames,
            row={
                "Name": "John",
                "Surname": "Doe",
                "Address": "120 jefferson st.",
                "City": "Riverside",
                "State": " NJ",
                "Income": "8075",
            },
        )
        self.csv_m.add_more_rows(
            fieldnames=self.fieldnames,
            row={
                "Name": "Jack",
                "Surname": "McGinnis",
                "Address": "220 hobo Av.",
                "City": "Phila",
                "State": " PA",
                "Income": "9119",
            },
        )
        with open(self.csv_m.abs_path, "r", newline="") as file:
            reader = [line for line in csv.reader(file)]
            final_data = self.test_data[:3]
            self.assertEqual(reader, final_data)

    def add_more_rows(self):
        self.csv_m.create_file(self.csv_m.abs_path)
        self.csv_m.add_rows_with_header(
            fieldnames=self.fieldnames,
            row={
                "Name": "John",
                "Surname": "Doe",
                "Address": "120 jefferson st.",
                "City": "Riverside",
                "State": " NJ",
                "Income": "8075",
            },
        )
        self.csv_m.add_more_rows(
            fieldnames=self.fieldnames,
            rows=[
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
            ],
        )
        with open(self.csv_m.abs_path, "r", newline="") as file:
            reader = [line for line in csv.reader(file)]
            final_data = self.test_data[:4]
            self.assertEqual(reader, final_data)

        # def test_update_file(self):
