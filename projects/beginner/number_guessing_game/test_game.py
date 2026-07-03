"""Tests for game.py — run with: pytest test_game.py

Uses monkeypatching to simulate user input so the game logic can be
tested without a real terminal.
"""

from unittest.mock import patch

from game import Difficulty, DIFFICULTY_SETTINGS, play_round


def test_win_on_correct_guess(monkeypatch):
    with patch("random.randint", return_value=42):
        inputs = iter(["42"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = play_round(Difficulty.EASY)
    assert result.won is True
    assert result.attempts_used == 1
    assert result.secret_number == 42


def test_loss_after_max_attempts(monkeypatch):
    _, max_attempts = DIFFICULTY_SETTINGS[Difficulty.HARD]
    with patch("random.randint", return_value=1):
        # Always guess something wrong (2), exhausting all attempts.
        inputs = iter(["2"] * max_attempts)
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = play_round(Difficulty.HARD)
    assert result.won is False
    assert result.attempts_used == max_attempts
    assert len(result.guesses) == max_attempts


def test_invalid_input_is_rejected_then_recovers(monkeypatch):
    with patch("random.randint", return_value=10):
        # "abc" invalid, "999" out of range, then correct guess "10"
        inputs = iter(["abc", "999", "10"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = play_round(Difficulty.EASY)
    assert result.won is True
    assert result.guesses == [10]  # invalid attempts don't count as guesses
