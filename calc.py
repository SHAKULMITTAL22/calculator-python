class SimpleCalculator:
    """
    A simple calculator class that can perform addition, subtraction,
    multiplication, and division.
    """

    @staticmethod
    def addition(num1, num2):
        """Return the sum of two numbers."""
        return num1 + num2

    @staticmethod
    def subtraction(num1, num2):
        """Return the difference of two numbers."""
        return num1 - num2

    @staticmethod
    def multiplication(num1, num2):
        """Return the product of two numbers."""
        return num1 * num2

def calculator(num1, num2, operation):
    """Directs to the appropriate function based on the operation requested using the SimpleCalculator class."""
    if operation == '+':
        return SimpleCalculator.addition(num1, num2)
    elif operation == '-':
        return SimpleCalculator.subtraction(num1, num2)
    elif operation == '*':
        return SimpleCalculator.multiplication(num1, num2)
    else:
        return "Invalid operation"

@staticmethod
def division(num1, num2):
    """Return the quotient of two numbers, checks for division by zero."""
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1 / num2

class Simp:
    """
    A simple calculator class that can perform addition, subtraction,
    multiplication, and division.
    """

# Example of using the calculator function:
result = calculator(10, 5, '*')
print(result)  # Output should be 50
