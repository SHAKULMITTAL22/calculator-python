import pytest
from calc import subtraction

@pytest.mark.smoke
class Test_SimpleCalculatorSubtraction:

    @pytest.mark.valid
    @pytest.mark.positive
    def test_subtract_positive_integers(self):
        # Arrange
        num1 = 10
        num2 = 5
        expected_result = 5
        # Act
        result = subtraction(num1, num2)
        # Assert
        assert result == expected_result

    @pytest.mark.regression
    @pytest.mark.valid
    @pytest.mark.positive
    def test_subtract_smaller_from_larger(self):
        # Arrange
        num1 = 15
        num2 = 7
        expected_result = 8
        # Act
        result = subtraction(num1, num2)
        # Assert
        assert result == expected_result

    @pytest.mark.regression
    @pytest.mark.valid
    @pytest.mark.negative
    def test_subtract_larger_from_smaller(self):
        # Arrange
        num1 = 4
        num2 = 9
        expected_result = -5
        # Act
        result = subtraction(num1, num2)
        # Assert
        assert result == expected_result

    @pytest.mark.regression
    @pytest.mark.valid
    @pytest.mark.positive
    def test_subtract_zero(self):
        # Arrange
        num1 = 23
        num2 = 0
        expected_result = 23
        # Act
        result = subtraction(num1, num2)
        # Assert
        assert result == expected_result

    @pytest.mark.smoke
    @pytest.mark.valid
    @pytest.mark.positive
    def test_subtract_same_number(self):
        # Arrange
        num1 = 7
        num2 = 7
        expected_result = 0
        # Act
        result = subtraction(num1, num2)
        # Assert
        assert result == expected_result

    @pytest.mark.regression
    @pytest.mark.valid
    @pytest.mark.positive
    def test_subtract_negative_numbers(self):
        # Arrange
        num1 = -4
        num2 = -6
        expected_result = 2
        # Act
        result = subtraction(num1, num2)
        # Assert
        assert result == expected_result

    @pytest.mark.smoke
    @pytest.mark.valid
    @pytest.mark.positive
    def test_subtract_mixed_positive_and_negative(self):
        # Arrange
        num1 = 8
        num2 = -3
        expected_result = 11
        # Act
        result = subtraction(num1, num2)
        # Assert
        assert result == expected_result

    @pytest.mark.regression
    @pytest.mark.valid
    @pytest.mark.positive
    def test_subtract_floating_point_numbers(self):
        # Arrange
        num1 = 10.5
        num2 = 3.2
        expected_result = 7.3
        # Act
        result = subtraction(num1, num2)
        # Assert
        assert result == expected_result

    @pytest.mark.regression
    @pytest.mark.valid
    @pytest.mark.positive
    def test_subtract_resulting_in_zero(self):
        # Arrange
        num1 = 5
        num2 = 5
        expected_result = 0
        # Act
        result = subtraction(num1, num2)
        # Assert
        assert result == expected_result

    @pytest.mark.performance
    @pytest.mark.valid
    @pytest.mark.positive
    def test_subtract_large_numbers(self):
        # Arrange
        num1 = 10**12    # TODO: Adjust test value if needed
        num2 = 10**11    # TODO: Adjust test value if needed
        expected_result = 9 * 10**11
        # Act
        result = subtraction(num1, num2)
        # Assert
        assert result == expected_result

    @pytest.mark.valid
    @pytest.mark.positive
    def test_subtract_small_floating_point(self):
        # Arrange
        num1 = 0.0005
        num2 = 0.0003
        expected_result = 0.0002
        # Act
        result = subtraction(num1, num2)
        # Assert
        assert result == pytest.approx(expected_result, rel=1e-7)
