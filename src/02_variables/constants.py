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
    print(f"App: {APP_NAME}")
    print(f"Max retries: {MAX_RETRIES}")
    print(f"Supported formats: {SUPPORTED_FORMATS}")
    print(f"Status example: {Status.RUNNING} (value={Status.RUNNING.value})")

    # Nothing stops reassignment at runtime -- Python trusts the developer.
    global MAX_RETRIES
    MAX_RETRIES = 5
    print(f"MAX_RETRIES can technically be reassigned: {MAX_RETRIES}")


if __name__ == "__main__":
    main()
