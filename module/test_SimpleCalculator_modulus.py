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
#   run_id:        37c4aef7
#   generated_at:  2026-04-25T13:48:30Z
#   scenarios:
#     - [happy_path ] test_modulus_positive_integers: Verify that the modulus of two positive integers is correctly calculated.
#     - [error_path ] test_modulus_by_zero: Verify that the function returns a specific error message when attempting to perform modulus by zero.
#     - [happy_path ] test_modulus_negative_dividend: Verify that the modulus with a negative dividend follows Python's floor division behavior (-10 % 3 = 2).
#     - [happy_path ] test_modulus_negative_divisor: Verify that the modulus with a negative divisor follows Python's floor division behavior (10 % -3 = -2).
#     - [edge_case  ] test_modulus_zero_dividend: Verify that the modulus of zero by any non-zero number is 0.
#     - [happy_path ] test_modulus_floating_point_numbers: Verify that the function correctly handles floating-point numbers.
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
    """Verify that the modulus of two positive integers is correctly calculated."""
    assert SimpleCalculator.modulus(10, 3) == 1

@pytest.mark.generated
@pytest.mark.error_path
def test_modulus_by_zero():
    """Verify that the function returns a specific error message when attempting to perform modulus by zero."""
    assert SimpleCalculator.modulus(10, 0) == "Cannot perform modulus by zero"

@pytest.mark.generated
@pytest.mark.happy_path
def test_modulus_negative_dividend():
    """Verify that the modulus with a negative dividend follows Python's floor division behavior (-10 % 3 = 2)."""
    assert SimpleCalculator.modulus(-10, 3) == 2

@pytest.mark.generated
@pytest.mark.happy_path
def test_modulus_negative_divisor():
    """Verify that the modulus with a negative divisor follows Python's floor division behavior (10 % -3 = -2)."""
    assert SimpleCalculator.modulus(10, -3) == -2

@pytest.mark.generated
@pytest.mark.edge_case
def test_modulus_zero_dividend():
    """Verify that the modulus of zero by any non-zero number is 0."""
    assert SimpleCalculator.modulus(0, 5) == 0

@pytest.mark.generated
@pytest.mark.happy_path
def test_modulus_floating_point_numbers():
    """Verify that the function correctly handles floating-point numbers."""
    assert SimpleCalculator.modulus(5.5, 2.0) == 1.5
