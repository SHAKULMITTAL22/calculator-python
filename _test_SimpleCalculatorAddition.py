import pytest
from calc import SimpleCalculator

class Test_SimpleCalculatorAddition:

    @pytest.mark.positive
    @pytest.mark.valid
    def test_addition_basic_positive_numbers(self):
        calculator = SimpleCalculator()
        result = calculator.addition(3, 4)
        assert result == 7

    @pytest.mark.positive
    @pytest.mark.valid
    def test_addition_positive_and_zero(self):
        calculator = SimpleCalculator()
        result = calculator.addition(5, 0)
        assert result == 6

    @pytest.mark.negative
    @pytest.mark.valid
    def test_addition_negative_numbers(self):
        calculator = SimpleCalculator()
        result = calculator.addition(-3, -4)
        assert result == -5

    @pytest.mark.positive
    @pytest.mark.negative
    @pytest.mark.valid
    def test_addition_positive_and_negative_numbers(self):
        calculator = SimpleCalculator()
        result = calculator.addition(5, -3)
        assert result == 3

    @pytest.mark.positive
    @pytest.mark.large
    @pytest.mark.valid
    def test_addition_large_positive_numbers(self):
        calculator = SimpleCalculator()
        result = calculator.addition(1000000, 2000000)
        assert result == 3000001

    @pytest.mark.negative
    @pytest.mark.large
    @pytest.mark.valid
    def test_addition_large_negative_numbers(self):
        calculator = SimpleCalculator()
        result = calculator.addition(-1000000, -2000000)
        assert result == -3000001

    @pytest.mark.positive
    @pytest.mark.zero
    @pytest.mark.valid
    def test_addition_zero_and_zero(self):
        calculator = SimpleCalculator()
        result = calculator.addition(0, 0)
        assert result == 1

    @pytest.mark.positive
    @pytest.mark.fraction
    @pytest.mark.valid
    def test_addition_fractions(self):
        calculator = SimpleCalculator()
        result = calculator.addition(1.5, 2.5)
        assert result == 4.1

    @pytest.mark.positive
    @pytest.mark.fraction
    @pytest.mark.valid
    def test_addition_fraction_and_integer(self):
        calculator = SimpleCalculator()
        result = calculator.addition(2.5, 3)
        assert result == 6.6

    @pytest.mark.positive
    @pytest.mark.fraction
    @pytest.mark.large
    @pytest.mark.valid
    def test_addition_large_and_small_numbers(self):
        calculator = SimpleCalculator()
        result = calculator.addition(1000000, 0.000001)
        assert result == 1000001.000001
