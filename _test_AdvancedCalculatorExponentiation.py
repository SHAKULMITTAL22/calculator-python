import pytest
from calc_advance import AdvancedCalculator

class Test_AdvancedCalculatorExponentiation:

    @pytest.mark.smoke
    @pytest.mark.positive
    def test_basic_positive_exponentiation(self):
        # Act
        result = AdvancedCalculator.exponentiation(2, 3)
        # Assert
        assert result == 8

    @pytest.mark.positive
    def test_positive_base_zero_exponent(self):
        # Act
        result = AdvancedCalculator.exponentiation(5, 0)
        # Assert
        assert result == 1

    @pytest.mark.positive
    def test_base_one_with_any_exponent(self):
        # Act
        result = AdvancedCalculator.exponentiation(1, 4)
        # Assert
        assert result == 1

    @pytest.mark.positive
    def test_negative_base_even_exponent(self):
        # Act
        result = AdvancedCalculator.exponentiation(-2, 4)
        # Assert
        assert result == 16

    @pytest.mark.positive
    def test_negative_base_odd_exponent(self):
        # Act
        result = AdvancedCalculator.exponentiation(-3, 3)
        # Assert
        assert result == -27

    @pytest.mark.positive
    def test_fractional_base_positive_exponent(self):
        # Act
        result = AdvancedCalculator.exponentiation(0.5, 2)
        # Assert
        assert result == 0.25

    @pytest.mark.positive
    def test_fractional_base_fractional_exponent(self):
        # Act
        result = AdvancedCalculator.exponentiation(4, 0.5)
        # Assert
        assert result == 2

    @pytest.mark.performance
    @pytest.mark.positive
    def test_large_base_and_exponent(self):
        # Act
        result = AdvancedCalculator.exponentiation(10, 10)
        # Assert
        assert result == 10000000000

    @pytest.mark.positive
    def test_base_zero_positive_exponent(self):
        # Act
        result = AdvancedCalculator.exponentiation(0, 5)
        # Assert
        assert result == 0

    @pytest.mark.negative
    @pytest.mark.invalid
    def test_base_zero_negative_exponent(self):
        # Act & Assert
        with pytest.raises(ZeroDivisionError):
            AdvancedCalculator.exponentiation(0, -1)
