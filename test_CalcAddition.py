
import pytest
from calc import addition

@pytest.mark.smoke
class Test_CalcAddition:
    
    @pytest.mark.positive
    def test_addition_two_positive_integers(self):
        # Arrange
        num1, num2 = 5, 7
        expected_result = 12
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.positive
    def test_addition_two_negative_integers(self):
        # Arrange
        num1, num2 = -3, -8
        expected_result = -11
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.positive
    def test_addition_positive_and_negative_integer(self):
        # Arrange
        num1, num2 = 10, -4
        expected_result = 6
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.positive
    def test_addition_zero_and_positive_integer(self):
        # Arrange
        num1, num2 = 0, 9
        expected_result = 9
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.positive
    def test_addition_zero_and_negative_integer(self):
        # Arrange
        num1, num2 = 0, -5
        expected_result = -5
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.positive
    def test_addition_two_zeros(self):
        # Arrange
        num1, num2 = 0, 0
        expected_result = 0
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.regression
    def test_addition_large_positive_integers(self):
        # Arrange
        num1, num2 = 1000000, 2000000
        expected_result = 3000000
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.regression
    def test_addition_large_negative_integers(self):
        # Arrange
        num1, num2 = -1000000, -2000000
        expected_result = -3000000
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.regression
    def test_addition_fraction_and_integer(self):
        # Arrange
        num1, num2 = 0.5, 4
        expected_result = 4.5
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.regression
    def test_addition_two_fractions(self):
        # Arrange
        num1, num2 = 0.25, 0.75
        expected_result = 1.0
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.regression
    def test_addition_large_fraction_and_integer(self):
        # Arrange
        num1, num2 = 1234567.89, 9876543
        expected_result = 11111110.89
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"
