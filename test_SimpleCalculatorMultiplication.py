# Import necessary modules and classes
import pytest
from calc import SimpleCalculator

# Define the test class
class Test_SimpleCalculatorMultiplication:

    @pytest.mark.positive
    def test_multiplication_positive_integers(self):
        # Arrange
        num1 = 5
        num2 = 4
        # Act
        result = SimpleCalculator.multiplication(num1, num2)
        # Assert
        assert result == 20

    @pytest.mark.negative
    def test_multiplication_with_one_negative_integer(self):
        # Arrange
        num1 = 6
        num2 = -3
        # Act
        result = SimpleCalculator.multiplication(num1, num2)
        # Assert
        assert result == -18

    @pytest.mark.positive
    def test_multiplication_two_negative_integers(self):
        # Arrange
        num1 = -7
        num2 = -2
        # Act
        result = SimpleCalculator.multiplication(num1, num2)
        # Assert
        assert result == 14

    @pytest.mark.edgecase
    def test_multiplication_with_zero(self):
        # Arrange
        num1 = 0
        num2 = 10
        # Act
        result = SimpleCalculator.multiplication(num1, num2)
        # Assert
        assert result == 0

    @pytest.mark.edgecase
    def test_multiplication_both_operands_zero(self):
        # Arrange
        num1 = 0
        num2 = 0
        # Act
        result = SimpleCalculator.multiplication(num1, num2)
        # Assert
        assert result == 0

    @pytest.mark.performance
    def test_multiplication_large_numbers(self):
        # Arrange
        num1 = 10**10
        num2 = 10**8
        # Act
        result = SimpleCalculator.multiplication(num1, num2)
        # Assert
        assert result == 10**18

    @pytest.mark.valid
    def test_multiplication_with_floats(self):
        # Arrange
        num1 = 2.5
        num2 = 4.0
        # Act
        result = SimpleCalculator.multiplication(num1, num2)
        # Assert
        assert result == 10.0

    @pytest.mark.valid
    def test_multiplication_positive_and_fractional_negative(self):
        # Arrange
        num1 = 3.6
        num2 = -1.5
        # Act
        result = SimpleCalculator.multiplication(num1, num2)
        # Assert
        assert result == -5.4

    @pytest.mark.valid
    def test_multiplication_small_fractional_numbers(self):
        # Arrange
        num1 = 1e-7
        num2 = 1e-8
        # Act
        result = SimpleCalculator.multiplication(num1, num2)
        # Assert
        assert result == 1e-15

    @pytest.mark.performance
    def test_multiplication_mixed_magnitudes(self):
        # Arrange
        num1 = 1e10
        num2 = 1e-10
        # Act
        result = SimpleCalculator.multiplication(num1, num2)
        # Assert
        assert result == 1.0

    @pytest.mark.valid
    def test_multiplication_limits_of_precision(self):
        # Arrange
        num1 = 0.3333333333
        num2 = 0.6666666667
        # Act
        result = SimpleCalculator.multiplication(num1, num2)
        # Assert
        assert pytest.approx(result, rel=1e-10) == 0.2222222222  # Use pytest.approx for floating-point precision
