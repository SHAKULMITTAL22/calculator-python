import pytest
from calc import addition

@pytest.mark.valid
class Test_SimpleCalculatorAddition:

    @pytest.mark.smoke
    @pytest.mark.positive
    def test_addition_positive_integers(self):
        # Arrange
        num1 = 5
        num2 = 3
        expected_result = 8
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.regression
    @pytest.mark.negative
    def test_addition_negative_integers(self):
        # Arrange
        num1 = -7
        num2 = -5
        expected_result = -12
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.regression
    @pytest.mark.valid
    def test_addition_mixed_sign_integers(self):
        # Arrange
        num1 = 10
        num2 = -3
        expected_result = 7
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.smoke
    @pytest.mark.valid
    def test_addition_with_zero(self):
        # Arrange
        num1 = 0
        num2 = 11
        expected_result = 11
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.smoke
    @pytest.mark.valid
    def test_addition_two_zeros(self):
        # Arrange
        num1 = 0
        num2 = 0
        expected_result = 0
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.performance
    @pytest.mark.valid
    def test_addition_large_integers(self):
        # Arrange
        num1 = 999999999
        num2 = 888888888
        expected_result = 1888888887
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == expected_result, f"Expected {expected_result}, got {result}"

    @pytest.mark.valid
    @pytest.mark.regression
    def test_addition_floating_points(self):
        # Arrange
        num1 = 3.5
        num2 = 4.3
        expected_result = 7.8
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == pytest.approx(expected_result), f"Expected {expected_result}, got {result}"

    @pytest.mark.valid
    @pytest.mark.regression
    def test_addition_integer_and_float(self):
        # Arrange
        num1 = 1000000
        num2 = 0.75
        expected_result = 1000000.75
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == pytest.approx(expected_result), f"Expected {expected_result}, got {result}"

    @pytest.mark.security
    @pytest.mark.valid
    def test_addition_negative_floats(self):
        # Arrange
        num1 = -2.5
        num2 = -3.5
        expected_result = -6.0
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == pytest.approx(expected_result), f"Expected {expected_result}, got {result}"

    @pytest.mark.performance
    @pytest.mark.valid
    def test_addition_tiny_floating_points(self):
        # Arrange
        num1 = 0.0001
        num2 = 0.0009
        expected_result = 0.001
        
        # Act
        result = addition(num1, num2)
        
        # Assert
        assert result == pytest.approx(expected_result), f"Expected {expected_result}, got {result}"
