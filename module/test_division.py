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
#   run_id:        abeed5a2
#   generated_at:  2026-04-27T07:38:31Z
#   scenarios:
#     - [happy_path ] zero_dividend: Verify that dividing zero by a non-zero number returns 0.0.
#     - [edge_case  ] float_zero_divisor: Verify that dividing by 0.0 (float) returns the error message.
#     - [edge_case  ] infinity_dividend: Verify that dividing infinity by a finite number returns infinity.
#     - [edge_case  ] infinity_divisor: Verify that dividing a finite number by infinity returns 0.0.
#     - [error_path ] type_error_string: Verify that passing a string as an argument raises a TypeError.
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
def test_float_zero_divisor():
    """Verify that dividing by 0.0 (float) returns the error message."""
    assert division(10, 0.0) == "Cannot divide by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_infinity_dividend():
    """Verify that dividing infinity by a finite number returns infinity."""
    assert division(float('inf'), 2) == float('inf')

@pytest.mark.generated
@pytest.mark.edge_case
def test_infinity_divisor():
    """Verify that dividing a finite number by infinity returns 0.0."""
    assert division(10, float('inf')) == 0.0

@pytest.mark.generated
@pytest.mark.error_path
def test_type_error_string():
    """Verify that passing a string as an argument raises a TypeError."""
    with pytest.raises(TypeError):
        division("10", 2)
