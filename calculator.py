import math


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the division result."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


def square_root(number):
    """Return the square root of a non-negative number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(number)


def factorial(number):
    """Return the factorial of a non-negative integer."""
    if not isinstance(number, int):
        raise TypeError("Factorial requires an integer.")

    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    return math.factorial(number)


# Simple program to test the calculator manually
if __name__ == "__main__":
    print("===== Python Calculator =====")

    print("Addition:", add(14, 5))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(10, 5))
    print("Division:", divide(10, 5))
    print("Power:", power(2, 3))
    print("Square Root:", square_root(25))
    print("Factorial:", factorial(5))
     
     
import unittest

