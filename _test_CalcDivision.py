import pytest
from calc import division

class Test_CalcDivision:

    @pytest.mark.negative
    def test_division_by_zero(self):
        assert division(10, 0) == "Cannot divide by zero"

    @pytest.mark.positive
    def test_positive_division(self):
        assert division(20, 4) == 5

    @pytest.mark.positive
    def test_negative_division(self):
        assert division(-18, -2) == 9

    @pytest.mark.positive
    def test_mixed_signs_division(self):
        assert division(15, -3) == -5

    @pytest.mark.positive
    def test_division_by_one(self):
        assert division(42, 1) == 42

    @pytest.mark.positive
    def test_large_numbers_division(self):
        assert division(1000000, 100) == 10000

    @pytest.mark.positive
    def test_small_numbers_division(self):
        assert division(0.000001, 0.0000001) == 10

    @pytest.mark.positive
    def test_division_with_decimal_results(self):
        assert division(7, 2) == 3.5

    @pytest.mark.positive
    def test_division_with_large_decimals(self):
        assert division(3.141592653589793, 3.141592653589793) == 1.0

    @pytest.mark.positive
    def test_division_with_negative_decimals(self):
        assert division(-3.141592653589793, 3.141592653589793) == -1.0
