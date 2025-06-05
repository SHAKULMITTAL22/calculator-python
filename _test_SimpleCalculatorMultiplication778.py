def test_basic_multiplication(self):
    result = SimpleCalculator.multiplication(3, 4)
    assert result == 12

def test_multiplication_with_zero(self):
    result = SimpleCalculator.multiplication(5, 0)
    assert result == 0

def test_multiplication_with_negative_numbers(self):
    result = SimpleCalculator.multiplication(-3, -4)
    assert result == 12

def test_multiplication_with_one(self):
    result = SimpleCalculator.multiplication(7, 1)
    assert result == 7

def test_multiplication_with_large_numbers(self):
    result = SimpleCalculator.multiplication(1000000, 2000000)
    assert result == 2000000000000

def test_multiplication_with_floating_point_numbers(self):
    result = SimpleCalculator.multiplication(2.5, 4.0)
    assert result == 10.0

def test_multiplication_with_mixed_numbers(self):
    result = SimpleCalculator.multiplication(5, 2.5)
    assert result == 12.5

def test_multiplication_with_special_characters(self):
    with pytest.raises(TypeError):
        SimpleCalculator.multiplication('#', 3)

def test_multiplication_with_strings(self):
    with pytest.raises(TypeError):
        SimpleCalculator.multiplication('a', 3)

def test_multiplication_with_boolean_values(self):
    result = SimpleCalculator.multiplication(True, False)
    assert result == 0

def test_multiplication_with_lists(self):
    with pytest.raises(TypeError):
        SimpleCalculator.multiplication([1, 2], 3)

def test_multiplication_with_tuples(self):
    with pytest.raises(TypeError):
        SimpleCalculator.multiplication((1, 2), 3)

def test_multiplication_with_none(self):
    with pytest.raises(TypeError):
        SimpleCalculator.multiplication(None, 3)

def test_multiplication_with_dicts(self):
    with pytest.raises(TypeError):
        SimpleCalculator.multiplication({'a': 1}, 3)
