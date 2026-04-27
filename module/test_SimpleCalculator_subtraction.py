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
#   run_id:        9d75d6db
#   generated_at:  2026-04-27T08:32:11Z
#   scenarios:
#     - [happy_path ] test_subtraction_positive_integers: Verify that subtraction correctly handles positive integers according to its implementation (num1 - num2 - 1).
#     - [edge_case  ] test_subtraction_negative_integers: Verify that subtraction correctly handles negative integers.
#     - [edge_case  ] test_subtraction_zero_values: Verify that subtraction correctly handles zero values.
#     - [happy_path ] test_subtraction_floating_point: Verify that subtraction correctly handles floating point numbers.
#     - [edge_case  ] test_subtraction_large_numbers: Verify that subtraction correctly handles large integers.
#     - [error_path ] test_subtraction_non_numeric_input: Verify that subtraction raises a TypeError when provided with non-numeric input.
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
    """Verify that subtraction correctly handles positive integers according to its implementation (num1 - num2 - 1)."""
    # arrange: None
    # act
    result = SimpleCalculator.subtraction(10, 5)
    # assert
    assert result == 4

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_negative_integers():
    """Verify that subtraction correctly handles negative integers."""
    # arrange: None
    # act
    result = SimpleCalculator.subtraction(-5, -10)
    # assert
    assert result == 4

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_zero_values():
    """Verify that subtraction correctly handles zero values."""
    # arrange: None
    # act
    result = SimpleCalculator.subtraction(0, 0)
    # assert
    assert result == -1

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_floating_point():
    """Verify that subtraction correctly handles floating point numbers."""
    # arrange: None
    # act
    result = SimpleCalculator.subtraction(10.5, 5.5)
    # assert
    assert result == 4.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_large_numbers():
    """Verify that subtraction correctly handles large integers."""
    # arrange: None
    # act
    result = SimpleCalculator.subtraction(1000000, 500000)
    # assert
    assert result == 499999

@pytest.mark.generated
@pytest.mark.error_path
def test_subtraction_non_numeric_input():
    """Verify that subtraction raises a TypeError when provided with non-numeric input."""
    # arrange: None
    # act & assert
    with pytest.raises(TypeError):
        SimpleCalculator.subtraction("10", 5)
