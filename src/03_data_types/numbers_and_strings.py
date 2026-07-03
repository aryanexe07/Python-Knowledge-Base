"""Chapter 03 · Data Types — numbers_and_strings.py

Demonstrates scalar types: int, float, bool, str, None, and the
classic floating-point precision pitfall.

Run:
    python src/03_data_types/numbers_and_strings.py
"""

import math


def numeric_types() -> None:
    """Demonstrate numeric scalar types and their runtime behavior."""
    i: int = 42
    f: float = 3.14
    b: bool = True  # bool is a subclass of int: True == 1, False == 0
    c: complex = 2 + 3j

    print(f"int: {i} ({type(i).__name__})")
    print(f"float: {f} ({type(f).__name__})")
    print(f"bool: {b} ({type(b).__name__}), True + True = {True + True}")
    print(f"complex: {c} ({type(c).__name__})")


def float_precision_pitfall() -> None:
    """Show floating-point rounding issues and how to compare values safely."""
    result = 0.1 + 0.2
    print(f"0.1 + 0.2 = {result}")
    print(f"0.1 + 0.2 == 0.3 -> {result == 0.3}")  # False, due to binary floats
    print(f"math.isclose fix -> {math.isclose(result, 0.3)}")  # True


def string_basics() -> None:
    """Demonstrate common string operations and immutability."""
    s = "Python"
    print(f"upper: {s.upper()}")
    print(f"lower: {s.lower()}")
    print(f"slice s[1:4]: {s[1:4]}")
    print(f"reversed: {s[::-1]}")
    print(f"f-string: {s} is {len(s)} characters long")

    # Strings are immutable: this creates a new string, doesn't mutate `s`
    upper_s = s.upper()
    print(f"original unchanged: s={s}, upper_s={upper_s}")


def none_type() -> None:
    """Demonstrate the None singleton and its identity comparison."""
    value = None
    print(f"value is None -> {value is None}")  # always use `is` for None checks


if __name__ == "__main__":
    numeric_types()
    float_precision_pitfall()
    string_basics()
    none_type()
