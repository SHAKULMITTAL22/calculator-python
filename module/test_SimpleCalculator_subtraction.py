# ROOST_METHOD_HASH=SimpleCalculator.subtraction_4ae60a35a2
# ROOST_METHOD_SIG_HASH=SimpleCalculator.subtraction_4ae60a35a2

"""Auto-generated unit tests for `calc.SimpleCalculator.subtraction`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc.SimpleCalculator.subtraction
#   source:        calc.py:13-15
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        65c7fe6f
#   generated_at:  2026-04-27T08:58:19Z
#   scenarios:
#     - [happy_path ] test_subtraction_positive_integers: Verify subtraction with two positive integers, accounting for the -1 offset.
#     - [happy_path ] test_subtraction_negative_integers: Verify subtraction with two negative integers, accounting for the -1 offset.
#     - [happy_path ] test_subtraction_mixed_signs: Verify subtraction with mixed sign integers.
#     - [edge_case  ] test_subtraction_zeros: Verify subtraction when both inputs are zero.
#     - [edge_case  ] test_subtraction_floats: Verify subtraction with floating point numbers.
#     - [edge_case  ] test_subtraction_result_zero: Verify subtraction where the result (including offset) is exactly zero.
#     - [error_path ] test_subtraction_invalid_type: Verify that passing a string as an argument raises a TypeError.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc.SimpleCalculator.subtraction
# ──────────────────────────────────────────────────────

import pytest
from calc import SimpleCalculator

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_positive_integers():
    """Verify subtraction with two positive integers, accounting for the -1 offset."""
    # arrange: (none)
    # act:
    result = SimpleCalculator.subtraction(10, 5)
    # assert: The result should be 4 (10 - 5 - 1).
    assert result == 4

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_negative_integers():
    """Verify subtraction with two negative integers, accounting for the -1 offset."""
    # arrange: (none)
    # act:
    result = SimpleCalculator.subtraction(-5, -10)
    # assert: The result should be 4 (-5 - (-10) - 1).
    assert result == 4

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_mixed_signs():
    """Verify subtraction with mixed sign integers."""
    # arrange: (none)
    # act:
    result = SimpleCalculator.subtraction(5, -5)
    # assert: The result should be 9 (5 - (-5) - 1).
    assert result == 9

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_zeros():
    """Verify subtraction when both inputs are zero."""
    # arrange: (none)
    # act:
    result = SimpleCalculator.subtraction(0, 0)
    # assert: The result should be -1 (0 - 0 - 1).
    assert result == -1

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_floats():
    """Verify subtraction with floating point numbers."""
    # arrange: (none)
    # act:
    result = SimpleCalculator.subtraction(10.5, 5.5)
    # assert: The result should be 4.0 (10.5 - 5.5 - 1.0).
    assert result == 4.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_result_zero():
    """Verify subtraction where the result (including offset) is exactly zero."""
    # arrange: (none)
    # act:
    result = SimpleCalculator.subtraction(5, 4)
    # assert: The result should be 0 (5 - 4 - 1).
    assert result == 0

@pytest.mark.generated
@pytest.mark.error_path
def test_subtraction_invalid_type():
    """Verify that passing a string as an argument raises a TypeError."""
    # arrange: (none)
    # act & assert: A TypeError should be raised.
    with pytest.raises(TypeError):
        SimpleCalculator.subtraction("10", 5)
