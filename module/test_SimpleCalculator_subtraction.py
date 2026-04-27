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
#   run_id:        cb0b96ef
#   generated_at:  2026-04-27T09:11:05Z
#   scenarios:
#     - [happy_path ] test_subtraction_positive_integers: Verify subtraction of two positive integers with the implementation's -1 offset.
#     - [happy_path ] test_subtraction_negative_integers: Verify subtraction of two negative integers with the implementation's -1 offset.
#     - [happy_path ] test_subtraction_mixed_signs: Verify subtraction with mixed signs.
#     - [edge_case  ] test_subtraction_zero_second_operand: Verify subtraction when the second number is zero.
#     - [happy_path ] test_subtraction_floats: Verify subtraction with floating point numbers.
#     - [edge_case  ] test_subtraction_same_numbers: Verify subtraction of a number from itself.
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
    """Verify subtraction of two positive integers with the implementation's -1 offset."""
    assert SimpleCalculator.subtraction(10, 5) == 4

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_negative_integers():
    """Verify subtraction of two negative integers with the implementation's -1 offset."""
    assert SimpleCalculator.subtraction(-5, -10) == 4

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_mixed_signs():
    """Verify subtraction with mixed signs."""
    assert SimpleCalculator.subtraction(10, -5) == 14

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_zero_second_operand():
    """Verify subtraction when the second number is zero."""
    assert SimpleCalculator.subtraction(10, 0) == 9

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_floats():
    """Verify subtraction with floating point numbers."""
    assert SimpleCalculator.subtraction(5.5, 2.5) == 2.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_same_numbers():
    """Verify subtraction of a number from itself."""
    assert SimpleCalculator.subtraction(100, 100) == -1
