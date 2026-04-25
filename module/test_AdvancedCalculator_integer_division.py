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
#   run_id:        6ffe75a1
#   generated_at:  2026-04-25T12:13:24Z
#   scenarios:
#     - [happy_path ] happy_path_exact: Verify integer division with two positive integers where the result is exact.
#     - [happy_path ] happy_path_with_remainder: Verify integer division with two positive integers where there is a remainder (result should be floored).
#     - [error_path ] error_division_by_zero: Verify that dividing by zero returns the expected error message.
#     - [edge_case  ] edge_case_negative_dividend: Verify integer division with a negative dividend to ensure it follows Python's floor division behavior.
#     - [edge_case  ] edge_case_negative_divisor: Verify integer division with a negative divisor to ensure it follows Python's floor division behavior.
#     - [edge_case  ] edge_case_zero_dividend: Verify integer division where the dividend is zero.
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
def test_happy_path_exact():
    """Verify integer division with two positive integers where the result is exact."""
    result = AdvancedCalculator.integer_division(20, 4)
    assert result == 5

@pytest.mark.generated
@pytest.mark.happy_path
def test_happy_path_with_remainder():
    """Verify integer division with two positive integers where there is a remainder (result should be floored)."""
    result = AdvancedCalculator.integer_division(17, 5)
    assert result == 3

@pytest.mark.generated
@pytest.mark.error_path
def test_error_division_by_zero():
    """Verify that dividing by zero returns the expected error message."""
    result = AdvancedCalculator.integer_division(10, 0)
    assert result == "Cannot perform integer division by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_edge_case_negative_dividend():
    """Verify integer division with a negative dividend to ensure it follows Python's floor division behavior."""
    result = AdvancedCalculator.integer_division(-11, 3)
    assert result == -4

@pytest.mark.generated
@pytest.mark.edge_case
def test_edge_case_negative_divisor():
    """Verify integer division with a negative divisor to ensure it follows Python's floor division behavior."""
    result = AdvancedCalculator.integer_division(10, -3)
    assert result == -4

@pytest.mark.generated
@pytest.mark.edge_case
def test_edge_case_zero_dividend():
    """Verify integer division where the dividend is zero."""
    result = AdvancedCalculator.integer_division(0, 10)
    assert result == 0
