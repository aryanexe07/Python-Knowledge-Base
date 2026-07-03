"""Chapter 02 · Variables — variables.py

Demonstrates assignment, multiple assignment, chained assignment,
augmented assignment, and the reference semantics of Python names.

Run:
    python src/02_variables/variables.py
"""


def basic_assignment() -> None:
    """Show basic assignment of simple values."""
    x = 10
    name = "Aryan"
    is_active = True
    print(f"x={x}, name={name!r}, is_active={is_active}")


def multiple_assignment() -> None:
    """Show multiple assignment with tuple unpacking."""
    a, b, c = 1, 2, 3
    print(f"a={a}, b={b}, c={c}")


def chained_assignment_pitfall() -> None:
    """Show the difference between immutable and mutable chained assignment."""
    # Safe: integers are immutable
    x = y = 0
    x += 1
    print(f"immutable chained: x={x}, y={y}")  # y stays 0

    # Risky: lists are mutable and shared
    shared = other = []
    shared.append(1)
    print(f"mutable chained: shared={shared}, other={other}")  # both [1]


def augmented_assignment() -> None:
    """Show augmented assignment inside a loop."""
    count = 0
    for _ in range(5):
        count += 1
    print(f"count after loop: {count}")


def swap_without_temp() -> None:
    """Swap two values without using a temporary variable."""
    a, b = 1, 2
    a, b = b, a  # tuple unpacking swap, no temp variable needed
    print(f"swapped: a={a}, b={b}")


if __name__ == "__main__":
    basic_assignment()
    multiple_assignment()
    chained_assignment_pitfall()
    augmented_assignment()
    swap_without_temp()
