import unittest
from Calculator import Calculator

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        """This method runs before each test."""
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(10, self.calc.add(7, 3), "Addition is incorrect")

    def test_subtract(self):
        self.assertEqual(4, self.calc.subtract(7, 3), "Subtraction is incorrect")

    def test_multiply(self):
        self.assertEqual(21, self.calc.multiply(7, 3), "Multiplication is incorrect")

    def test_square_root(self):
        self.assertEqual(5, self.calc.square_root(25), "Square root calculation is incorrect")

    def test_negative_square_root(self):
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

if __name__ == '__main__':
    unittest.main()
