"""Tests for the numeric-based calculator's REPL functionality."""

import sys
from io import StringIO  # <-- Standard library imports first

from app.calculator import Calculator  # <-- Local imports last


def simulate_calculator(monkeypatch, inputs):
    """
    Helper function to simulate user input for the calculator REPL.

    Args:
        monkeypatch (pytest.MonkeyPatch): Pytest fixture to override input().
        inputs (list[str]): A list of strings to feed as user input.

    Returns:
        str: The captured output from the REPL session.
    """
    input_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_iter))

    captured_output = StringIO()
    sys.stdout = captured_output
    Calculator.run()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


def test_start_and_quit(monkeypatch):
    """Test that '7' quits the calculator."""
    output = simulate_calculator(monkeypatch, ["7"])
    assert "Calculator Menu" in output
    assert "Exiting calculator. Goodbye!" in output


def test_addition(monkeypatch):
    """Test that '1' performs addition."""
    output = simulate_calculator(monkeypatch, ["1", "3", "2", "7"])
    assert "The result is: 5.0" in output


def test_subtraction(monkeypatch):
    """Test that '2' performs subtraction."""
    output = simulate_calculator(monkeypatch, ["2", "10", "4", "7"])
    assert "The result is: 6.0" in output


def test_multiplication(monkeypatch):
    """Test that '3' performs multiplication."""
    output = simulate_calculator(monkeypatch, ["3", "2", "3", "7"])
    assert "The result is: 6.0" in output


def test_division_by_zero(monkeypatch):
    """Test that '4' with zero triggers zero-division error."""
    output = simulate_calculator(monkeypatch, ["4", "5", "0", "7"])
    assert "Cannot divide by zero." in output


def test_invalid_number_input(monkeypatch):
    """Test entering a non-numeric value triggers invalid number message."""
    output = simulate_calculator(monkeypatch, ["1", "abc", "2", "3", "7"])
    assert "Invalid number" in output


def test_history(monkeypatch):
    """Test that '5' shows the calculation history."""
    output = simulate_calculator(monkeypatch, ["1", "1", "1", "5", "7"])
    assert "1.0 addition 1.0 = 2.0" in output


def test_clear_history_via_repl(monkeypatch):
    """Test that '6' clears the history."""
    output = simulate_calculator(monkeypatch, ["6", "7"])
    assert "History has been cleared." in output


def test_clear_history_direct(capsys):
    """Test calling clear_history() directly."""
    Calculator.clear_history()
    captured = capsys.readouterr()
    assert "History has been cleared." in captured.out


def test_quit_during_number_input(monkeypatch):
    """Test typing 'quit' as the second number."""
    output = simulate_calculator(monkeypatch, ["1", "5", "quit"])
    assert "Exiting calculator. Goodbye!" in output


def test_invalid_command(monkeypatch):
    """Test an unrecognized command prints invalid choice."""
    output = simulate_calculator(monkeypatch, ["999", "7"])
    assert "Invalid choice" in output


def test_compute_divide_by_zero_direct():
    """Directly test compute() with zero divisor."""
    result = Calculator.compute("division", 5, 0)
    assert result is None


def test_stoptest_command(monkeypatch):
    """Test hidden '8' command for coverage final line."""
    output = simulate_calculator(monkeypatch, ["8"])
    assert "Testing coverage for final line." in output


def test_quit_as_first_number(monkeypatch):
    """Test typing 'quit' as first number."""
    output = simulate_calculator(monkeypatch, ["1", "quit"])
    assert "Exiting calculator. Goodbye!" in output


def test_empty_history(monkeypatch):
    """Test that '5' shows 'No calculations recorded.' when history is empty."""
    output = simulate_calculator(monkeypatch, ["5", "7"])
    assert "No calculations recorded." in output
