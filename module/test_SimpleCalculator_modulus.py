# ROOST_METHOD_HASH=SimpleCalculator.modulus_a78485441a
# ROOST_METHOD_SIG_HASH=SimpleCalculator.modulus_a78485441a

"""Auto-generated unit tests for `calc.SimpleCalculator.modulus`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc.SimpleCalculator.modulus
#   source:        calc.py:23-27
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        7b5781f7
#   generated_at:  2026-04-27T05:32:15Z
#   scenarios:
#     - [happy_path ] positive_integers: Verify modulus with two positive integers.
#     - [error_path ] modulus_by_zero: Verify that modulus by zero returns the expected error message.
#     - [edge_case  ] negative_dividend: Verify modulus with a negative dividend. In Python, the result takes the sign of the divisor.
#     - [edge_case  ] negative_divisor: Verify modulus with a negative divisor. In Python, the result takes the sign of the divisor.
#     - [edge_case  ] zero_dividend: Verify modulus when the dividend is zero.
#     - [happy_path ] floating_point_numbers: Verify modulus with floating point numbers.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc.SimpleCalculator.modulus
# ──────────────────────────────────────────────────────

import pytest
from calc import SimpleCalculator

@pytest.mark.generated
@pytest.mark.happy_path
def test_positive_integers():
    """Verify modulus with two positive integers."""
    result = SimpleCalculator.modulus(10, 3)
    assert result == 1

@pytest.mark.generated
@pytest.mark.error_path
def test_modulus_by_zero():
    """Verify that modulus by zero returns the expected error message."""
    result = SimpleCalculator.modulus(10, 0)
    assert result == "Cannot perform modulus by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_dividend():
    """Verify modulus with a negative dividend. In Python, the result takes the sign of the divisor."""
    result = SimpleCalculator.modulus(-10, 3)
    assert result == 2

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_divisor():
    """Verify modulus with a negative divisor. In Python, the result takes the sign of the divisor."""
    result = SimpleCalculator.modulus(10, -3)
    assert result == -2

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_dividend():
    """Verify modulus when the dividend is zero."""
    result = SimpleCalculator.modulus(0, 7)
    assert result == 0

@pytest.mark.generated
@pytest.mark.happy_path
def test_floating_point_numbers():
    """Verify modulus with floating point numbers."""
    result = SimpleCalculator.modulus(7.5, 2.5)
    assert result == 0.0
