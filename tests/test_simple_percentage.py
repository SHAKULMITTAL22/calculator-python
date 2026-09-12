import pytest

from calc import SimpleCalculator


@pytest.mark.parametrize(
    ("value", "percent", "expected"),
    [(200, 15, 30), (0, 25, 0), (80, 12.5, 10), (-50, 10, -5)],
)
def test_percentage(value, percent, expected):
    assert SimpleCalculator.percentage(value, percent) == expected
