import unittest
from big_numbers import pretty_display


class TestBigNumbers(unittest.TestCase):

    def test_pretty_display_int(self):
        """
        Tests if it pretty displays an integer.
        """
        number = 2348608546
        result = pretty_display(number)
        self.assertEqual(result, '2,348,608,546')

    def test_pretty_display_float(self):
        """
        Tests if it pretty displays a float.
        """
        number = 25341578153.86596475
        result = pretty_display(number)
        self.assertEqual(result, '25,341,578,153.87')

    