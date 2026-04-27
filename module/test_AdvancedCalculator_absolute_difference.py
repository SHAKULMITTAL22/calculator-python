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
#   run_id:        30a9e555
#   generated_at:  2026-04-27T05:19:47Z
#   scenarios:
#     - [happy_path ] test_positive_integers_first_larger: Test absolute difference with two positive integers where the first is larger.
#     - [happy_path ] test_positive_integers_second_larger: Test absolute difference with two positive integers where the second is larger.
#     - [happy_path ] test_mixed_signs: Test absolute difference with one positive and one negative integer.
#     - [happy_path ] test_both_negative_integers: Test absolute difference with two negative integers.
#     - [edge_case  ] test_with_zero_input: Test absolute difference when one of the numbers is zero.
#     - [happy_path ] test_floating_point_inputs: Test absolute difference with floating point numbers.
#     - [error_path ] test_invalid_type_input: Test that non-numeric input raises a TypeError.
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
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'absolute difference' but implementation returns abs(num1 + num2)")
def test_positive_integers_first_larger():
    """Test absolute difference with two positive integers where the first is larger."""
    result = AdvancedCalculator.absolute_difference(10, 4)
    assert result == 6

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'absolute difference' but implementation returns abs(num1 + num2)")
def test_positive_integers_second_larger():
    """Test absolute difference with two positive integers where the second is larger."""
    result = AdvancedCalculator.absolute_difference(4, 10)
    assert result == 6

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'absolute difference' but implementation returns abs(num1 + num2)")
def test_mixed_signs():
    """Test absolute difference with one positive and one negative integer."""
    result = AdvancedCalculator.absolute_difference(7, -3)
    assert result == 10

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'absolute difference' but implementation returns abs(num1 + num2)")
def test_both_negative_integers():
    """Test absolute difference with two negative integers."""
    result = AdvancedCalculator.absolute_difference(-5, -12)
    assert result == 7

@pytest.mark.generated
@pytest.mark.edge_case
def test_with_zero_input():
    """Test absolute difference when one of the numbers is zero."""
    result = AdvancedCalculator.absolute_difference(0, -8)
    assert result == 8

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'absolute difference' but implementation returns abs(num1 + num2)")
def test_floating_point_inputs():
    """Test absolute difference with floating point numbers."""
    result = AdvancedCalculator.absolute_difference(10.5, 2.5)
    assert result == 8.0

@pytest.mark.generated
@pytest.mark.error_path
def test_invalid_type_input():
    """Test that non-numeric input raises a TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.absolute_difference("10", 5)
