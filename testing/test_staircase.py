import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from functions.staircase import staircase


class StairCaseTest(unittest.TestCase):
    def test_negative_input(self):
        self.assertEqual(staircase(-5, "#"), "Invalid input!")

    def test_zero_input(self):
        self.assertEqual(staircase(0, "#"), "Invalid input!")

    def test_exceeding_max_limit(self):
        self.assertEqual(staircase(31, "#"), "Invalid input!")

    def test_min_valid_input(self):
        self.assertEqual(staircase(1, "#"), "#")

    def test_max_valid_input(self):
        result = staircase(30, "#")
        self.assertTrue(result.startswith(" " * 29 + "#"))
        self.assertTrue(result.endswith("#" * 30))

    def test_middle_range_input(self):
        expected_output = "  #\n ##\n###"
        self.assertEqual(staircase(3, "#"), expected_output)

    def test_custom_character(self):
        expected_output = "  @\n @@\n@@@"
        self.assertEqual(staircase(3, "@"), expected_output)

    def test_spaces_as_character(self):
        expected_output = "   \n   \n   "
        self.assertEqual(staircase(3, " "), expected_output)


if __name__ == "__main__":
    unittest.main()
