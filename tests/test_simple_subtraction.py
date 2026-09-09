from calc import SimpleCalculator


def test_subtracting_identical_numbers_returns_zero():
    assert SimpleCalculator.subtraction(7, 7) == 0
