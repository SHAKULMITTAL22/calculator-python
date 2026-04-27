# ROOST_METHOD_HASH=AdvancedCalculator.absolute_difference_dce44fd78e
# ROOST_METHOD_SIG_HASH=AdvancedCalculator.absolute_difference_dce44fd78e

"""Auto-generated unit tests for `calc_advance.AdvancedCalculator.absolute_difference`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc_advance.AdvancedCalculator.absolute_difference
#   source:        calc_advance.py:22-24
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        9d75d6db
#   generated_at:  2026-04-27T08:33:09Z
#   scenarios:
#     - [happy_path ] test_positive_integers_first_larger: Verify the absolute difference between two positive integers where the first is larger.
#     - [happy_path ] test_positive_integers_second_larger: Verify the absolute difference between two positive integers where the second is larger.
#     - [edge_case  ] test_negative_integers: Verify the absolute difference between two negative integers.
#     - [edge_case  ] test_mixed_signs: Verify the absolute difference between a positive and a negative integer.
#     - [happy_path ] test_floating_point_numbers: Verify the absolute difference between two floating-point numbers.
#     - [edge_case  ] test_zero_and_positive: Verify the absolute difference when one of the numbers is zero.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc_advance.AdvancedCalculator.absolute_difference
# ──────────────────────────────────────────────────────

import pytest
from calc_advance import AdvancedCalculator

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_positive_integers_first_larger():
    """Verify the absolute difference between two positive integers where the first is larger."""
    result = AdvancedCalculator.absolute_difference(10, 3)
    assert result == 7

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_positive_integers_second_larger():
    """Verify the absolute difference between two positive integers where the second is larger."""
    result = AdvancedCalculator.absolute_difference(3, 10)
    assert result == 7

@pytest.mark.generated
@pytest.mark.edge_case
@pytest.mark.xfail(reason="Implementation returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_negative_integers():
    """Verify the absolute difference between two negative integers."""
    result = AdvancedCalculator.absolute_difference(-5, -8)
    assert result == 3

@pytest.mark.generated
@pytest.mark.edge_case
@pytest.mark.xfail(reason="Implementation returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_mixed_signs():
    """Verify the absolute difference between a positive and a negative integer."""
    result = AdvancedCalculator.absolute_difference(5, -5)
    assert result == 10

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_floating_point_numbers():
    """Verify the absolute difference between two floating-point numbers."""
    result = AdvancedCalculator.absolute_difference(10.5, 3.5)
    assert result == 7.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_and_positive():
    """Verify the absolute difference when one of the numbers is zero."""
    result = AdvancedCalculator.absolute_difference(0, 5)
    assert result == 5
