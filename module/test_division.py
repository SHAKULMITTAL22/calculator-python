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
#   run_id:        30a9e555
#   generated_at:  2026-04-27T05:18:19Z
#   scenarios:
#     - [happy_path ] zero_numerator: Verify that dividing zero by a non-zero number returns 0.0.
#     - [edge_case  ] zero_by_zero: Verify that dividing zero by zero returns the error message "Cannot divide by zero".
#     - [error_path ] type_error_string_numerator: Verify that passing a string as the numerator raises a TypeError.
#     - [error_path ] type_error_none_denominator: Verify that passing None as the denominator raises a TypeError.
#     - [edge_case  ] infinity_numerator: Verify that dividing infinity by a finite number returns infinity.
#     - [happy_path ] very_large_integer_division: Verify that dividing very large integers (beyond standard 64-bit range) works correctly and returns a float.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc.division
# ──────────────────────────────────────────────────────

import pytest
from calc import division

@pytest.mark.generated
@pytest.mark.happy_path
def test_zero_numerator():
    """Verify that dividing zero by a non-zero number returns 0.0."""
    result = division(0, 5)
    assert result == 0.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_by_zero():
    """Verify that dividing zero by zero returns the error message "Cannot divide by zero"."""
    result = division(0, 0)
    assert result == "Cannot divide by zero"

@pytest.mark.generated
@pytest.mark.error_path
def test_type_error_string_numerator():
    """Verify that passing a string as the numerator raises a TypeError."""
    with pytest.raises(TypeError):
        division("10", 2)

@pytest.mark.generated
@pytest.mark.error_path
def test_type_error_none_denominator():
    """Verify that passing None as the denominator raises a TypeError."""
    with pytest.raises(TypeError):
        division(10, None)

@pytest.mark.generated
@pytest.mark.edge_case
def test_infinity_numerator():
    """Verify that dividing infinity by a finite number returns infinity."""
    result = division(float('inf'), 2)
    assert result == float('inf')

@pytest.mark.generated
@pytest.mark.happy_path
def test_very_large_integer_division():
    """Verify that dividing very large integers works correctly and returns a float."""
    result = division(10**20, 10**10)
    assert result == 10000000000.0
