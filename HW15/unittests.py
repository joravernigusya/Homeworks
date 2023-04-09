import unittest
import sys
from HW4 import mult_nums, field_years, sum_of_numbers
from HW3 import strip_string


class TestMultiplyNumbers(unittest.TestCase):
    def test_input_int(self):
        self.assertEqual(mult_nums(5), 120, "N != 120")

    def test_input_negative(self):
        with self.assertRaises(TypeError):
            mult_nums(-5)

    def test_input_one(self):
        self.assertEqual(mult_nums(1), 1)

    def test_input_zero(self):
        self.assertEqual(mult_nums(0), 0)

    def test_input_max(self):
        with self.assertRaises(OverflowError):
            mult_nums(sys.maxsize)

    def test_input_over_max(self):
        with self.assertRaises(OverflowError):
            mult_nums(sys.maxsize + 1)

    def test_input_min(self):
        with self.assertRaises(TypeError):
            mult_nums(sys.float_info.min)

    #
    def test_input_float(self):
        with self.assertRaises(TypeError):
            mult_nums(7.3)


class TestFieldYears(unittest.TestCase):
    def test_correct_values(self):
        self.assertEqual(field_years(3, 6), 4)
        self.assertEqual(field_years(10, 11), 6)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            field_years(-1, 10)
        with self.assertRaises(ValueError):
            field_years(1, -10)
        with self.assertRaises(ValueError):
            field_years(-1, -10)

    def test_non_numeric_values(self):
        with self.assertRaises(ValueError):
            field_years("1", 10)
        with self.assertRaises(ValueError):
            field_years(1, "10")
        with self.assertRaises(ValueError):
            field_years("1", "10")

    def test_s1_greater_than_s2(self):
        with self.assertRaises(ValueError):
            field_years(10, 1)


class TestSumOfNumbers(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(sum_of_numbers(4, 8), 30)

    def test_a_equals_b(self):
        self.assertEqual(sum_of_numbers(5, 5), 5)

    def test_large_numbers(self):
        self.assertEqual(sum_of_numbers(10000, 100000), 4950055000)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_numbers(-5, 5), 0)

    def test_zero_values(self):
        self.assertEqual(sum_of_numbers(0, 0), 0)


class TestStripString(unittest.TestCase):
    def test_strip_left(self):
        self.assertEqual(strip_string("  some text"), "some text")

    def test_strip_right(self):
        self.assertEqual(strip_string("some text  "), "some text")

    def test_strip_both(self):
        self.assertEqual(strip_string("  some text  "), "some text")

    def test_one_space(self):
        self.assertEqual(strip_string(" "), "")

    def test_no_spaces(self):
        self.assertEqual(strip_string("some text"), "some text")
