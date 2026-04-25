# ROOST_METHOD_HASH=AdvancedCalculator.exponentiation_e4ad67523b
# ROOST_METHOD_SIG_HASH=AdvancedCalculator.exponentiation_e4ad67523b

"""Auto-generated unit tests for `calc_advance.AdvancedCalculator.exponentiation`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc_advance.AdvancedCalculator.exponentiation
#   source:        calc_advance.py:10-12
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        37c4aef7
#   generated_at:  2026-04-25T13:50:05Z
#   scenarios:
#     - [happy_path ] test_exponentiation_positive_integers: Verify that raising a positive integer to a positive integer power returns the correct result.
#     - [edge_case  ] test_exponentiation_zero_exponent: Verify that any non-zero number raised to the power of 0 returns 1.
#     - [edge_case  ] test_exponentiation_negative_exponent: Verify that raising a number to a negative power returns the correct reciprocal power.
#     - [edge_case  ] test_exponentiation_fractional_exponent: Verify that raising a number to a fractional power (e.g., 0.5 for square root) returns the correct result.
#     - [edge_case  ] test_exponentiation_negative_base_even_exponent: Verify that raising a negative base to an even power returns a positive result.
#     - [error_path ] test_exponentiation_zero_base_negative_exponent: Verify that raising zero to a negative power raises a ZeroDivisionError.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc_advance.AdvancedCalculator.exponentiation
# ──────────────────────────────────────────────────────

import pytest
from calc_advance import AdvancedCalculator

@pytest.mark.generated
@pytest.mark.happy_path
def test_exponentiation_positive_integers():
    """Verify that raising a positive integer to a positive integer power returns the correct result."""
    # arrange: None
    # act
    result = AdvancedCalculator.exponentiation(2, 3)
    # assert
    assert result == 8

@pytest.mark.generated
@pytest.mark.edge_case
def test_exponentiation_zero_exponent():
    """Verify that any non-zero number raised to the power of 0 returns 1."""
    # arrange: None
    # act
    result = AdvancedCalculator.exponentiation(5, 0)
    # assert
    assert result == 1

@pytest.mark.generated
@pytest.mark.edge_case
def test_exponentiation_negative_exponent():
    """Verify that raising a number to a negative power returns the correct reciprocal power."""
    # arrange: None
    # act
    result = AdvancedCalculator.exponentiation(2, -2)
    # assert
    assert result == 0.25

@pytest.mark.generated
@pytest.mark.edge_case
def test_exponentiation_fractional_exponent():
    """Verify that raising a number to a fractional power (e.g., 0.5 for square root) returns the correct result."""
    # arrange: None
    # act
    result = AdvancedCalculator.exponentiation(9, 0.5)
    # assert
    assert result == 3.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_exponentiation_negative_base_even_exponent():
    """Verify that raising a negative base to an even power returns a positive result."""
    # arrange: None
    # act
    result = AdvancedCalculator.exponentiation(-3, 2)
    # assert
    assert result == 9

@pytest.mark.generated
@pytest.mark.error_path
def test_exponentiation_zero_base_negative_exponent():
    """Verify that raising zero to a negative power raises a ZeroDivisionError."""
    # arrange: None
    # act & assert
    with pytest.raises(ZeroDivisionError):
        AdvancedCalculator.exponentiation(0, -1)
