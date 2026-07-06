"""
Chapter 04 · Operators

Today we will learn about operators in Python.

Operators are special symbols used to perform operations on values and variables.

Python provides the following categories of operators:

    • Arithmetic Operators
    • Comparison Operators
    • Logical Operators
    • Assignment Operators
    • Bitwise Operators
    • Membership Operators
    • Identity Operators
"""


def main() -> None:
    # --------------------------------------------------
    # Arithmetic Operators
    # --------------------------------------------------
    print("=== Arithmetic Operators ===")

    a = 10
    b = 3

    print(f"{a} + {b} =", a + b)  # Addition
    print(f"{a} - {b} =", a - b)  # Subtraction
    print(f"{a} * {b} =", a * b)  # Multiplication
    print(f"{a} / {b} =", a / b)  # Division
    print(f"{a} // {b} =", a // b)  # Floor Division
    print(f"{a} % {b} =", a % b)  # Modulus
    print(f"{a} ** {b} =", a**b)  # Exponentiation

    print()

    # --------------------------------------------------
    # Comparison Operators
    # --------------------------------------------------
    print("=== Comparison Operators ===")

    print(f"{a} == {b} ->", a == b)
    print(f"{a} != {b} ->", a != b)
    print(f"{a} > {b} ->", a > b)
    print(f"{a} < {b} ->", a < b)
    print(f"{a} >= {b} ->", a >= b)
    print(f"{a} <= {b} ->", a <= b)

    print()

    # --------------------------------------------------
    # Logical Operators
    # --------------------------------------------------
    print("=== Logical Operators ===")

    x = True
    y = False

    print("True and False ->", x and y)
    print("True or False  ->", x or y)
    print("not True       ->", not x)

    print()

    # --------------------------------------------------
    # Assignment Operators
    # --------------------------------------------------
    print("=== Assignment Operators ===")

    num = 10
    print("Initial value:", num)

    num += 5
    print("After += 5 :", num)

    num -= 3
    print("After -= 3 :", num)

    num *= 2
    print("After *= 2 :", num)

    num /= 4
    print("After /= 4 :", num)

    num %= 3
    print("After %= 3 :", num)

    num **= 2
    print("After **= 2:", num)

    num //= 2
    print("After //= 2:", num)

    print()

    # --------------------------------------------------
    # Bitwise Operators
    # --------------------------------------------------
    print("=== Bitwise Operators ===")

    a = 5  # 0101
    b = 3  # 0011

    print(f"{a} & {b} =", a & b)
    print(f"{a} | {b} =", a | b)
    print(f"{a} ^ {b} =", a ^ b)
    print(f"~{a} =", ~a)
    print(f"{a} << 1 =", a << 1)
    print(f"{a} >> 1 =", a >> 1)

    print()

    # --------------------------------------------------
    # Membership Operators
    # --------------------------------------------------
    print("=== Membership Operators ===")

    text = "Python Programming"

    print("'Python' in text     ->", "Python" in text)
    print("'Java' in text       ->", "Java" in text)
    print("'Java' not in text   ->", "Java" not in text)

    numbers = [1, 2, 3, 4, 5]

    print("3 in numbers         ->", 3 in numbers)
    print("10 not in numbers    ->", 10 not in numbers)

    print()

    # --------------------------------------------------
    # Identity Operators
    # --------------------------------------------------
    print("=== Identity Operators ===")

    list1 = [1, 2, 3]
    list2 = list1
    list3 = [1, 2, 3]

    print("list1 is list2      ->", list1 is list2)
    print("list1 is list3      ->", list1 is list3)

    print("list1 == list3      ->", list1 == list3)

    print("list1 is not list3  ->", list1 is not list3)


if __name__ == "__main__":
    main()
