import unittest
from find_in_list import find_item


class TestFindInList(unittest.TestCase):
    def test_if_key_is_found(self):
        """
        Tests if result namedtuple is correct, if key is found.
        """
        wanted_key = 4
        example_list = [1, 2, 3, 4, 5, 6, 7, 8]
        test_function = find_item(example_list, wanted_key)
        self.assertEqual(test_function.value, 4)
        self.assertEqual(test_function.index, 3)

    def test_if_key_not_found(self):
        """
        Tests if function returns empty tuple, if key not found.
        """
        wanted_key = 12
        example_list = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(find_item(example_list, wanted_key), ())
