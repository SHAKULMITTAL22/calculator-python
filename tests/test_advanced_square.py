import pytest

from calc_advance import AdvancedCalculator


@pytest.mark.parametrize(
    ("number", "expected"),
    [(0, 0), (1, 1), (4, 16), (-3, 9), (1.5, 2.25)],
)
def test_square(number, expected):
    assert AdvancedCalculator.square(number) == expected
