import pytest
from calc import multiplication

class Test_SimpleCalculatorMultiplication:
    
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_multiplication_positive_integers(self):
        # Arrange
        num1 = 5
        num2 = 4
        expected = 20
        # Act
        result = multiplication(num1, num2)
        # Assert
        assert result == expected

    @pytest.mark.regression
    @pytest.mark.negative
    def test_multiplication_with_one_negative_integer(self):
        # Arrange
        num1 = 6
        num2 = -3
        expected = -18
        # Act
        result = multiplication(num1, num2)
        # Assert
        assert result == expected

    @pytest.mark.regression
    @pytest.mark.positive
    def test_multiplication_two_negative_integers(self):
        # Arrange
        num1 = -7
        num2 = -2
        expected = 14
        # Act
        result = multiplication(num1, num2)
        # Assert
        assert result == expected

    @pytest.mark.smoke
    @pytest.mark.negative
    def test_multiplication_with_zero(self):
        # Arrange
        num1 = 0
        num2 = 10
        expected = 0
        # Act
        result = multiplication(num1, num2)
        # Assert
        assert result == expected

    @pytest.mark.smoke
    @pytest.mark.positive
    def test_multiplication_both_operands_zero(self):
        # Arrange
        num1 = 0
        num2 = 0
        expected = 0
        # Act
        result = multiplication(num1, num2)
        # Assert
        assert result == expected

    @pytest.mark.performance
    def test_multiplication_large_numbers(self):
        # Arrange
        num1 = 10**10
        num2 = 10**8
        expected = 10**18
        # Act
        result = multiplication(num1, num2)
        # Assert
        assert result == expected

    @pytest.mark.valid
    def test_multiplication_with_floats(self):
        # Arrange
        num1 = 2.5
        num2 = 4.0
        expected = 10.0
        # Act
        result = multiplication(num1, num2)
        # Assert
        assert result == expected

    @pytest.mark.valid
    def test_multiplication_positive_and_fractional_negative(self):
        # Arrange
        num1 = 3.6
        num2 = -1.5
        expected = -5.4
        # Act
        result = multiplication(num1, num2)
        # Assert
        assert result == expected

    @pytest.mark.security
    def test_multiplication_small_fractional_numbers(self):
        # Arrange
        num1 = 1e-7
        num2 = 1e-8
        expected = 1e-15
        # Act
        result = multiplication(num1, num2)
        # Assert
        assert result == expected

    @pytest.mark.stress
    def test_multiplication_mixed_magnitudes(self):
        # Arrange
        num1 = 1e10
        num2 = 1e-10
        expected = 1.0
        # Act
        result = multiplication(num1, num2)
        # Assert
        assert result == expected

    @pytest.mark.precision
    def test_multiplication_limits_of_precision(self):
        # Arrange
        num1 = 0.3333333333
        num2 = 0.6666666667
        expected = pytest.approx(0.2222222222, rel=1e-9)  # Adjust delta if necessary
        # Act
        result = multiplication(num1, num2)
        # Assert
        assert result == expected
