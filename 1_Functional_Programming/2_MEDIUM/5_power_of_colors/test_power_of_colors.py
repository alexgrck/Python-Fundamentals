import unittest
import random
from power_of_colors import random_hex_colors, random_rgb_colors, convert_colors


class TestPowerOfColors(unittest.TestCase):
    def test_random_hex(self):
        """
        Tests if function returns expected random hex value when random.seed
        is set  e.g. to 3.
        """
        random.seed(3)
        self.assertEqual(random_hex_colors(), "#79d67f")

    def test_random_rgb(self):
        """
        Tests if function returns expected random rgb value when random.seed
        is set  e.g. to 3.
        """
        random.seed(3)
        self.assertEqual(random_rgb_colors(), (121, 66, 189))

    def test_convert_from_rgb(self):
        """
        Tests if function returns correct hex value when converting from rgb.
        """
        sample = (213, 45, 94)
        self.assertEqual(convert_colors(sample), "#d52d5e")

    def test_convert_from_hex(self):
        """
        Tests if function returns correct rgb value when converting from hex.
        """
        sample = "#32f4a2"
        self.assertEqual(convert_colors(sample), (50, 244, 162))

    def test_incorrect_converting(self):
        """
        Tests if function returns proper message when input is incorrect
        """
        sample_1 = (256, 45, 94)
        sample_2 = "#3791039"
        self.assertEqual(convert_colors(sample_1), "Incorrect input value.")
        self.assertEqual(convert_colors(sample_2), "Incorrect input value.")
