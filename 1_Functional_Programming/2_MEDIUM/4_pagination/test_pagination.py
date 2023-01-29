import unittest
from pagination import paginate


class TestPagination(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_input = list(range(300))

    @classmethod
    def tearDownClass(cls):
        cls.doCleanups

    def test_first_page(self):
        """
        Tests if function returns correct output for the first page.
        """
        sample_output = [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
        ]
        self.assertEqual(paginate(self.sample_input, 26, 0), sample_output)

    def test_middle_page(self):
        """
        Tests if function returns correct output for the random middle page.
        """
        sample_output = [
            182,
            183,
            184,
            185,
            186,
            187,
            188,
            189,
            190,
            191,
            192,
            193,
            194,
            195,
            196,
            197,
            198,
            199,
            200,
            201,
            202,
            203,
            204,
            205,
            206,
            207,
        ]
        self.assertEqual(paginate(self.sample_input, 26, 7), sample_output)

    def test_last_page(self):
        """
        Tests if function returns correct output for the last page.
        """
        sample_output = [
            286,
            287,
            288,
            289,
            290,
            291,
            292,
            293,
            294,
            295,
            296,
            297,
            298,
            299,
        ]
        self.assertEqual(paginate(self.sample_input, 26, 11), sample_output)

    def test_more_pages(self):
        """
        Tests if function returns False if checked page number is out of range
        of page numbers (function should return empty list).
        """
        self.assertFalse(paginate(self.sample_input, 26, 14))

    def test_0_0(self):
        """
        Tests if function returns False if max_elements_on_page == 0 and
        page_number == 0 (function should return empty list).
        """
        self.assertFalse(paginate(self.sample_input, 0, 0))

    def test_all_content(self):
        """
        Tests if function returns the (whole content - 1) == 299
        if max_elements_on_page == -1 and page_number == 0.
        """
        self.assertEqual(paginate(self.sample_input, -1, 0), self.sample_input[:-1])
