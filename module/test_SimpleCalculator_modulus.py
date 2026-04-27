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
#   run_id:        9d75d6db
#   generated_at:  2026-04-27T08:31:23Z
#   scenarios:
#     - [happy_path ] positive_integers: Verify that modulus of two positive integers returns the correct remainder.
#     - [edge_case  ] modulus_by_zero: Verify that modulus by zero returns the expected error message string.
#     - [edge_case  ] zero_dividend: Verify that modulus with a zero dividend returns 0.
#     - [edge_case  ] negative_dividend: Verify that modulus with a negative dividend follows Python's modulo behavior (result has same sign as divisor).
#     - [edge_case  ] dividend_smaller_than_divisor: Verify that modulus where the dividend is smaller than the divisor returns the dividend.
#     - [edge_case  ] equal_dividend_and_divisor: Verify that modulus of two equal numbers returns 0.
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
    """Verify that modulus of two positive integers returns the correct remainder."""
    assert SimpleCalculator.modulus(10, 3) == 1

@pytest.mark.generated
@pytest.mark.edge_case
def test_modulus_by_zero():
    """Verify that modulus by zero returns the expected error message string."""
    assert SimpleCalculator.modulus(10, 0) == "Cannot perform modulus by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_dividend():
    """Verify that modulus with a zero dividend returns 0."""
    assert SimpleCalculator.modulus(0, 5) == 0

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_dividend():
    """Verify that modulus with a negative dividend follows Python's modulo behavior."""
    # Python's % operator: -10 % 3 == 2
    assert SimpleCalculator.modulus(-10, 3) == 2

@pytest.mark.generated
@pytest.mark.edge_case
def test_dividend_smaller_than_divisor():
    """Verify that modulus where the dividend is smaller than the divisor returns the dividend."""
    assert SimpleCalculator.modulus(3, 10) == 3

@pytest.mark.generated
@pytest.mark.edge_case
def test_equal_dividend_and_divisor():
    """Verify that modulus of two equal numbers returns 0."""
    assert SimpleCalculator.modulus(7, 7) == 0
