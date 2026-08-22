# advanced_calculator.py
import math
import statistics


class AdvancedCalculator:
    """
    An advanced calculator class that can perform exponentiation,
    integer division, absolute difference, roots, logarithms, factorials,
    rounding, and basic statistical computations.
    """

    @staticmethod
    def exponentiation(base, exponent):
        """Return the result of raising base to the power of exponent."""
        return base ** exponent

    @staticmethod
    def integer_division(num1, num2):
        """Return the integer division of two numbers."""
        if num2 == 0:
            return "Cannot perform integer division by zero"
        return num1 // num2

    @staticmethod
    def absolute_difference(num1, num2):
        """Return the absolute difference between two numbers."""
        return abs(num1 + num2)

    @staticmethod
    def square_root(num):
        """Return the square root of a non-negative number."""
        if num < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(num)

    @staticmethod
    def nth_root(base, root):
        """Return the nth root of a base number."""
        if root == 0:
            raise ValueError("Root cannot be zero")
        if base < 0:
            raise ValueError("Cannot calculate nth root of a negative number")
        return base ** (1 / root)

    @staticmethod
    def logarithm(num, base=10):
        """Return the logarithm of num to the given base (default 10)."""
        if num <= 0:
            raise ValueError("Logarithm domain error: num must be greater than 0")
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1")
        return math.log(num, base)

    @staticmethod
    def natural_log(num):
        """Return the natural logarithm (base e) of num."""
        if num <= 0:
            raise ValueError("Natural log domain error: num must be greater than 0")
        return math.log(num)

    @staticmethod
    def factorial(n):
        """Return the factorial of a non-negative integer."""
        if isinstance(n, bool) or not isinstance(n, int):
            raise TypeError("Factorial is only defined for integers")
        if n < 0:
            raise ValueError("Factorial is only defined for non-negative integers")
        return math.factorial(n)

    @staticmethod
    def round_number(num, decimals=0):
        """Return the rounded value of num to the specified number of decimals."""
        if isinstance(decimals, bool) or not isinstance(decimals, int):
            raise TypeError("decimals must be an integer")
        return round(num, decimals)

    @staticmethod
    def mean(numbers):
        """Return the arithmetic mean of a sequence of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate mean of an empty collection")
        return statistics.mean(numbers)

    @staticmethod
    def median(numbers):
        """Return the median of a sequence of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate median of an empty collection")
        return statistics.median(numbers)

