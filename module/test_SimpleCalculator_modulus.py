ROOST_METHOD_HASH=SimpleCalculator.modulus_a78485441a
ROOST_METHOD_SIG_HASH=SimpleCalculator.modulus_a78485441a

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
#   run_id:        6ffe75a1
#   generated_at:  2026-04-25T12:11:59Z
#   scenarios:
#     - [happy_path ] test_modulus_positive_integers: Verify that modulus correctly returns the remainder for two positive integers.
#     - [error_path ] test_modulus_by_zero: Verify that the function returns a specific error message when the divisor is zero.
#     - [edge_case  ] test_modulus_negative_dividend: Verify that modulus handles a negative dividend correctly.
#     - [edge_case  ] test_modulus_negative_divisor: Verify that modulus handles a negative divisor correctly.
#     - [edge_case  ] test_modulus_floating_point: Verify that modulus correctly handles floating point numbers.
#     - [happy_path ] test_modulus_zero_dividend: Verify that modulus returns 0 when the dividend is zero.
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
    """Verify that modulus correctly returns the remainder for two positive integers."""
    result = SimpleCalculator.modulus(10, 3)
    assert result == 1

@pytest.mark.generated
@pytest.mark.error_path
def test_modulus_by_zero():
    """Verify that the function returns a specific error message when the divisor is zero."""
    result = SimpleCalculator.modulus(10, 0)
    assert result == "Cannot perform modulus by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_modulus_negative_dividend():
    """Verify that modulus handles a negative dividend correctly."""
    result = SimpleCalculator.modulus(-10, 3)
    assert result == 2

@pytest.mark.generated
@pytest.mark.edge_case
def test_modulus_negative_divisor():
    """Verify that modulus handles a negative divisor correctly."""
    result = SimpleCalculator.modulus(10, -3)
    assert result == -2

@pytest.mark.generated
@pytest.mark.edge_case
def test_modulus_floating_point():
    """Verify that modulus correctly handles floating point numbers."""
    result = SimpleCalculator.modulus(10.5, 3.0)
    assert result == 1.5

@pytest.mark.generated
@pytest.mark.happy_path
def test_modulus_zero_dividend():
    """Verify that modulus returns 0 when the dividend is zero."""
    result = SimpleCalculator.modulus(0, 5)
    assert result == 0
