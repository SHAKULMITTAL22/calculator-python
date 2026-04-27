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
#   run_id:        30a9e555
#   generated_at:  2026-04-27T05:18:11Z
#   scenarios:
#     - [happy_path ] positive_integers: Verify that modulus returns the correct remainder for two positive integers.
#     - [error_path ] modulus_by_zero: Verify that the method handles division by zero by returning a specific error message.
#     - [edge_case  ] negative_dividend: Verify the behavior of modulus with a negative dividend.
#     - [edge_case  ] dividend_zero: Verify that modulus returns 0 when the dividend is zero.
#     - [edge_case  ] dividend_smaller_than_divisor: Verify that modulus returns the dividend when it is smaller than the divisor.
#     - [happy_path ] float_inputs: Verify that the method correctly handles floating point numbers.
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
    """Verify that modulus returns the correct remainder for two positive integers."""
    assert SimpleCalculator.modulus(10, 3) == 1

@pytest.mark.generated
@pytest.mark.error_path
def test_modulus_by_zero():
    """Verify that the method handles division by zero by returning a specific error message."""
    assert SimpleCalculator.modulus(10, 0) == "Cannot perform modulus by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_dividend():
    """Verify the behavior of modulus with a negative dividend."""
    assert SimpleCalculator.modulus(-10, 3) == 2

@pytest.mark.generated
@pytest.mark.edge_case
def test_dividend_zero():
    """Verify that modulus returns 0 when the dividend is zero."""
    assert SimpleCalculator.modulus(0, 5) == 0

@pytest.mark.generated
@pytest.mark.edge_case
def test_dividend_smaller_than_divisor():
    """Verify that modulus returns the dividend when it is smaller than the divisor."""
    assert SimpleCalculator.modulus(3, 10) == 3

@pytest.mark.generated
@pytest.mark.happy_path
def test_float_inputs():
    """Verify that the method correctly handles floating point numbers."""
    assert SimpleCalculator.modulus(10.5, 3) == 1.5
