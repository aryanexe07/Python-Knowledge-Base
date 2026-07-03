"""Tests for calculator.py — run with: pytest test_calculator.py"""

import pytest

from calculator import CalculatorError, evaluate


def test_basic_arithmetic():
    assert evaluate("2 + 3") == 5
    assert evaluate("10 - 4") == 6
    assert evaluate("6 * 7") == 42
    assert evaluate("8 / 2") == 4


def test_precedence():
    assert evaluate("3 + 4 * 2") == 11
    assert evaluate("(3 + 4) * 2") == 14


def test_power_right_associative():
    assert evaluate("2 ** 3 ** 2") == 512  # 2 ** (3 ** 2), not (2 ** 3) ** 2


def test_unary_minus():
    assert evaluate("-5 + 3") == -2
    assert evaluate("-(2 + 3)") == -5


def test_floor_div_and_mod():
    assert evaluate("10 // 3") == 3
    assert evaluate("10 % 3") == 1


def test_division_by_zero_raises():
    with pytest.raises(CalculatorError):
        evaluate("5 / 0")


def test_unmatched_parenthesis_raises():
    with pytest.raises(CalculatorError):
        evaluate("(3 + 4")
