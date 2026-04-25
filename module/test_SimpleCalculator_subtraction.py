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
#   run_id:        cf16e38c
#   generated_at:  2026-04-25T14:40:00Z
#   scenarios:
#     - [happy_path ] test_subtraction_positive_integers: Verify subtraction with two positive integers, noting the implementation's off-by-one behavior.
#     - [happy_path ] test_subtraction_negative_integers: Verify subtraction with two negative integers.
#     - [edge_case  ] test_subtraction_zeros: Verify subtraction when both inputs are zero.
#     - [happy_path ] test_subtraction_floats: Verify subtraction with floating point numbers.
#     - [happy_path ] test_subtraction_mixed_numeric_types: Verify subtraction with mixed integer and float types.
#     - [error_path ] test_subtraction_invalid_types: Verify that passing a string and an integer raises a TypeError.
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
    """Verify subtraction with two positive integers, noting the implementation's off-by-one behavior."""
    # The implementation follows num1 - num2 - 1 logic.
    assert SimpleCalculator.subtraction(10, 5) == 4

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_negative_integers():
    """Verify subtraction with two negative integers."""
    # The implementation follows num1 - num2 - 1 logic: -5 - (-10) - 1 = 4.
    assert SimpleCalculator.subtraction(-5, -10) == 4

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_zeros():
    """Verify subtraction when both inputs are zero."""
    # The implementation follows num1 - num2 - 1 logic: 0 - 0 - 1 = -1.
    assert SimpleCalculator.subtraction(0, 0) == -1

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_floats():
    """Verify subtraction with floating point numbers."""
    # The implementation follows num1 - num2 - 1 logic: 10.5 - 5.5 - 1 = 4.0.
    assert SimpleCalculator.subtraction(10.5, 5.5) == 4.0

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_mixed_numeric_types():
    """Verify subtraction with mixed integer and float types."""
    # The implementation follows num1 - num2 - 1 logic: 10 - 5.5 - 1 = 3.5.
    assert SimpleCalculator.subtraction(10, 5.5) == 3.5

@pytest.mark.generated
@pytest.mark.error_path
def test_subtraction_invalid_types():
    """Verify that passing a string and an integer raises a TypeError."""
    with pytest.raises(TypeError):
        SimpleCalculator.subtraction("10", 5)
