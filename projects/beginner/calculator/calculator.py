"""Calculator — a small CLI calculator with a real expression parser.

Supports +, -, *, /, //, %, ** and parentheses, with correct operator
precedence, using Python's own tokenizer + a recursive-descent parser
(no eval()).

Run:
    python calculator.py
    python calculator.py "3 + 4 * (2 - 1)"
"""

from __future__ import annotations

import sys
from dataclasses import dataclass


class CalculatorError(Exception):
    """Raised for any calculator-specific error (bad syntax, div by zero)."""


@dataclass
class Token:
    kind: str  # "NUM" | "OP" | "LPAREN" | "RPAREN" | "END"
    value: str


def tokenize(expression: str) -> list[Token]:
    tokens: list[Token] = []
    i = 0
    n = len(expression)
    while i < n:
        ch = expression[i]
        if ch.isspace():
            i += 1
            continue
        if ch.isdigit() or ch == ".":
            start = i
            while i < n and (expression[i].isdigit() or expression[i] == "."):
                i += 1
            tokens.append(Token("NUM", expression[start:i]))
            continue
        if ch == "(":
            tokens.append(Token("LPAREN", ch))
            i += 1
            continue
        if ch == ")":
            tokens.append(Token("RPAREN", ch))
            i += 1
            continue
        if ch in "+-*/%":
            # Handle ** as a single power operator
            if ch == "*" and i + 1 < n and expression[i + 1] == "*":
                tokens.append(Token("OP", "**"))
                i += 2
                continue
            if ch == "/" and i + 1 < n and expression[i + 1] == "/":
                tokens.append(Token("OP", "//"))
                i += 2
                continue
            tokens.append(Token("OP", ch))
            i += 1
            continue
        raise CalculatorError(f"Unexpected character: {ch!r}")
    tokens.append(Token("END", ""))
    return tokens


class Parser:
    """Recursive-descent parser implementing standard precedence:
    ( ) > ** > unary +/- > * / // % > + -
    """

    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.pos = 0

    def _peek(self) -> Token:
        return self.tokens[self.pos]

    def _advance(self) -> Token:
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def parse(self) -> float:
        result = self._expr()
        if self._peek().kind != "END":
            raise CalculatorError(f"Unexpected token: {self._peek().value!r}")
        return result

    def _expr(self) -> float:
        value = self._term()
        while self._peek().kind == "OP" and self._peek().value in ("+", "-"):
            op = self._advance().value
            rhs = self._term()
            value = value + rhs if op == "+" else value - rhs
        return value

    def _term(self) -> float:
        value = self._power()
        while self._peek().kind == "OP" and self._peek().value in ("*", "/", "//", "%"):
            op = self._advance().value
            rhs = self._power()
            if op == "*":
                value = value * rhs
            elif op == "/":
                if rhs == 0:
                    raise CalculatorError("Division by zero")
                value = value / rhs
            elif op == "//":
                if rhs == 0:
                    raise CalculatorError("Division by zero")
                value = value // rhs
            else:
                value = value % rhs
        return value

    def _power(self) -> float:
        value = self._unary()
        if self._peek().kind == "OP" and self._peek().value == "**":
            self._advance()
            exponent = self._power()  # right-associative
            value = value**exponent
        return value

    def _unary(self) -> float:
        if self._peek().kind == "OP" and self._peek().value in ("+", "-"):
            op = self._advance().value
            value = self._unary()
            return -value if op == "-" else value
        return self._atom()

    def _atom(self) -> float:
        tok = self._peek()
        if tok.kind == "NUM":
            self._advance()
            return float(tok.value)
        if tok.kind == "LPAREN":
            self._advance()
            value = self._expr()
            if self._peek().kind != "RPAREN":
                raise CalculatorError("Missing closing parenthesis")
            self._advance()
            return value
        raise CalculatorError(f"Unexpected token: {tok.value!r}")


def evaluate(expression: str) -> float:
    tokens = tokenize(expression)
    return Parser(tokens).parse()


def format_result(value: float) -> str:
    return str(int(value)) if value == int(value) else str(value)


def run_repl() -> None:
    print("Calculator — type an expression, or 'quit' to exit.")
    while True:
        try:
            expression = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if expression.lower() in ("quit", "exit"):
            break
        if not expression:
            continue
        try:
            result = evaluate(expression)
            print(format_result(result))
        except CalculatorError as exc:
            print(f"Error: {exc}")


def main() -> None:
    if len(sys.argv) > 1:
        expression = " ".join(sys.argv[1:])
        try:
            print(format_result(evaluate(expression)))
        except CalculatorError as exc:
            print(f"Error: {exc}")
            sys.exit(1)
    else:
        run_repl()


if __name__ == "__main__":
    main()
