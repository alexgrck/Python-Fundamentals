import unittest
from case_sensitive import case_check


class TestCaseSensitive(unittest.TestCase):
    def test_if_lower(self):
        """
        Tests if given parameters are lower.
        """
        string_1 = "abc"
        string_2 = "def"
        self.assertTrue(case_check(string_1, string_2))
        self.assertTrue(case_check(string_2, string_1))

    def test_if_upper(self):
        """
        Tests if given parameters are upper.
        """
        string_1 = "ABC"
        string_2 = "DEF"
        self.assertTrue(case_check(string_1, string_2))
        self.assertTrue(case_check(string_2, string_1))

    def test_if_different_cases(self):
        """
        Tests if given parameters are of different cases and function returns False.
        """
        string_1 = "ABC"
        string_2 = "def"
        self.assertFalse(case_check(string_1, string_2))
        self.assertFalse(case_check(string_2, string_1))

    def test_if_both_strings(self):
        """
        Tests if both parameters are strings.
        """
        string_1 = 123
        string_2 = "abc"
        self.assertEqual(case_check(string_1, string_2), "-1")
        self.assertEqual(case_check(string_2, string_1), "-1")

    def test_special_chars(self):
        """
        Tests if returns False if one parameter contains special characters.
        """
        string_1 = "abc"
        string_2 = "!@#$"
        self.assertEqual(case_check(string_1, string_2), "-1")
        self.assertEqual(case_check(string_2, string_1), "-1")
