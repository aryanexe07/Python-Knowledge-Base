"""Chapter 02 · Variables — constants.py

Python has no enforced constants, only a naming convention (ALL_CAPS).
This module shows the convention and a common pattern for making
"more constant" values using tuples and Enum.

Run:
    python src/02_variables/constants.py
"""

from enum import Enum, auto

# Convention: ALL_CAPS signals "treat this as a constant" to other developers.
MAX_RETRIES = 3
DEFAULT_TIMEOUT_SECONDS = 30
APP_NAME = "Python Knowledge Base"

# Tuples are immutable, so they're a good fit for fixed collections.
SUPPORTED_FORMATS = ("json", "csv", "yaml")


class Status(Enum):
    """Enums give you a real, type-checked set of named constants."""

    PENDING = auto()
    RUNNING = auto()
    COMPLETE = auto()
    FAILED = auto()


def main() -> None:
    """Show constant naming and explain that Python does not enforce immutability."""
    print(f"App: {APP_NAME}")
    print(f"Max retries: {MAX_RETRIES}")
    print(f"Supported formats: {SUPPORTED_FORMATS}")
    print(f"Status example: {Status.RUNNING} (value={Status.RUNNING.value})")

    # Python does not enforce constants; this is only a naming convention.
    highlighted_retries = MAX_RETRIES
    print(f"MAX_RETRIES is a convention, not enforced: {highlighted_retries}")


if __name__ == "__main__":
    main()
