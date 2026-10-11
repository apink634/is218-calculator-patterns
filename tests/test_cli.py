import importlib

import pytest
from calculator.cli import build_calculation, main


def run_cli(monkeypatch, capsys, commands):
    # Fake the typing: each call to input() returns the next command in the list.
    answers = iter(commands)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))
    main()
    # Return everything that was printed, one line per item.
    return capsys.readouterr().out.splitlines()


# CLI success for all four commands.
def test_cli_success(monkeypatch, capsys):
    lines = run_cli(monkeypatch, capsys,
                    ["add 5 3", "subtract 5 3", "multiply 2.5 -2", "divide 6 3", "exit"])
    assert lines == ["8.0", "2.0", "-5.0", "2.0"]


def test_cli_unknown_command(monkeypatch, capsys):
    lines = run_cli(monkeypatch, capsys, ["power 2 3", "exit"])
    assert lines == ["Unknown command: power"]


def test_cli_wrong_operand_counts(monkeypatch, capsys):
    lines = run_cli(monkeypatch, capsys, ["add 5", "add 5 3 1", "exit"])
    assert lines == [
        "add needs exactly two numbers, e.g. add 5 3",
        "add needs exactly two numbers, e.g. add 5 3",
    ]


def test_cli_invalid_number(monkeypatch, capsys):
    lines = run_cli(monkeypatch, capsys, ["add five 3", "exit"])
    assert lines == ["Invalid number"]


def test_cli_division_by_zero(monkeypatch, capsys):
    lines = run_cli(monkeypatch, capsys, ["divide 5 0", "exit"])
    assert lines == ["Cannot divide by zero"]


# Continuing after errors: a valid command still works afterward,
# and the failed calculation is not saved in history.
def test_cli_continues_after_errors(monkeypatch, capsys):
    lines = run_cli(monkeypatch, capsys,
                    ["divide 5 0", "add five 3", "", "add 5 3", "history", "exit"])
    assert lines == ["Cannot divide by zero", "Invalid number", "8.0", "add 5.0 3.0 = 8.0"]


def test_cli_empty_history(monkeypatch, capsys):
    lines = run_cli(monkeypatch, capsys, ["history", "exit"])
    assert lines == ["History is empty"]


# Exit stops the loop: the command after it never runs.
def test_cli_exit(monkeypatch, capsys):
    lines = run_cli(monkeypatch, capsys, ["exit", "add 5 3"])
    assert lines == []


# EOF ends the program without an error.
def test_cli_eof(monkeypatch, capsys):
    def end_of_input(prompt=""):
        raise EOFError
    monkeypatch.setattr("builtins.input", end_of_input)
    main()  # Must return without an uncaught exception.
    assert capsys.readouterr().out == ""


# build_calculation's own unknown-command check (main() never reaches it).
def test_build_calculation_unknown_command():
    with pytest.raises(ValueError, match="Unknown command: power"):
        build_calculation("power", "2", "3")


# Covers the import line in __main__.py.
def test_main_module_imports_main():
    module = importlib.import_module("calculator.__main__")
    assert module.main is main