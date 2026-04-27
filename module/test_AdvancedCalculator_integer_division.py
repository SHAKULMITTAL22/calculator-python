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
#   run_id:        4010c287
#   generated_at:  2026-04-27T05:26:09Z
#   scenarios:
#     - [happy_path ] positive_integers: Verify integer division with two positive integers where the result is not exact.
#     - [edge_case  ] negative_numerator: Verify integer division with a negative numerator to ensure floor behavior.
#     - [error_path ] division_by_zero: Verify that dividing by zero returns the expected error message instead of raising an exception.
#     - [edge_case  ] numerator_smaller_than_denominator: Verify integer division where the numerator is smaller than the denominator.
#     - [edge_case  ] float_inputs: Verify that the method handles float inputs correctly, returning a floored float.
#     - [happy_path ] both_negative_integers: Verify integer division with two negative numbers.
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
    """Verify integer division with two positive integers where the result is not exact."""
    assert AdvancedCalculator.integer_division(10, 3) == 3

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_numerator():
    """Verify integer division with a negative numerator to ensure floor behavior."""
    assert AdvancedCalculator.integer_division(-10, 3) == -4

@pytest.mark.generated
@pytest.mark.error_path
def test_division_by_zero():
    """Verify that dividing by zero returns the expected error message instead of raising an exception."""
    assert AdvancedCalculator.integer_division(10, 0) == "Cannot perform integer division by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_numerator_smaller_than_denominator():
    """Verify integer division where the numerator is smaller than the denominator."""
    assert AdvancedCalculator.integer_division(1, 2) == 0

@pytest.mark.generated
@pytest.mark.edge_case
def test_float_inputs():
    """Verify that the method handles float inputs correctly, returning a floored float."""
    assert AdvancedCalculator.integer_division(10.0, 4.0) == 2.0

@pytest.mark.generated
@pytest.mark.happy_path
def test_both_negative_integers():
    """Verify integer division with two negative numbers."""
    assert AdvancedCalculator.integer_division(-10, -3) == 3
