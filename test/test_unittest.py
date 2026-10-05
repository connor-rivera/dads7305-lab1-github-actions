import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(5, 0), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(2, 3), -1)
        self.assertEqual(calculator.subtract(5, 0), 5)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(5, 0), 0)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-1, -1), 1)

    def test_add_three_nums(self):
        self.assertEqual(calculator.add_three_nums(2, 3, 5), 10)
        self.assertEqual(calculator.add_three_nums(5, 0, -1), 4)
        self.assertEqual(calculator.add_three_nums(-1, -1, -1), -3)
        self.assertEqual(calculator.add_three_nums(-1, -1, 100), 98)

    def test_divide(self):
        self.assertEqual(calculator.divide(6, 3), 2.0)
        self.assertEqual(calculator.divide(7, 2), 3.5)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(2, -1), 0.5)

    def test_average(self):
        self.assertEqual(calculator.average([2, 4, 6]), 4.0)
        self.assertEqual(calculator.average([7]), 7.0)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculator.add("a", 1)
        with self.assertRaises(ValueError):
            calculator.add_three_nums(1, 2, "3")
        with self.assertRaises(ValueError):
            calculator.divide(1, 0)
        with self.assertRaises(ValueError):
            calculator.average([])


if __name__ == '__main__':
    unittest.main()