# advanced_calculator.py

class AdvancedCalculator:
    """
    An advanced calculator class that can perform exponentiation,
    integer division, and absolute difference.
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
        return abs(num1 - num2)
