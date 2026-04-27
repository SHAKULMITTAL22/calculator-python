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
#   run_id:        7dd18b11
#   generated_at:  2026-04-27T08:04:31Z
#   scenarios:
#     - [happy_path ] zero_numerator: Verify that dividing zero by a positive number returns 0.0.
#     - [edge_case  ] both_zero: Verify that dividing zero by zero returns the expected error message, consistent with other division-by-zero cases.
#     - [error_path ] type_error_num1_string: Verify that passing a string as the first argument raises a TypeError.
#     - [error_path ] type_error_num2_string: Verify that passing a string as the second argument raises a TypeError.
#     - [edge_case  ] infinity_numerator: Verify that dividing infinity by a finite number returns infinity.
#     - [edge_case  ] nan_numerator: Verify that dividing NaN by a number returns NaN.
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
def test_zero_numerator():
    """Verify that dividing zero by a positive number returns 0.0."""
    result = division(0, 10)
    assert result == 0.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_both_zero():
    """Verify that dividing zero by zero returns the expected error message."""
    result = division(0, 0)
    assert result == "Cannot divide by zero"

@pytest.mark.generated
@pytest.mark.error_path
def test_type_error_num1_string():
    """Verify that passing a string as the first argument raises a TypeError."""
    with pytest.raises(TypeError):
        division("10", 2)

@pytest.mark.generated
@pytest.mark.error_path
def test_type_error_num2_string():
    """Verify that passing a string as the second argument raises a TypeError."""
    with pytest.raises(TypeError):
        division(10, "2")

@pytest.mark.generated
@pytest.mark.edge_case
def test_infinity_numerator():
    """Verify that dividing infinity by a finite number returns infinity."""
    result = division(float('inf'), 2)
    assert result == float('inf')

@pytest.mark.generated
@pytest.mark.edge_case
def test_nan_numerator():
    """Verify that dividing NaN by a number returns NaN."""
    result = division(float('nan'), 2)
    assert math.isnan(result)
