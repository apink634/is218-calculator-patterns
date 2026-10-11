from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand


def test_calculate_command_returns_result_and_records_history():
    history = []
    calculation = ArithmeticCalculation.create(5, 3, Operations.add)
    command = CalculateCommand(calculation, history)
    result = command.execute()
    assert result == 8
    assert history == ["add 5 3 = 8"]


def test_failed_calculation_adds_no_history():
    history = []
    calculation = ArithmeticCalculation.create(5, 0, Operations.divide)
    command = CalculateCommand(calculation, history)
    try:
        command.execute()
    except ValueError:
        pass
    assert history == []


def test_history_command_empty():
    history = []
    command = HistoryCommand(history)
    assert command.execute() == []


def test_history_command_returns_copy():
    history = ["add 5 3 = 8"]
    copy = HistoryCommand(history).execute()
    copy.append("changed")
    assert history == ["add 5 3 = 8"]