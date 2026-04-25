ROOST_METHOD_HASH=AdvancedCalculator.integer_division_6e0bd798e7
ROOST_METHOD_SIG_HASH=AdvancedCalculator.integer_division_6e0bd798e7

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
#   run_id:        a9ed4208
#   generated_at:  2026-04-25T13:32:24Z
#   scenarios:
#     - [happy_path ] positive_integers: Verify integer division with two positive integers where the first is larger.
#     - [happy_path ] negative_dividend: Verify integer division with a negative dividend to ensure floor division behavior.
#     - [error_path ] division_by_zero_integer: Verify that division by zero returns the expected error message instead of raising an exception.
#     - [error_path ] division_by_zero_float: Verify that division by float zero also returns the expected error message.
#     - [edge_case  ] zero_dividend: Verify that zero divided by any non-zero number is 0.
#     - [happy_path ] float_inputs: Verify that the method handles float inputs correctly using floor division.
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
def test_positive_integers():
    """Verify integer division with two positive integers where the first is larger."""
    result = AdvancedCalculator.integer_division(10, 3)
    assert result == 3

@pytest.mark.generated
@pytest.mark.happy_path
def test_negative_dividend():
    """Verify integer division with a negative dividend to ensure floor division behavior."""
    result = AdvancedCalculator.integer_division(-10, 3)
    assert result == -4

@pytest.mark.generated
@pytest.mark.error_path
def test_division_by_zero_integer():
    """Verify that division by zero returns the expected error message instead of raising an exception."""
    result = AdvancedCalculator.integer_division(10, 0)
    assert result == "Cannot perform integer division by zero"

@pytest.mark.generated
@pytest.mark.error_path
def test_division_by_zero_float():
    """Verify that division by float zero also returns the expected error message."""
    result = AdvancedCalculator.integer_division(10, 0.0)
    assert result == "Cannot perform integer division by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_dividend():
    """Verify that zero divided by any non-zero number is 0."""
    result = AdvancedCalculator.integer_division(0, 5)
    assert result == 0

@pytest.mark.generated
@pytest.mark.happy_path
def test_float_inputs():
    """Verify that the method handles float inputs correctly using floor division."""
    result = AdvancedCalculator.integer_division(10.5, 2.0)
    assert result == 5.0
