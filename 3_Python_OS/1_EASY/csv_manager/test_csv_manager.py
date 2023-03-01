from unittest import TestCase
from csv_manager import CSVManager
import csv


class TestCSVManager(TestCase):
    def setUp(self):
        self.csv_m1 = CSVManager(
            "C:\\Ola\\LocalHost\\python-fundamentals-master\\3_Python_OS\\1_EASY\\csv_manager",
            "test_csv1.csv",
        )
        self.csv_m2 = CSVManager(
            "C:\\Ola\\LocalHost\\python-fundamentals-master\\3_Python_OS\\1_EASY\\csv_manager",
            "test_csv2.csv",
        )
        self.csv_m_with_data = CSVManager(
            "C:\\Ola\\LocalHost\\python-fundamentals-master\\3_Python_OS\\1_EASY\\csv_manager",
            "test_file_with_data.csv",
        )
        self.csv_m_to_update = CSVManager(
            "C:\\Ola\\LocalHost\\python-fundamentals-master\\3_Python_OS\\1_EASY\\csv_manager",
            "test_file_to_update.csv",
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
        if self.csv_m2.abs_path.exists():
            self.csv_m2.abs_path.unlink()
        elif self.csv_m1.abs_path.exists():
            self.csv_m1.abs_path.unlink()

    def test_create_file(self):
        self.csv_m1.create_file(self.csv_m1.abs_path)
        self.assertTrue(self.csv_m1.abs_path.exists(), True)

    def test_read_file(self):
        self.csv_m1.create_file(self.csv_m1.abs_path)
        with open(self.csv_m1.abs_path, "w", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(self.test_data)
        read = self.csv_m1.read_csv()
        self.assertEqual(self.test_data, read)

    def test_add_rows_with_header(self):
        self.csv_m1.create_file(self.csv_m1.abs_path)
        self.csv_m2.create_file(self.csv_m2.abs_path)
        self.csv_m1.add_rows_with_header(
            fieldnames=self.fieldnames,
            row=self.test_dicts[0],
        )
        final_data1 = self.test_data[:2]
        with open(self.csv_m1.abs_path, "r", newline="") as file:
            reader = [line for line in csv.reader(file)]
            self.assertEqual(reader, final_data1)
        self.csv_m2.add_rows_with_header(
            fieldnames=self.fieldnames, rows=self.test_dicts
        )
        with open(self.csv_m2.abs_path, "r", newline="") as file:
            reader = [line for line in csv.reader(file)]
            self.assertEqual(reader, self.test_data)

    def test_add_more_rows(self):
        self.csv_m_with_data.add_more_rows(
            fieldnames=self.fieldnames,
            row=self.test_dicts[1],
        )
        with open(self.csv_m_with_data.abs_path, "r", newline="") as file:
            reader = [line for line in csv.reader(file)]
            final_data = self.test_data[:3]
            self.assertEqual(reader, final_data)

        with open(self.csv_m_with_data.abs_path, "w", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(self.test_data[:2])
        self.csv_m_with_data.add_more_rows(
            fieldnames=self.fieldnames,
            rows=self.test_dicts[1:3],
        )
        with open(self.csv_m_with_data.abs_path, "r", newline="") as file:
            reader = [line for line in csv.reader(file)]
            final_data = self.test_data[:4]
            self.assertEqual(reader, final_data)
        with open(self.csv_m_with_data.abs_path, "w", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerows(self.test_data[:2])

    def test_update_file(self):
        self.csv_m_to_update.update_csv(self.fieldnames, "City", 2, "Houston")
        new_line = ["Jack", "McGinnis", "220 hobo Av.", "Houston", " PA", "9119"]
        with open(self.csv_m_to_update.abs_path, "r", newline="") as file:
            reader = [line for line in csv.reader(file)]
            self.assertEqual(reader[2], new_line)
