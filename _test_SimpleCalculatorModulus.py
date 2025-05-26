import pytest
from calc import SimpleCalculator

class Test_SimpleCalculatorModulus:

    @pytest.mark.valid
    @pytest.mark.positive
    def test_modulus_with_positive_integers(self):
        result = SimpleCalculator.modulus(10, 3)
        assert result == 1

    @pytest.mark.valid
    @pytest.mark.negative
    def test_modulus_with_negative_integers(self):
        result = SimpleCalculator.modulus(-10, 3)
        assert result == 2

    @pytest.mark.invalid
    @pytest.mark.negative
    def test_modulus_with_zero_divisor(self):
        result = SimpleCalculator.modulus(10, 0)
        assert result == "Cannot perform modulus by zero"

    @pytest.mark.valid
    @pytest.mark.positive
    def test_modulus_with_large_numbers(self):
        result = SimpleCalculator.modulus(12345678901234567890, 9876543210)
        assert result == 9876543200

    @pytest.mark.valid
    @pytest.mark.negative
    def test_modulus_with_negative_divisor(self):
        result = SimpleCalculator.modulus(10, -3)
        assert result == -2

    @pytest.mark.valid
    @pytest.mark.fractional
    def test_modulus_with_fractional_numbers(self):
        result = SimpleCalculator.modulus(10.5, 3.5)
        assert result == 3.0

    @pytest.mark.valid
    @pytest.mark.mixed_sign
    def test_modulus_with_mixed_sign_numbers(self):
        result = SimpleCalculator.modulus(-10.5, 3.5)
        assert result == -3.0

    @pytest.mark.valid
    @pytest.mark.zero_dividend
    def test_modulus_zero_dividend(self):
        result = SimpleCalculator.modulus(0, 5)
        assert result == 0

    @pytest.mark.valid
    @pytest.mark.identical_numbers
    def test_modulus_identical_numbers(self):
        result = SimpleCalculator.modulus(5, 5)
        assert result == 0
