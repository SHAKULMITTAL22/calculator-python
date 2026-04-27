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
#   run_id:        7b5781f7
#   generated_at:  2026-04-27T05:31:38Z
#   scenarios:
#     - [happy_path ] test_subtraction_positive_integers: Verify that subtraction of two positive integers returns (num1 - num2 - 1).
#     - [edge_case  ] test_subtraction_negative_integers: Verify that subtraction of two negative integers correctly handles signs and the additional -1.
#     - [edge_case  ] test_subtraction_zeros: Verify that subtraction of two zeros returns -1.
#     - [happy_path ] test_subtraction_floats: Verify that subtraction works correctly with floating point numbers.
#     - [happy_path ] test_subtraction_mixed_signs: Verify subtraction with mixed positive and negative integers.
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
    """Verify that subtraction of two positive integers returns (num1 - num2 - 1)."""
    assert SimpleCalculator.subtraction(10, 5) == 4

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_negative_integers():
    """Verify that subtraction of two negative integers correctly handles signs and the additional -1."""
    assert SimpleCalculator.subtraction(-5, -10) == 4

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_zeros():
    """Verify that subtraction of two zeros returns -1."""
    assert SimpleCalculator.subtraction(0, 0) == -1

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_floats():
    """Verify that subtraction works correctly with floating point numbers."""
    assert SimpleCalculator.subtraction(5.5, 2.5) == 2.0

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_mixed_signs():
    """Verify subtraction with mixed positive and negative integers."""
    # 10 - (-5) - 1 = 10 + 5 - 1 = 14
    assert SimpleCalculator.subtraction(10, -5) == 14

@pytest.mark.generated
@pytest.mark.error_path
def test_subtraction_invalid_type():
    """Verify that passing a string as an argument raises a TypeError."""
    with pytest.raises(TypeError):
        SimpleCalculator.subtraction("10", 5)
