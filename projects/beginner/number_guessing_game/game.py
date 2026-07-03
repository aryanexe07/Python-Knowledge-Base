"""Number Guessing Game — guess a secret number within a limited number
of attempts, with three difficulty levels and a running high-score log.

Run:
    python game.py
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from enum import Enum


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


DIFFICULTY_SETTINGS: dict[Difficulty, tuple[int, int]] = {
    # difficulty -> (range_max, max_attempts)
    Difficulty.EASY: (50, 10),
    Difficulty.MEDIUM: (100, 7),
    Difficulty.HARD: (200, 6),
}


@dataclass
class GameResult:
    won: bool
    attempts_used: int
    secret_number: int
    guesses: list[int] = field(default_factory=list)


def choose_difficulty() -> Difficulty:
    """Prompt the player to choose a difficulty level."""
    prompt = "Choose difficulty [easy / medium / hard] (default medium): "
    while True:
        choice = input(prompt).strip().lower() or "medium"
        try:
            return Difficulty(choice)
        except ValueError:
            print(f"'{choice}' isn't a valid option. Try again.")


def get_guess(range_max: int, attempts_left: int) -> int:
    """Request and validate a numeric guess from the player."""
    while True:
        raw = input(f"Guess a number (1-{range_max}) [{attempts_left} attempts left]: ").strip()
        if not raw.lstrip("-").isdigit():
            print("Please enter a whole number.")
            continue
        value = int(raw)
        if not 1 <= value <= range_max:
            print(f"Your guess must be between 1 and {range_max}.")
            continue
        return value


def play_round(difficulty: Difficulty) -> GameResult:
    """Play one round of the game at the chosen difficulty."""
    range_max, max_attempts = DIFFICULTY_SETTINGS[difficulty]
    secret = random.randint(1, range_max)
    guesses: list[int] = []

    for attempt in range(1, max_attempts + 1):
        guess = get_guess(range_max, max_attempts - attempt + 1)
        guesses.append(guess)

        if guess == secret:
            return GameResult(won=True, attempts_used=attempt, secret_number=secret, guesses=guesses)

        hint = "higher" if guess < secret else "lower"
        print(f"Too {'low' if hint == 'higher' else 'high'}! Try {hint}.")

    return GameResult(won=False, attempts_used=max_attempts, secret_number=secret, guesses=guesses)


def print_result(result: GameResult) -> None:
    """Display the player's result for the current round."""
    if result.won:
        print(f"\n🎉 Correct! The number was {result.secret_number}.")
        print(f"You got it in {result.attempts_used} attempt(s).")
    else:
        print(f"\n💀 Out of attempts! The number was {result.secret_number}.")
    print(f"Your guesses: {result.guesses}\n")


def main() -> None:
    """Run the main game loop and display best scores."""
    print("=== Number Guessing Game ===\n")
    best_scores: dict[Difficulty, int] = {}

    while True:
        difficulty = choose_difficulty()
        result = play_round(difficulty)
        print_result(result)

        if result.won:
            current_best = best_scores.get(difficulty)
            if current_best is None or result.attempts_used < current_best:
                best_scores[difficulty] = result.attempts_used
                print(f"New best score for {difficulty.value}: {result.attempts_used} attempts!\n")

        again = input("Play again? [y/N]: ").strip().lower()
        if again != "y":
            break

    if best_scores:
        print("\n=== Best Scores ===")
        for difficulty, score in best_scores.items():
            print(f"  {difficulty.value}: {score} attempts")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
