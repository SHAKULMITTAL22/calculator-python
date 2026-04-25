ROOST_METHOD_HASH=AdvancedCalculator.absolute_difference_dce44fd78e
ROOST_METHOD_SIG_HASH=AdvancedCalculator.absolute_difference_dce44fd78e

"""Auto-generated unit tests for `calc_advance.AdvancedCalculator.absolute_difference`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc_advance.AdvancedCalculator.absolute_difference
#   source:        calc_advance.py:22-24
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        a9ed4208
#   generated_at:  2026-04-25T13:32:00Z
#   scenarios:
#     - [happy_path ] test_positive_integers: Verify the absolute difference between two positive integers.
#     - [happy_path ] test_negative_and_positive_integers: Verify the absolute difference between a negative and a positive integer.
#     - [happy_path ] test_both_negative_integers: Verify the absolute difference between two negative integers.
#     - [edge_case  ] test_zero_values_both: Verify the absolute difference between two zeros.
#     - [edge_case  ] test_identical_numbers: Verify the absolute difference between two identical numbers is zero.
#     - [happy_path ] test_floating_point_numbers: Verify the absolute difference with floating point numbers.
#     - [property   ] test_symmetry_property: Verify that the absolute difference is symmetric (order of arguments doesn't matter).
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc_advance.AdvancedCalculator.absolute_difference
# ──────────────────────────────────────────────────────

import pytest
from calc_advance import AdvancedCalculator

@pytest.mark.generated
@pytest.mark.happy_path
def test_positive_integers():
    """Verify the absolute difference between two positive integers."""
    result = AdvancedCalculator.absolute_difference(10, 3)
    assert result == 7

@pytest.mark.generated
@pytest.mark.happy_path
def test_negative_and_positive_integers():
    """Verify the absolute difference between a negative and a positive integer."""
    result = AdvancedCalculator.absolute_difference(-5, 5)
    assert result == 10

@pytest.mark.generated
@pytest.mark.happy_path
def test_both_negative_integers():
    """Verify the absolute difference between two negative integers."""
    result = AdvancedCalculator.absolute_difference(-10, -3)
    assert result == 7

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_values_both():
    """Verify the absolute difference between two zeros."""
    result = AdvancedCalculator.absolute_difference(0, 0)
    assert result == 0

@pytest.mark.generated
@pytest.mark.edge_case
def test_identical_numbers():
    """Verify the absolute difference between two identical numbers is zero."""
    result = AdvancedCalculator.absolute_difference(42, 42)
    assert result == 0

@pytest.mark.generated
@pytest.mark.happy_path
def test_floating_point_numbers():
    """Verify the absolute difference with floating point numbers."""
    result = AdvancedCalculator.absolute_difference(5.5, 2.1)
    assert result == pytest.approx(3.4)

@pytest.mark.generated
@pytest.mark.property
def test_symmetry_property():
    """Verify that the absolute difference is symmetric (order of arguments doesn't matter)."""
    assert AdvancedCalculator.absolute_difference(10, 3) == AdvancedCalculator.absolute_difference(3, 10)
