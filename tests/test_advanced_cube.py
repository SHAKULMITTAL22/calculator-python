import pytest

from calc_advance import AdvancedCalculator


@pytest.mark.parametrize(
    ("number", "expected"),
    [(0, 0), (1, 1), (4, 64), (-3, -27), (1.5, 3.375)],
)
def test_cube(number, expected):
    assert AdvancedCalculator.cube(number) == expected
