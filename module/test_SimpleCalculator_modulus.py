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
#   run_id:        7dd18b11
#   generated_at:  2026-04-27T08:04:48Z
#   scenarios:
#     - [happy_path ] test_modulus_positive_integers: Verify that modulus works correctly with two positive integers.
#     - [edge_case  ] test_modulus_by_zero: Verify that the method returns the correct error message when the divisor is zero.
#     - [edge_case  ] test_modulus_negative_dividend: Verify modulus behavior with a negative dividend (following Python's % operator behavior).
#     - [edge_case  ] test_modulus_negative_divisor: Verify modulus behavior with a negative divisor (following Python's % operator behavior).
#     - [edge_case  ] test_modulus_zero_dividend: Verify that modulus returns 0 when the dividend is zero.
#     - [happy_path ] test_modulus_floats: Verify that modulus works correctly with floating point numbers.
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
def test_modulus_positive_integers():
    """Verify that modulus works correctly with two positive integers."""
    assert SimpleCalculator.modulus(10, 3) == 1

@pytest.mark.generated
@pytest.mark.edge_case
def test_modulus_by_zero():
    """Verify that the method returns the correct error message when the divisor is zero."""
    assert SimpleCalculator.modulus(10, 0) == "Cannot perform modulus by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_modulus_negative_dividend():
    """Verify modulus behavior with a negative dividend (following Python's % operator behavior)."""
    assert SimpleCalculator.modulus(-10, 3) == 2

@pytest.mark.generated
@pytest.mark.edge_case
def test_modulus_negative_divisor():
    """Verify modulus behavior with a negative divisor (following Python's % operator behavior)."""
    assert SimpleCalculator.modulus(10, -3) == -2

@pytest.mark.generated
@pytest.mark.edge_case
def test_modulus_zero_dividend():
    """Verify that modulus returns 0 when the dividend is zero."""
    assert SimpleCalculator.modulus(0, 5) == 0

@pytest.mark.generated
@pytest.mark.happy_path
def test_modulus_floats():
    """Verify that modulus works correctly with floating point numbers."""
    assert SimpleCalculator.modulus(7.5, 2.5) == 0.0
