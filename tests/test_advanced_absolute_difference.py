import pytest

from calc_advance import AdvancedCalculator


@pytest.mark.parametrize(
    ("num1", "num2", "expected"),
    [(10, 4, 6), (4, 10, 6), (-3, -8, 5), (2.5, 1.0, 1.5), (7, 7, 0)],
)
def test_absolute_difference(num1, num2, expected):
    assert AdvancedCalculator.absolute_difference(num1, num2) == expected
