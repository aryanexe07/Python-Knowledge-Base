"""Chapter 03 · Data Types — collections_demo.py

Demonstrates list, tuple, dict, and set — including the classic
"list as dict key" TypeError and an order-preserving dedup exercise.

Run:
    python src/03_data_types/collections_demo.py
"""


def list_and_tuple() -> None:
    numbers: list[int] = [4, 2, 8, 1]
    numbers.append(10)
    numbers.sort()
    print(f"sorted list: {numbers}")

    point: tuple[int, int] = (3, 4)
    print(f"tuple (fixed shape): {point}")

    try:
        point[0] = 99  # type: ignore[index]
    except TypeError as exc:
        print(f"tuples are immutable: {exc}")


def dict_and_set() -> None:
    scores: dict[str, int] = {"alice": 90, "bob": 85}
    scores["carol"] = 95
    print(f"dict: {scores}")

    unique_ids: set[int] = {1, 2, 2, 3, 3, 3}
    print(f"set removes duplicates: {unique_ids}")

    try:
        bad_key: dict[list, str] = {[1, 2]: "value"}  # type: ignore[misc]
    except TypeError as exc:
        print(f"lists can't be dict keys (unhashable): {exc}")


def stats_from_numbers(numbers: list[float]) -> tuple[float, float, float]:
    """Return (min, max, average) as a tuple."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


def dedupe_preserving_order(items: list[int]) -> list[int]:
    """Deduplicate a list while preserving first-seen order."""
    seen: set[int] = set()
    result: list[int] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    list_and_tuple()
    dict_and_set()

    print(f"stats: {stats_from_numbers([4, 8, 15, 16, 23, 42])}")
    print(f"dedup: {dedupe_preserving_order([3, 1, 3, 2, 1, 4])}")
