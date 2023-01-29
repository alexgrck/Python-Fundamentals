import unittest
import random
from chunks import to_chunks


class TestChunks(unittest.TestCase):
    def setUp(self):
        self.alphabet = [x for x in "abcdefghijklmnoprstuwxyz"]

    def test_to_chunks(self):
        """
        Tests if function returns correct chunks if random.seed set to 3.
        """
        random.seed(3)
        self.assertEqual(
            to_chunks(self.alphabet),
            [
                ["a", "b", "c", "d", "e"],
                ["f", "g", "h", "i", "j"],
                ["k", "l", "m", "n", "o", "p"],
                ["r", "s", "t", "u"],
                ["w", "x", "y", "z"],
            ],
        )

    def test_if_chunk_lengths_correct(self):
        chunks_func = to_chunks(self.alphabet)
        lengths = [4 <= len(chunk) <= 7 for chunk in chunks_func]
        self.assertTrue(all(lengths))
