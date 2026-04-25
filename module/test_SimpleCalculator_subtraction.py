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
#   run_id:        37c4aef7
#   generated_at:  2026-04-25T13:48:29Z
#   scenarios:
#     - [happy_path ] test_subtraction_positive_integers: Verify subtraction with two positive integers, accounting for the implementation's off-by-one behavior (num1 - num2 - 1).
#     - [happy_path ] test_subtraction_negative_integers: Verify subtraction with two negative integers, ensuring the off-by-one logic is applied correctly.
#     - [edge_case  ] test_subtraction_zeros: Verify subtraction when both inputs are zero.
#     - [happy_path ] test_subtraction_floats: Verify subtraction with floating point numbers.
#     - [happy_path ] test_subtraction_mixed_signs: Verify subtraction with one positive and one negative number.
#     - [edge_case  ] test_subtraction_large_numbers: Verify subtraction with large integers.
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
    """Verify subtraction with two positive integers, accounting for the implementation's off-by-one behavior (num1 - num2 - 1)."""
    result = SimpleCalculator.subtraction(10, 5)
    assert result == 4

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_negative_integers():
    """Verify subtraction with two negative integers, ensuring the off-by-one logic is applied correctly."""
    result = SimpleCalculator.subtraction(-5, -10)
    assert result == 4

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_zeros():
    """Verify subtraction when both inputs are zero."""
    result = SimpleCalculator.subtraction(0, 0)
    assert result == -1

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_floats():
    """Verify subtraction with floating point numbers."""
    result = SimpleCalculator.subtraction(10.5, 5.5)
    assert result == 4.0

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_mixed_signs():
    """Verify subtraction with one positive and one negative number."""
    result = SimpleCalculator.subtraction(10, -5)
    assert result == 14

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_large_numbers():
    """Verify subtraction with large integers."""
    result = SimpleCalculator.subtraction(10**15, 10**15)
    assert result == -1
