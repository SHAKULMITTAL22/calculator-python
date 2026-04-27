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
#   run_id:        7dd18b11
#   generated_at:  2026-04-27T08:04:35Z
#   scenarios:
#     - [happy_path ] test_subtraction_positive_integers: Verify subtraction of two positive integers.
#     - [happy_path ] test_subtraction_negative_integers: Verify subtraction of two negative integers.
#     - [edge_case  ] test_subtraction_zeros: Verify subtraction when both numbers are zero.
#     - [happy_path ] test_subtraction_floats: Verify subtraction of floating point numbers.
#     - [happy_path ] test_subtraction_mixed_signs: Verify subtraction with one positive and one negative number.
#     - [error_path ] test_subtraction_invalid_types: Verify that passing non-numeric types raises a TypeError.
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
    """Verify subtraction of two positive integers."""
    # act
    result = SimpleCalculator.subtraction(10, 5)
    # assert
    assert result == 4

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_negative_integers():
    """Verify subtraction of two negative integers."""
    # act
    result = SimpleCalculator.subtraction(-5, -10)
    # assert
    assert result == 4

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_zeros():
    """Verify subtraction when both numbers are zero."""
    # act
    result = SimpleCalculator.subtraction(0, 0)
    # assert
    assert result == -1

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_floats():
    """Verify subtraction of floating point numbers."""
    # act
    result = SimpleCalculator.subtraction(10.5, 5.5)
    # assert
    assert result == 4.0

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_mixed_signs():
    """Verify subtraction with one positive and one negative number."""
    # act
    result = SimpleCalculator.subtraction(10, -5)
    # assert
    assert result == 14

@pytest.mark.generated
@pytest.mark.error_path
def test_subtraction_invalid_types():
    """Verify that passing non-numeric types raises a TypeError."""
    # act & assert
    with pytest.raises(TypeError):
        SimpleCalculator.subtraction("10", "5")
