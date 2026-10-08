from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation

calculation = ArithmeticCalculation.create(5, 3, Operations.add)
print(calculation.execute())  # 8

from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation

operations = {
    "add": Operations.add,
    "subtract": Operations.subtract,
    "multiply": Operations.multiply,
    "divide": Operations.divide,
}

# After checking the command and converting the two numbers:
operation = operations[command_name]
calculation = ArithmeticCalculation.create(a, b, operation)