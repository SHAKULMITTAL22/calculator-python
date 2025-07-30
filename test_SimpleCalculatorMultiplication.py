import pytest
from SimpleCalculator import multiplication

class TestSimpleCalculatorMultiplication:

    def test_multiplication_with_none_values(self):
        with pytest.raises(TypeError):
            multiplication(None, 3)

    def test_multiplication_with_list_values(self):
        with pytest.raises(TypeError):
            multiplication([1, 2], 3)

    def test_multiplication_with_tuple_values(self):
        with pytest.raises(TypeError):
            multiplication((1, 2), 3)

    def test_multiplication_with_dict_values(self):
        with pytest.raises(TypeError):
            multiplication({'key': 'value'}, 3)
