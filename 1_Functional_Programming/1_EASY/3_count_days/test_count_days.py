import unittest
import datetime
from count_days import count_days, date_from


class TestCountDays(unittest.TestCase):
  
    def test_count_days(self):
        """
        Tests if count_days() is counting days properly.
        """
        date1 = '2022-08-01'
        date2 = '2022-08-31'
        self.assertEqual(count_days(date1, date2), datetime.timedelta(days=30))

    def test_date_from_positive(self):
        """
        Tests if given_date() returns proper date when number_of_days positive.
        """
        given_date = '2022-08-31'
        number_of_days = 5
        self.assertEqual(date_from(given_date, number_of_days), 
                datetime.date(2022, 9, 5))

    def test_date_from_negative(self):
        """
        Tests if given_date() returns proper date when number_of_days negative.
        """
        given_date = '2022-08-31'
        number_of_days = -5
        self.assertEqual(date_from(given_date, number_of_days), 
                datetime.date(2022, 8, 26))

