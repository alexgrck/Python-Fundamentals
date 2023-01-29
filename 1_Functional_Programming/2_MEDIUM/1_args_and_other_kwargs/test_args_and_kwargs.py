import unittest
from args_and_other_kwargs import list_parameters


class TestArgsAndKwargs(unittest.TestCase):
    def test_if_args_work(self):
        """
        Tests if function works if *args given as the only parameter.
        """
        self.assertEqual(
            list_parameters("apple", "peach", "pear", "banana"),
            {0: "apple", 1: "peach", 2: "pear", 3: "banana"},
        )

    def test_if_kwargs_work(self):
        """
        Tests if function works if **kwargs given as the only parameter.
        """
        self.assertEqual(
            list_parameters(
                first="apple", second="peach", third="pear", fourth="banana"
            ),
            {"first": "apple", "second": "peach", "third": "pear", "fourth": "banana"},
        )

    def test_if_function_works(self):
        """
        Tests if function works if *args and **kwargs given as parameters.
        """
        self.assertEqual(
            list_parameters(
                "apple",
                "peach",
                "pear",
                "banana",
                first="apple",
                second="peach",
                third="pear",
                fourth="banana",
            ),
            {
                0: "apple",
                1: "peach",
                2: "pear",
                3: "banana",
                "first": "apple",
                "second": "peach",
                "third": "pear",
                "fourth": "banana",
            },
        )
