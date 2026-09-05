import pytest

from calc_advance import AdvancedCalculator


@pytest.mark.parametrize(
    ("number", "expected"),
    [(0, 0), (1, 1), (4, 64), (-3, -27), (1.5, 3.375)],
)
def test_cube(number, expected):
    assert AdvancedCalculator.cube(number) == expected


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (
            9_223_372_036_854_775_807,
            784_637_716_923_335_095_224_261_902_710_254_454_442_933_591_094_742_482_943,
        ),
        (
            -9_223_372_036_854_775_808,
            -784_637_716_923_335_095_479_473_677_900_958_302_012_794_430_558_004_314_112,
        ),
    ],
    ids=["signed-64-bit-maximum", "signed-64-bit-minimum"],
)
def test_cube_at_signed_64_bit_boundaries(number, expected):
    assert AdvancedCalculator.cube(number) == expected
