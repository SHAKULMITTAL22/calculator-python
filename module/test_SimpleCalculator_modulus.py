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
#   run_id:        4010c287
#   generated_at:  2026-04-27T05:24:16Z
#   scenarios:
#     - [happy_path ] positive_integers: Verify that the modulus of two positive integers is correctly calculated.
#     - [error_path ] modulus_by_zero: Verify that the function returns a specific error message when the divisor is zero.
#     - [edge_case  ] negative_dividend: Verify the modulus behavior with a negative dividend, following Python's floor division rules.
#     - [edge_case  ] negative_divisor: Verify the modulus behavior with a negative divisor, following Python's floor division rules.
#     - [edge_case  ] floating_point_numbers: Verify that the function correctly handles floating point numbers.
#     - [edge_case  ] zero_dividend: Verify that the modulus is 0 when the dividend is zero.
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
    """Verify that the modulus of two positive integers is correctly calculated."""
    assert SimpleCalculator.modulus(20, 6) == 2

@pytest.mark.generated
@pytest.mark.error_path
def test_modulus_by_zero():
    """Verify that the function returns a specific error message when the divisor is zero."""
    assert SimpleCalculator.modulus(15, 0) == "Cannot perform modulus by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_dividend():
    """Verify the modulus behavior with a negative dividend, following Python's floor division rules."""
    assert SimpleCalculator.modulus(-20, 6) == 4

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_divisor():
    """Verify the modulus behavior with a negative divisor, following Python's floor division rules."""
    assert SimpleCalculator.modulus(20, -6) == -4

@pytest.mark.generated
@pytest.mark.edge_case
def test_floating_point_numbers():
    """Verify that the function correctly handles floating point numbers."""
    assert SimpleCalculator.modulus(10.5, 3) == 1.5

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_dividend():
    """Verify that the modulus is 0 when the dividend is zero."""
    assert SimpleCalculator.modulus(0, 10) == 0
