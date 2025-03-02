from functions.FIZZBUZZ import get_fizzbuzz
import unittest


class PrimeListTest(unittest.TestCase):
    def test_give_neg_2_is_empty_str(self):
        number = -2
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "")

    def test_give_neg_201717_is_fizz(self):
        number = 201717
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "Fizz")

    def test_give_465_is_fizzbuzz(self):
        number = 465
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "FizzBuzz")

    def test_give_neg_1940_is_buzz(self):
        number = -1940
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "Buzz")

    def test_give_neg_15_is_fizzbuzz(self):
        number = -15
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "FizzBuzz")

    def test_give_neg_137_is_empty_str(self):
        number = -137
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "")

    def test_give_neg_1324_is_empty_str(self):
        number = -1324
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "")

    def test_give_neg_80_is_buzz(self):
        number = -80
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "Buzz")

    def test_give_neg_723542_is_empty_str(self):
        number = -723542
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "")

    def test_give_750_is_fizzbuzz(self):
        number = 750
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "FizzBuzz")

    def test_give_14_is_empty_str(self):
        number = 14
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "")

    def test_give_791_is_empty_str(self):
        number = 791
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "")

    def test_give_2478_is_fizz(self):
        number = 2478
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "Fizz")

    def test_give_10569_is_fizz(self):
        number = 10569
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "Fizz")

    def test_give_545_is_buzz(self):
        number = 545
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "Buzz")

    def test_give_960_is_fizzbuzz(self):
        number = 960
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb, "FizzBuzz")
