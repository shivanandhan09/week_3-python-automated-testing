import unittest
import calculator


class TestCalculator(unittest.TestCase):

    # Test addition
    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(-10, 5), -5)
        self.assertEqual(calculator.add(0, 5), 5)

    # Test subtraction
    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(5, 10), -5)
        self.assertEqual(calculator.subtract(0, 5), -5)

    # Test multiplication
    def test_multiply(self):
        self.assertEqual(calculator.multiply(10, 5), 50)
        self.assertEqual(calculator.multiply(-2, 5), -10)
        self.assertEqual(calculator.multiply(0, 10), 0)

    # Test division
    def test_divide(self):
        self.assertEqual(calculator.divide(10, 5), 2)
        self.assertEqual(calculator.divide(9, 3), 3)

    # Test division by zero
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

    # Test power
    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(5, 2), 25)
        self.assertEqual(calculator.power(10, 0), 1)

    # Test square root
    def test_square_root(self):
        self.assertEqual(calculator.square_root(25), 5)
        self.assertEqual(calculator.square_root(0), 0)

    # Test square root of negative number
    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-25)

    # Test factorial
    def test_factorial(self):
        self.assertEqual(calculator.factorial(5), 120)
        self.assertEqual(calculator.factorial(0), 1)
        self.assertEqual(calculator.factorial(3), 6)

    # Test factorial with negative number
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            calculator.factorial(-5)

    # Test factorial with non-integer
    def test_factorial_invalid_type(self):
        with self.assertRaises(TypeError):
            calculator.factorial(5.5)


# Run all tests
if __name__ == "__main__":
    unittest.main()