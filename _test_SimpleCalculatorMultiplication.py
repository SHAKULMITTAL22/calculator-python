import pytest
from decimal import Decimal
from calc import SimpleCalculator

class Test_SimpleCalculatorMultiplication:

    def test_positive_multiplication(self):
        # Arrange and Act
        result = SimpleCalculator.multiplication(3, 4)
        # Assert
        assert result == 12

    def test_negative_multiplication(self):
        # Arrange and Act
        result = SimpleCalculator.multiplication(-3, -4)
        # Assert
        assert result == 12

    def test_mixed_sign_multiplication(self):
        # Arrange and Act
        result = SimpleCalculator.multiplication(3, -4)
        # Assert
        assert result == -12

    def test_zero_multiplication(self):
        # Arrange and Act
        result = SimpleCalculator.multiplication(5, 0)
        # Assert
        assert result == 0

    def test_large_number_multiplication(self):
        # Arrange and Act
        result = SimpleCalculator.multiplication(123456789, 987654321)
        # Assert
        assert result == 121932631112635269

    def test_floating_point_multiplication(self):
        # Arrange and Act
        result = SimpleCalculator.multiplication(1.5, 2.5)
        # Assert
        assert result == 3.75

    def test_very_small_number_multiplication(self):
        # Arrange and Act
        result = SimpleCalculator.multiplication(1e-10, 2e-10)
        # Assert
        assert result == 2e-20

    def test_identical_numbers_multiplication(self):
        # Arrange and Act
        result = SimpleCalculator.multiplication(7, 7)
        # Assert
        assert result == 49

    def test_decimal_multiplication(self):
        # Arrange and Act
        result = SimpleCalculator.multiplication(Decimal('1.23'), Decimal('4.56'))
        # Assert
        assert result == Decimal('5.6088')

    def test_complex_number_multiplication(self):
        # Arrange and Act
        result = SimpleCalculator.multiplication(complex(1, 2), complex(3, 4))
        # Assert
        assert result == (-5+10j)
