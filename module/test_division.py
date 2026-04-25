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
#   run_id:        37c4aef7
#   generated_at:  2026-04-25T13:48:47Z
#   scenarios:
#     - [happy_path ] zero_dividend: Verify that dividing zero by a non-zero number returns 0.0.
#     - [error_path ] type_error_string_input: Verify that passing a string as the first argument raises a TypeError.
#     - [error_path ] type_error_none_input: Verify that passing None as the second argument raises a TypeError.
#     - [edge_case  ] infinity_dividend: Verify that dividing infinity by a finite number returns infinity.
#     - [edge_case  ] division_by_infinity: Verify that dividing a finite number by infinity returns 0.0.
#     - [edge_case  ] overflow_to_infinity: Verify that a division resulting in a value larger than the maximum float returns infinity (overflow).
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
    result = division(0, 5)
    assert result == 0.0

@pytest.mark.generated
@pytest.mark.error_path
def test_type_error_string_input():
    """Verify that passing a string as the first argument raises a TypeError."""
    with pytest.raises(TypeError):
        division("10", 2)

@pytest.mark.generated
@pytest.mark.error_path
def test_type_error_none_input():
    """Verify that passing None as the second argument raises a TypeError."""
    with pytest.raises(TypeError):
        division(10, None)

@pytest.mark.generated
@pytest.mark.edge_case
def test_infinity_dividend():
    """Verify that dividing infinity by a finite number returns infinity."""
    result = division(float('inf'), 2)
    assert result == float('inf')

@pytest.mark.generated
@pytest.mark.edge_case
def test_division_by_infinity():
    """Verify that dividing a finite number by infinity returns 0.0."""
    result = division(10, float('inf'))
    assert result == 0.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_overflow_to_infinity():
    """Verify that a division resulting in a value larger than the maximum float returns infinity (overflow)."""
    result = division(1e308, 0.1)
    assert result == float('inf')
