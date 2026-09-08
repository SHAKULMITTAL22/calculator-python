from calc import percentage


def test_percentage_example():
    assert percentage(200, 15) == 30


def test_percentage_with_fractional_values():
    assert percentage(12.5, 20) == 2.5


def test_percentage_with_zero_percent():
    assert percentage(200, 0) == 0


def test_percentage_with_negative_value():
    assert percentage(-200, 15) == -30
