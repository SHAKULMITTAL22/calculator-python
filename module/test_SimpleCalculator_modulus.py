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
#   run_id:        cf16e38c
#   generated_at:  2026-04-25T14:39:09Z
#   scenarios:
#     - [happy_path ] positive_integers: Verify that the modulus of two positive integers is correctly calculated.
#     - [error_path ] modulus_by_zero: Verify that the method returns a specific error message when attempting to perform modulus by zero.
#     - [happy_path ] negative_dividend: Verify the modulus behavior when the dividend is a negative number.
#     - [happy_path ] negative_divisor: Verify the modulus behavior when the divisor is a negative number.
#     - [edge_case  ] zero_dividend: Verify that the modulus is 0 when the dividend is 0.
#     - [happy_path ] floating_point_numbers: Verify that the method correctly handles floating point numbers.
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
    assert SimpleCalculator.modulus(10, 3) == 1

@pytest.mark.generated
@pytest.mark.error_path
def test_modulus_by_zero():
    """Verify that the method returns a specific error message when attempting to perform modulus by zero."""
    assert SimpleCalculator.modulus(10, 0) == "Cannot perform modulus by zero"

@pytest.mark.generated
@pytest.mark.happy_path
def test_negative_dividend():
    """Verify the modulus behavior when the dividend is a negative number."""
    assert SimpleCalculator.modulus(-10, 3) == 2

@pytest.mark.generated
@pytest.mark.happy_path
def test_negative_divisor():
    """Verify the modulus behavior when the divisor is a negative number."""
    assert SimpleCalculator.modulus(10, -3) == -2

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_dividend():
    """Verify that the modulus is 0 when the dividend is 0."""
    assert SimpleCalculator.modulus(0, 5) == 0

@pytest.mark.generated
@pytest.mark.happy_path
def test_floating_point_numbers():
    """Verify that the method correctly handles floating point numbers."""
    assert SimpleCalculator.modulus(7.5, 2.5) == 0.0
