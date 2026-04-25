ROOST_METHOD_HASH=SimpleCalculator.subtraction_4ae60a35a2
ROOST_METHOD_SIG_HASH=SimpleCalculator.subtraction_4ae60a35a2

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
#   run_id:        a9ed4208
#   generated_at:  2026-04-25T13:31:31Z
#   scenarios:
#     - [happy_path ] test_subtraction_positive_integers: Verify that subtracting a smaller positive integer from a larger one returns the correct difference.
#     - [happy_path ] test_subtraction_negative_numbers: Verify that subtraction involving negative numbers correctly handles the signs and returns the expected difference.
#     - [edge_case  ] test_subtraction_with_zero_subtrahend: Verify that subtracting zero from a number returns the number itself.
#     - [happy_path ] test_subtraction_floats: Verify that the function correctly handles floating-point numbers and returns an accurate difference.
#     - [edge_case  ] test_subtraction_same_numbers: Verify that subtracting a number from itself returns zero.
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
    """Verify that subtracting a smaller positive integer from a larger one returns the correct difference."""
    assert SimpleCalculator.subtraction(10, 5) == 5

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_negative_numbers():
    """Verify that subtraction involving negative numbers correctly handles the signs and returns the expected difference."""
    assert SimpleCalculator.subtraction(-5, -15) == 10

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_with_zero_subtrahend():
    """Verify that subtracting zero from a number returns the number itself."""
    assert SimpleCalculator.subtraction(10, 0) == 10

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_floats():
    """Verify that the function correctly handles floating-point numbers and returns an accurate difference."""
    assert SimpleCalculator.subtraction(5.5, 2.5) == 3.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_same_numbers():
    """Verify that subtracting a number from itself returns zero."""
    assert SimpleCalculator.subtraction(5, 5) == 0
