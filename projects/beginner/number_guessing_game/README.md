# Number Guessing Game

A terminal number-guessing game with three difficulty levels, input validation, high/low hints, and a running best-score tracker across rounds.

## Features

- Three difficulties (`easy` / `medium` / `hard`) with different ranges and attempt limits
- Robust input validation (rejects non-numbers and out-of-range guesses without spending an attempt)
- Higher/lower hints after each wrong guess
- Best-score tracking per difficulty across multiple rounds in one session
- Fully unit-testable game logic, decoupled from I/O via `unittest.mock`

## Requirements

No external dependencies — standard library only.

## Usage

```bash
python game.py
```

```
=== Number Guessing Game ===

Choose difficulty [easy / medium / hard] (default medium): easy
Guess a number (1-50) [10 attempts left]: 25
Too low! Try higher.
Guess a number (1-50) [9 attempts left]: 40
🎉 Correct! The number was 40.
You got it in 2 attempt(s).
```

## Running Tests

```bash
pytest test_game.py -v
```

Tests mock both `random.randint` and `input()` so game logic is verified deterministically without needing a live terminal.

## Project Structure

```
number_guessing_game/
├── README.md
├── game.py
├── test_game.py
└── screenshots/
```

## Screenshots

<!-- Add a terminal screenshot of a played round -->
`screenshots/gameplay.png`

## Design Notes

- `Difficulty` is an `Enum` rather than a raw string, so invalid values fail fast and IDEs autocomplete valid options.
- `play_round()` contains all game logic and returns a `GameResult` dataclass, cleanly separated from `main()`'s I/O/loop concerns — this is what makes it testable (see [Chapter 20: Testing](../../../docs/20_testing/README.md)).

## Possible Extensions

- Persist best scores to a JSON file between sessions
- Add a "computer guesses your number" reverse mode (binary search)
- Add a timer-based scoring bonus
