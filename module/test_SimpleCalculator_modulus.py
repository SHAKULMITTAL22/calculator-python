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
#   run_id:        cb0b96ef
#   generated_at:  2026-04-27T09:10:43Z
#   scenarios:
#     - [happy_path ] positive_integers: Verify modulus with two positive integers where the dividend is greater than the divisor.
#     - [error_path ] modulus_by_zero: Verify that modulus by zero returns the specific error message instead of raising ZeroDivisionError.
#     - [edge_case  ] dividend_zero: Verify that modulus where the dividend is zero returns zero.
#     - [edge_case  ] negative_dividend: Verify modulus with a negative dividend to ensure it follows Python's standard behavior.
#     - [edge_case  ] negative_divisor: Verify modulus with a negative divisor.
#     - [happy_path ] dividend_smaller_than_divisor: Verify modulus where the dividend is smaller than the divisor.
#     - [happy_path ] float_numbers: Verify modulus with floating point numbers.
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
    """Verify modulus with two positive integers where the dividend is greater than the divisor."""
    assert SimpleCalculator.modulus(10, 3) == 1

@pytest.mark.generated
@pytest.mark.error_path
def test_modulus_by_zero():
    """Verify that modulus by zero returns the specific error message instead of raising ZeroDivisionError."""
    assert SimpleCalculator.modulus(10, 0) == "Cannot perform modulus by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_dividend_zero():
    """Verify that modulus where the dividend is zero returns zero."""
    assert SimpleCalculator.modulus(0, 5) == 0

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_dividend():
    """Verify modulus with a negative dividend to ensure it follows Python's standard behavior."""
    assert SimpleCalculator.modulus(-10, 3) == 2

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_divisor():
    """Verify modulus with a negative divisor."""
    assert SimpleCalculator.modulus(10, -3) == -2

@pytest.mark.generated
@pytest.mark.happy_path
def test_dividend_smaller_than_divisor():
    """Verify modulus where the dividend is smaller than the divisor."""
    assert SimpleCalculator.modulus(3, 10) == 3

@pytest.mark.generated
@pytest.mark.happy_path
def test_float_numbers():
    """Verify modulus with floating point numbers."""
    assert SimpleCalculator.modulus(10.5, 3.0) == 1.5
