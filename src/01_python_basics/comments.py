"""Chapter 01 · Python Basics — comments.py

Demonstrates the three practical comment styles used in Python code.

Run:
    python src/01_python_basics/comments.py
"""

# 1. Line comment: explains the line(s) below it.
# Calculate the area of a rectangle.
WIDTH = 4
HEIGHT = 5
AREA = WIDTH * HEIGHT  # 2. Inline comment: explains this specific line

"""
3. Block comment (technically a standalone string literal, but commonly
used as a multi-line explanatory block, e.g. at the top of a script or
before a complex section of code).
"""


def describe_area() -> None:
    """Docstring: NOT a comment — this is metadata the interpreter stores
    on the function object (accessible via describe_area.__doc__) and
    tools like help() read. Use docstrings for anything that documents
    *what a function/class/module does*, comments for *why the code does
    what it does*.
    """
    print(f"A {WIDTH}x{HEIGHT} rectangle has an area of {AREA}.")


if __name__ == "__main__":
    describe_area()
    print(describe_area.__doc__)
