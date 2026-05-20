import pytest
from calc_advance import AdvancedCalculator

class Test_AdvancedCalculatorAbsoluteDifference:

    @pytest.mark.positive
    def test_absolute_difference_pos_neg(self):
        result = AdvancedCalculator.absolute_difference(5, -3)
        assert result == 8

    @pytest.mark.positive
    def test_absolute_difference_both_pos(self):
        result = AdvancedCalculator.absolute_difference(10, 4)
        assert result == 6

    @pytest.mark.positive
    def test_absolute_difference_both_neg(self):
        result = AdvancedCalculator.absolute_difference(-10, -7)
        assert result == 3

    @pytest.mark.positive
    def test_absolute_difference_same_numbers(self):
        result = AdvancedCalculator.absolute_difference(8, 8)
        assert result == 0

    @pytest.mark.performance
    def test_absolute_difference_large_numbers(self):
        result = AdvancedCalculator.absolute_difference(1000000, 1)
        assert result == 999999

    @pytest.mark.positive
    def test_absolute_difference_floating_point(self):
        result = AdvancedCalculator.absolute_difference(3.5, 1.2)
        assert result == 2.3

    @pytest.mark.valid
    def test_absolute_difference_one_zero(self):
        result = AdvancedCalculator.absolute_difference(0, 5)
        assert result == 5

    @pytest.mark.negative
    def test_absolute_difference_negative_zero(self):
        result = AdvancedCalculator.absolute_difference(-5, 0)
        assert result == 5

    @pytest.mark.valid
    def test_absolute_difference_large_neg_small_pos(self):
        result = AdvancedCalculator.absolute_difference(-1000, 50)
        assert result == 1050

    @pytest.mark.valid
    def test_absolute_difference_large_pos_small_neg(self):
        result = AdvancedCalculator.absolute_difference(1000, -50)
        assert result == 1050
