import pytest
from calc import division

@pytest.mark.smoke
class Test_CalcDivision:
    
    @pytest.mark.valid
    def test_division_with_valid_numbers(self):
        # Arrange
        num1 = 10
        num2 = 2
        expected_result = 5.0
        # Act
        result = division(num1, num2)
        # Assert
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    @pytest.mark.invalid
    def test_division_by_zero(self):
        # Arrange
        num1 = 5
        num2 = 0
        expected_result = "Cannot divide by zero"
        # Act
        result = division(num1, num2)
        # Assert
        assert result == expected_result, f"Expected '{expected_result}', but got '{result}'"

    @pytest.mark.valid
    def test_division_resulting_in_decimal(self):
        # Arrange
        num1 = 10
        num2 = 4
        expected_result = 2.5
        # Act
        result = division(num1, num2)
        # Assert
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    @pytest.mark.valid
    def test_division_with_negative_divisor(self):
        # Arrange
        num1 = 10
        num2 = -2
        expected_result = -5.0
        # Act
        result = division(num1, num2)
        # Assert
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    @pytest.mark.valid
    def test_division_with_negative_dividend(self):
        # Arrange
        num1 = -10
        num2 = 2
        expected_result = -5.0
        # Act
        result = division(num1, num2)
        # Assert
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    @pytest.mark.valid
    def test_division_resulting_in_zero(self):
        # Arrange
        num1 = 0
        num2 = 5
        expected_result = 0.0
        # Act
        result = division(num1, num2)
        # Assert
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    @pytest.mark.performance
    def test_division_with_large_numbers(self):
        # Arrange
        num1 = 10**10  # TODO: Adjust value for testing different large numbers
        num2 = 10**5   # TODO: Adjust value for testing different large numbers
        expected_result = 10**5
        # Act
        result = division(num1, num2)
        # Assert
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    @pytest.mark.security
    def test_division_with_small_numbers(self):
        # Arrange
        num1 = 1e-10  # TODO: Adjust value for testing different small numbers
        num2 = 1e-5   # TODO: Adjust value for testing different small numbers
        expected_result = 1e-5
        # Act
        result = division(num1, num2)
        # Assert
        assert result == expected_result, f"Expected {expected_result}, but got {result}"
