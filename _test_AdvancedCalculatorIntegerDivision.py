import pytest
from calc_advance import AdvancedCalculator

class Test_AdvancedCalculatorIntegerDivision:

    @pytest.mark.valid
    def test_division_with_positive_integers(self):
        result = AdvancedCalculator.integer_division(10, 2)
        assert result == 5

    @pytest.mark.valid
    def test_division_with_negative_integers(self):
        result = AdvancedCalculator.integer_division(-10, -2)
        assert result == 5

    @pytest.mark.valid
    def test_division_with_one_negative_integer(self):
        result = AdvancedCalculator.integer_division(-10, 2)
        assert result == -5

    @pytest.mark.invalid
    def test_division_by_zero(self):
        result = AdvancedCalculator.integer_division(10, 0)
        assert result == "Cannot perform integer division by zero"

    @pytest.mark.valid
    def test_division_with_zero_numerator(self):
        result = AdvancedCalculator.integer_division(0, 10)
        assert result == 0

    @pytest.mark.valid
    def test_division_with_large_integers(self):
        result = AdvancedCalculator.integer_division(1000000, 2)
        assert result == 500000

    @pytest.mark.valid
    def test_division_with_fractional_result(self):
        result = AdvancedCalculator.integer_division(5, 2)
        assert result == 2

    @pytest.mark.valid
    def test_division_with_identical_numbers(self):
        result = AdvancedCalculator.integer_division(7, 7)
        assert result == 1
