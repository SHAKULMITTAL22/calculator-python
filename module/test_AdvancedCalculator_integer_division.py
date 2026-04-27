# ROOST_METHOD_HASH=AdvancedCalculator.integer_division_6e0bd798e7
# ROOST_METHOD_SIG_HASH=AdvancedCalculator.integer_division_6e0bd798e7

"""Auto-generated unit tests for `calc_advance.AdvancedCalculator.integer_division`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc_advance.AdvancedCalculator.integer_division
#   source:        calc_advance.py:15-19
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        cb0b96ef
#   generated_at:  2026-04-27T09:12:35Z
#   scenarios:
#     - [happy_path ] positive_integers_with_remainder: Verify integer division with two positive integers where there is a remainder.
#     - [happy_path ] negative_dividend_floor_behavior: Verify integer division with a negative dividend to ensure floor division behavior.
#     - [error_path ] division_by_zero_returns_string: Verify that division by zero returns the specific error message string instead of raising an exception.
#     - [edge_case  ] division_by_float_zero: Verify that division by float zero also returns the error message string.
#     - [edge_case  ] dividend_smaller_than_divisor: Verify integer division where the dividend is smaller than the divisor.
#     - [happy_path ] float_inputs_integer_division: Verify integer division with float inputs.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc_advance.AdvancedCalculator.integer_division
# ──────────────────────────────────────────────────────

import pytest
from calc_advance import AdvancedCalculator

@pytest.mark.generated
@pytest.mark.happy_path
def test_positive_integers_with_remainder():
    """Verify integer division with two positive integers where there is a remainder."""
    result = AdvancedCalculator.integer_division(10, 3)
    assert result == 3

@pytest.mark.generated
@pytest.mark.happy_path
def test_negative_dividend_floor_behavior():
    """Verify integer division with a negative dividend to ensure floor division behavior."""
    result = AdvancedCalculator.integer_division(-10, 3)
    assert result == -4

@pytest.mark.generated
@pytest.mark.error_path
def test_division_by_zero_returns_string():
    """Verify that division by zero returns the specific error message string instead of raising an exception."""
    result = AdvancedCalculator.integer_division(10, 0)
    assert result == "Cannot perform integer division by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_division_by_float_zero():
    """Verify that division by float zero also returns the error message string."""
    result = AdvancedCalculator.integer_division(10, 0.0)
    assert result == "Cannot perform integer division by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_dividend_smaller_than_divisor():
    """Verify integer division where the dividend is smaller than the divisor."""
    result = AdvancedCalculator.integer_division(1, 2)
    assert result == 0

@pytest.mark.generated
@pytest.mark.happy_path
def test_float_inputs_integer_division():
    """Verify integer division with float inputs."""
    result = AdvancedCalculator.integer_division(7.5, 2.5)
    assert result == 3.0
