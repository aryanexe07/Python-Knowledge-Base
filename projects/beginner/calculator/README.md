# Calculator

A CLI calculator with a real recursive-descent parser — no `eval()`. Supports `+ - * / // % **`, parentheses, unary minus, and correct operator precedence (including right-associative `**`).

## Features

- Tokenizer + recursive-descent parser (see [Chapter 11: OOP](../../../docs/11_oop/README.md) style patterns applied)
- Correct precedence: `()` > `**` > unary `+/-` > `* / // %` > `+ -`
- Interactive REPL mode and single-expression CLI mode
- Proper error handling (division by zero, unmatched parentheses, invalid characters)
- Full test suite with `pytest`

## Requirements

```
pytest>=8.2.0
```

Install: `pip install -r ../../../requirements.txt`

## Usage

**REPL mode:**
```bash
python calculator.py
>>> 3 + 4 * (2 - 1)
7
>>> 2 ** 10
1024
>>> quit
```

**Single expression:**
```bash
python calculator.py "3 + 4 * (2 - 1)"
# 7
```

## Running Tests

```bash
pytest test_calculator.py -v
```

## Project Structure

```
calculator/
├── README.md
├── calculator.py       # tokenizer, parser, evaluator, CLI/REPL
├── test_calculator.py  # pytest suite
└── screenshots/
```

## Screenshots

<!-- Add a terminal screenshot of the REPL in action -->
`screenshots/repl_demo.png`

## How It Works

1. **Tokenize** — the raw string is split into `NUM`, `OP`, `LPAREN`, `RPAREN` tokens.
2. **Parse** — a recursive-descent parser walks the tokens using one method per precedence level (`_expr` → `_term` → `_power` → `_unary` → `_atom`), so precedence is enforced by the call structure itself rather than a lookup table.
3. **Evaluate** — each parse step returns a computed `float` directly (a "tree-walking" evaluator without building an explicit AST first).

## Possible Extensions

- Add support for variables (`x = 5`, then `x * 2`)
- Add functions (`sqrt()`, `sin()`, `abs()`)
- Add a history command in the REPL
