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
#   run_id:        cb0b96ef
#   generated_at:  2026-04-27T09:10:51Z
#   scenarios:
#     - [happy_path ] zero_numerator: Verify that dividing zero by a non-zero number returns 0.0.
#     - [edge_case  ] float_zero_denominator: Verify that the function handles float zero (0.0) as a denominator.
#     - [edge_case  ] zero_divided_by_zero: Verify that 0 divided by 0 returns the error message.
#     - [edge_case  ] infinity_denominator: Verify that dividing by infinity returns 0.0.
#     - [error_path ] string_input_raises_type_error: Verify that passing a string as an argument raises a TypeError.
#     - [edge_case  ] overflow_to_infinity: Verify that a division resulting in a value larger than the maximum float returns infinity.
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
def test_float_zero_denominator():
    """Verify that the function handles float zero (0.0) as a denominator."""
    result = division(10, 0.0)
    assert result == "Cannot divide by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_divided_by_zero():
    """Verify that 0 divided by 0 returns the error message."""
    result = division(0, 0)
    assert result == "Cannot divide by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_infinity_denominator():
    """Verify that dividing by infinity returns 0.0."""
    result = division(10, float('inf'))
    assert result == 0.0

@pytest.mark.generated
@pytest.mark.error_path
def test_string_input_raises_type_error():
    """Verify that passing a string as an argument raises a TypeError."""
    with pytest.raises(TypeError):
        division("10", 2)

@pytest.mark.generated
@pytest.mark.edge_case
def test_overflow_to_infinity():
    """Verify that a division resulting in a value larger than the maximum float returns infinity."""
    result = division(1e308, 1e-10)
    assert result == float('inf')
