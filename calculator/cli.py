from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation

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