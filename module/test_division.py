# ROOST_METHOD_HASH=division_641e53a5f9
# ROOST_METHOD_SIG_HASH=division_641e53a5f9

"""Auto-generated unit tests for `calc.division`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc.division
#   source:        calc.py:29-33
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        65c7fe6f
#   generated_at:  2026-04-27T08:57:43Z
#   scenarios:
#     - [happy_path ] test_zero_dividend: Verify that dividing zero by any non-zero number returns 0.0.
#     - [edge_case  ] test_float_zero_divisor: Verify that dividing by float zero (0.0) returns the error message "Cannot divide by zero".
#     - [edge_case  ] test_negative_zero_divisor: Verify that dividing by negative float zero (-0.0) returns the error message.
#     - [edge_case  ] test_infinity_dividend: Verify that dividing infinity by a finite number returns infinity.
#     - [edge_case  ] test_nan_input: Verify that dividing NaN by a number returns NaN.
#     - [error_path ] test_type_error_on_string: Verify that passing a string as an argument raises a TypeError.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc.division
# ──────────────────────────────────────────────────────

import pytest
import math
from calc import division

@pytest.mark.generated
@pytest.mark.happy_path
def test_zero_dividend():
    """Verify that dividing zero by any non-zero number returns 0.0."""
    result = division(0, 10)
    assert result == 0.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_float_zero_divisor():
    """Verify that dividing by float zero (0.0) returns the error message 'Cannot divide by zero'."""
    result = division(10, 0.0)
    assert result == "Cannot divide by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_zero_divisor():
    """Verify that dividing by negative float zero (-0.0) returns the error message."""
    result = division(10, -0.0)
    assert result == "Cannot divide by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_infinity_dividend():
    """Verify that dividing infinity by a finite number returns infinity."""
    result = division(float('inf'), 2)
    assert result == float('inf')

@pytest.mark.generated
@pytest.mark.edge_case
def test_nan_input():
    """Verify that dividing NaN by a number returns NaN."""
    result = division(float('nan'), 5)
    assert math.isnan(result)

@pytest.mark.generated
@pytest.mark.error_path
def test_type_error_on_string():
    """Verify that passing a string as an argument raises a TypeError."""
    with pytest.raises(TypeError):
        division("10", 2)
