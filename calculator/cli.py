from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation

from calculator.commands import CalculateCommand, HistoryCommand

operations = {
    "add": Operations.add,
    "subtract": Operations.subtract,
    "multiply": Operations.multiply,
    "divide": Operations.divide,
}

def build_calculation(command_name, first, second):
    # Check that the command exists before looking it up.
    if command_name not in operations:
        raise ValueError(f"Unknown command: {command_name}")
    try:
        a = float(first)
        b = float(second)
    except ValueError:
        raise ValueError("Invalid number") from None

    # After checking the command and converting the two numbers:
    operation = operations[command_name]
    calculation = ArithmeticCalculation.create(a, b, operation)
    return calculation

def main():
    history = []
    # Create the operation dictionary here.
    # Already done: the `operations` dictionary at the top of this file (Step 4).
    while True:
        try:
            words = input("> ").split()
        except EOFError:
            break
        # Handle blank input, exit, and history.
        if not words:
            continue
        command_name = words[0]
        if command_name == "exit":
            break
        if command_name == "history":
            entries = HistoryCommand(history).execute()
            if entries:
                for entry in entries:
                    print(entry)
            else:
                print("History is empty")
            continue
        # Check the operation and operand count.
        if command_name not in operations:
            print(f"Unknown command: {command_name}")
            continue
        if len(words) != 3:
            print(f"{command_name} needs exactly two numbers, e.g. {command_name} 5 3")
            continue
        # Convert the numbers, select the strategy, and build the pieces.
        # For "add 5 3" the path is: read input -> choose Operations.add ->
        # create a calculation -> create and execute a command -> print the answer.
        try:
            calculation = build_calculation(command_name, words[1], words[2])
            command = CalculateCommand(calculation, history)
            # Execute the command and show its result or a helpful error.
            print(command.execute())
        except ValueError as error:
            print(error)