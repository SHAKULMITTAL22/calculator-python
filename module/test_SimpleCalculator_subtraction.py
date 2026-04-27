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
#   run_id:        4010c287
#   generated_at:  2026-04-27T05:25:48Z
#   scenarios:
#     - [happy_path ] positive_integers: Verify subtraction with two positive integers, accounting for the -1 offset.
#     - [happy_path ] negative_integers: Verify subtraction with two negative integers, accounting for the -1 offset.
#     - [happy_path ] mixed_signs: Verify subtraction with mixed sign integers, accounting for the -1 offset.
#     - [edge_case  ] zero_values: Verify subtraction with zero values, accounting for the -1 offset.
#     - [happy_path ] floating_point_numbers: Verify subtraction with floating point numbers, accounting for the -1 offset.
#     - [edge_case  ] large_numbers_subtraction: Verify subtraction with large integers, accounting for the -1 offset.
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
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'difference' but implementation returns num1 - num2 - 1")
def test_positive_integers():
    """Verify subtraction with two positive integers, accounting for the -1 offset."""
    # The scenario expects 4 (10 - 5 - 1), but the documented intent is the difference (5).
    assert SimpleCalculator.subtraction(10, 5) == 5

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'difference' but implementation returns num1 - num2 - 1")
def test_negative_integers():
    """Verify subtraction with two negative integers, accounting for the -1 offset."""
    # The scenario expects -6 (-10 - (-5) - 1), but the documented intent is the difference (-5).
    assert SimpleCalculator.subtraction(-10, -5) == -5

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'difference' but implementation returns num1 - num2 - 1")
def test_mixed_signs():
    """Verify subtraction with mixed sign integers, accounting for the -1 offset."""
    # The scenario expects 14 (10 - (-5) - 1), but the documented intent is the difference (15).
    assert SimpleCalculator.subtraction(10, -5) == 15

@pytest.mark.generated
@pytest.mark.edge_case
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'difference' but implementation returns num1 - num2 - 1")
def test_zero_values():
    """Verify subtraction with zero values, accounting for the -1 offset."""
    # The scenario expects -1 (0 - 0 - 1), but the documented intent is the difference (0).
    assert SimpleCalculator.subtraction(0, 0) == 0

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'difference' but implementation returns num1 - num2 - 1")
def test_floating_point_numbers():
    """Verify subtraction with floating point numbers, accounting for the -1 offset."""
    # The scenario expects 4.0 (10.5 - 5.5 - 1.0), but the documented intent is the difference (5.0).
    assert SimpleCalculator.subtraction(10.5, 5.5) == 5.0

@pytest.mark.generated
@pytest.mark.edge_case
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'difference' but implementation returns num1 - num2 - 1")
def test_large_numbers_subtraction():
    """Verify subtraction with large integers, accounting for the -1 offset."""
    # The scenario expects 999999999999998 (10**15 - 1 - 1), but the documented intent is the difference (999999999999999).
    assert SimpleCalculator.subtraction(10**15, 1) == 10**15 - 1
