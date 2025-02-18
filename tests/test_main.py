import pytest
from main import calculation, cli_mode
import sys


@pytest.mark.parametrize("a_string, b_string, operation_string, expected_output", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")
])
def test_calculation(a_string, b_string, operation_string, expected_output, capsys):
    """
    Tests the calculation function with different input values and operations.
    Captures printed output and compares it with expected results.
    """
    calculation(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output


def test_cli_mode_with_repl(monkeypatch, capsys):
    """
    Simulate `python main.py` (no arguments) to trigger REPL mode.
    Since REPL expects infinite user input, we simulate a simple session.
    """
    inputs = iter(["1", "5", "3", "7"])  # Simulate choosing addition and quitting
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(sys, "argv", ["main.py"])

    cli_mode()

    captured = capsys.readouterr()
    assert "Starting REPL mode" in captured.out
    assert "Calculator Menu" in captured.out
    assert "The result is: 8.0" in captured.out
    assert "Goodbye!" in captured.out



def test_cli_mode_with_invalid_args(capsys, monkeypatch):
    """
    Simulate `python main.py 1 2` (invalid number of args) to trigger usage error.
    """
    monkeypatch.setattr(sys, "argv", ["main.py", "1", "2"])
    with pytest.raises(SystemExit) as excinfo:
        cli_mode()
    captured = capsys.readouterr()
    assert "Usage: python main.py <num1> <num2> <operation>" in captured.out
    assert excinfo.value.code == 1


def test_cli_mode_with_valid_args(capsys, monkeypatch):
    """
    Simulate `python main.py 5 3 add` (valid args) to trigger calculation.
    """
    monkeypatch.setattr(sys, "argv", ["main.py", "5", "3", "add"])
    cli_mode()
    captured = capsys.readouterr()
    assert "The result of 5 add 3 is equal to 8" in captured.out
