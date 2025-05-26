import pytest
from calc import SimpleCalculator

class Test_SimpleCalculatorSubtraction:

    @pytest.mark.positive
    def test_basic_subtraction(self):
        # Arrange
        num1 = 10
        num2 = 5

        # Act
        result = SimpleCalculator.subtraction(num1, num2)

        # Assert
        assert result == 5

    @pytest.mark.positive
    def test_subtraction_with_zero(self):
        # Arrange
        num1 = 7
        num2 = 0

        # Act
        result = SimpleCalculator.subtraction(num1, num2)

        # Assert
        assert result == 7

    @pytest.mark.negative
    def test_subtraction_resulting_negative(self):
        # Arrange
        num1 = 3
        num2 = 8

        # Act
        result = SimpleCalculator.subtraction(num1, num2)

        # Assert
        assert result == -5

    @pytest.mark.negative
    def test_subtraction_with_negative_numbers(self):
        # Arrange
        num1 = -5
        num2 = -3

        # Act
        result = SimpleCalculator.subtraction(num1, num2)

        # Assert
        assert result == -2

    @pytest.mark.floating
    def test_subtraction_with_floating_point_numbers(self):
        # Arrange
        num1 = 10.5
        num2 = 3.2

        # Act
        result = SimpleCalculator.subtraction(num1, num2)

        # Assert
        assert result == pytest.approx(7.3)

    @pytest.mark.large
    def test_subtraction_with_large_numbers(self):
        # Arrange
        num1 = 10**10
        num2 = 1

        # Act
        result = SimpleCalculator.subtraction(num1, num2)

        # Assert
        assert result == 9999999999

    @pytest.mark.mixed
    def test_subtraction_with_mixed_types(self):
        # Arrange
        num1 = 10
        num2 = 3.5

        # Act
        result = SimpleCalculator.subtraction(num1, num2)

        # Assert
        assert result == pytest.approx(6.5)

    @pytest.mark.positive
    def test_subtraction_with_identical_numbers(self):
        # Arrange
        num1 = 7
        num2 = 7

        # Act
        result = SimpleCalculator.subtraction(num1, num2)

        # Assert
        assert result == 0
