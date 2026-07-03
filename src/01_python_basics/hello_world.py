"""Chapter 01 · Python Basics — hello_world.py

The traditional first program. Demonstrates the print() built-in,
string literals, and basic script execution.

Run:
    python src/01_python_basics/hello_world.py
"""


def main() -> None:
    """Entry point for the script."""
    print("Hello, World!")

    # print() accepts multiple arguments, joined by `sep` (default: space)
    print("Hello,", "World!", sep=" ")

    # `end` controls what's printed after the message (default: newline)
    print("Hello,", end=" ")
    print("World!")

    # f-strings (Python 3.6+) are the preferred way to format output
    name = "Python"
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
