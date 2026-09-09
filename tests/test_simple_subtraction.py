import pytest

from calc import SimpleCalculator


@pytest.mark.parametrize("operand", [7, 0, -7, 2.5])
def test_subtracting_identical_numbers_returns_zero(operand):
    assert SimpleCalculator.subtraction(operand, operand) == 0
