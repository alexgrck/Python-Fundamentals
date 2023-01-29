import unittest
import infinite_randoms


class TestInfiniteRandoms(unittest.TestCase):
    def tearDown(self):
        infinite_randoms.history = []

    def test_0_if_generates(self):
        """
        Tests if it generates numbers and stores them in history.
        """
        next(infinite_randoms.random_number())
        next(infinite_randoms.random_number())
        next(infinite_randoms.random_number())
        self.assertEqual(len(infinite_randoms.history), 3)

    def test_1_if_generates_ints(self):
        """
        Tests if it generates integers.
        """
        next(infinite_randoms.random_number())
        next(infinite_randoms.random_number())
        next(infinite_randoms.random_number())
        for number in infinite_randoms.history:
            self.assertTrue(isinstance(number, int))
