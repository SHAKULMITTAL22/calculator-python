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
#   run_id:        7b5781f7
#   generated_at:  2026-04-27T05:31:52Z
#   scenarios:
#     - [happy_path ] zero_dividend: Verify that dividing zero by a non-zero number returns 0.0.
#     - [edge_case  ] negative_zero_divisor: Verify that dividing by negative zero (-0.0) returns the error message.
#     - [edge_case  ] zero_divided_by_zero: Verify that dividing zero by zero returns the error message.
#     - [happy_path ] complex_numbers: Verify that the function correctly handles complex numbers.
#     - [error_path ] type_error_string_input: Verify that passing a string as the dividend raises a TypeError.
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
def test_zero_dividend():
    """Verify that dividing zero by a non-zero number returns 0.0."""
    assert division(0, 10) == 0.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_zero_divisor():
    """Verify that dividing by negative zero (-0.0) returns the error message."""
    assert division(10, -0.0) == "Cannot divide by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_divided_by_zero():
    """Verify that dividing zero by zero returns the error message."""
    assert division(0, 0) == "Cannot divide by zero"

@pytest.mark.generated
@pytest.mark.happy_path
def test_complex_numbers():
    """Verify that the function correctly handles complex numbers."""
    assert division(10 + 4j, 2) == 5 + 2j

@pytest.mark.generated
@pytest.mark.error_path
def test_type_error_string_input():
    """Verify that passing a string as the dividend raises a TypeError."""
    with pytest.raises(TypeError):
        division("10", 2)
