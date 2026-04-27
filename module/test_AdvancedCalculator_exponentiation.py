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
#   run_id:        30a9e555
#   generated_at:  2026-04-27T05:20:00Z
#   scenarios:
#     - [happy_path ] positive_integers: Test exponentiation with positive integer base and exponent.
#     - [edge_case  ] zero_exponent: Test that any non-zero base raised to the power of zero is 1.
#     - [edge_case  ] negative_exponent: Test exponentiation with a negative exponent, resulting in a fraction.
#     - [edge_case  ] negative_base_even_exponent: Test that a negative base raised to an even exponent results in a positive value.
#     - [edge_case  ] fractional_exponent: Test exponentiation with a fractional exponent (square root).
#     - [error_path ] zero_base_negative_exponent: Test that raising zero to a negative power raises a ZeroDivisionError.
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
    """Test exponentiation with positive integer base and exponent."""
    assert AdvancedCalculator.exponentiation(2, 3) == 8

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_exponent():
    """Test that any non-zero base raised to the power of zero is 1."""
    assert AdvancedCalculator.exponentiation(5, 0) == 1

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_exponent():
    """Test exponentiation with a negative exponent, resulting in a fraction."""
    assert AdvancedCalculator.exponentiation(2, -2) == 0.25

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_base_even_exponent():
    """Test that a negative base raised to an even exponent results in a positive value."""
    assert AdvancedCalculator.exponentiation(-2, 4) == 16

@pytest.mark.generated
@pytest.mark.edge_case
def test_fractional_exponent():
    """Test exponentiation with a fractional exponent (square root)."""
    assert AdvancedCalculator.exponentiation(9, 0.5) == 3.0

@pytest.mark.generated
@pytest.mark.error_path
def test_zero_base_negative_exponent():
    """Test that raising zero to a negative power raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        AdvancedCalculator.exponentiation(0, -1)
