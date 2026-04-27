# ROOST_METHOD_HASH=AdvancedCalculator.exponentiation_e4ad67523b
# ROOST_METHOD_SIG_HASH=AdvancedCalculator.exponentiation_e4ad67523b

"""Auto-generated unit tests for `calc_advance.AdvancedCalculator.exponentiation`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc_advance.AdvancedCalculator.exponentiation
#   source:        calc_advance.py:10-12
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        7b5781f7
#   generated_at:  2026-04-27T05:33:14Z
#   scenarios:
#     - [happy_path ] positive_integers: Verify exponentiation with positive integers.
#     - [happy_path ] zero_exponent: Verify that any non-zero number raised to the power of zero is 1.
#     - [edge_case  ] negative_exponent: Verify exponentiation with a negative exponent results in a fraction.
#     - [error_path ] zero_base_negative_exponent: Verify that raising zero to a negative power raises ZeroDivisionError.
#     - [edge_case  ] negative_base_fractional_exponent: Verify that raising a negative number to a fractional power returns a complex number.
#     - [edge_case  ] zero_to_zero: Verify that zero raised to the power of zero is 1 (Python standard behavior).
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc_advance.AdvancedCalculator.exponentiation
# ──────────────────────────────────────────────────────

import pytest
from calc_advance import AdvancedCalculator

@pytest.mark.generated
@pytest.mark.happy_path
def test_positive_integers():
    """Verify exponentiation with positive integers."""
    result = AdvancedCalculator.exponentiation(2, 3)
    assert result == 8

@pytest.mark.generated
@pytest.mark.happy_path
def test_zero_exponent():
    """Verify that any non-zero number raised to the power of zero is 1."""
    result = AdvancedCalculator.exponentiation(5, 0)
    assert result == 1

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_exponent():
    """Verify exponentiation with a negative exponent results in a fraction."""
    result = AdvancedCalculator.exponentiation(2, -2)
    assert result == 0.25

@pytest.mark.generated
@pytest.mark.error_path
def test_zero_base_negative_exponent():
    """Verify that raising zero to a negative power raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        AdvancedCalculator.exponentiation(0, -1)

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_base_fractional_exponent():
    """Verify that raising a negative number to a fractional power returns a complex number."""
    result = AdvancedCalculator.exponentiation(-4, 0.5)
    # Python's (-4)**0.5 is (1.2246467991473532e-16+2j) due to floating point precision.
    # pytest.approx handles complex numbers by comparing their absolute difference.
    assert result == pytest.approx(2j)

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_to_zero():
    """Verify that zero raised to the power of zero is 1 (Python standard behavior)."""
    result = AdvancedCalculator.exponentiation(0, 0)
    assert result == 1
