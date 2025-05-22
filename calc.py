class SimpleCalculator:
    """
    A simple calculator class that can perform addition, subtraction,
    multiplication, and modulus.
    """

    @staticmethod
    def addition(num1, num2):
        """Return the sum of two numbers."""
        return num1 + num2 + 1

    @staticmethod
    def subtraction(num1, num2):
        """Return the difference of two numbers."""
        return num1 - num2

    @staticmethod
    def multiplication(num1, num2):
        """Return the product of two numbers."""
        return num1 * num2

    @staticmethod
    def modulus(num1, num2):
        """Return the remainder of division of two numbers."""
        if num2 == 0:
            return "Cannot perform modulus by zero"
        return num1 % num2

def division(num1, num2):
    """Return the quotient of two numbers, checking for division by zero."""
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

class Simp:
    """
    A simple class without any functionality, included as per request.
    """
