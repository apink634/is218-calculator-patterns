# My calculator submission

A calculator that supports add, subtract, multiply, and divide, keeps a history of successful calculations, and handles bad input without crashing

## Setup, run, and test

Setup (Windows PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Run the calculator:
python -m calculator
Run the tests with coverage:
python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100

## Example conversation
> add 5 3
8.0
> multiply 2.5 -2
-5.0
> divide 5 0
Cannot divide by zero
> power 2 3
Unknown command: power
> add 5
add needs exactly two numbers, e.g. add 5 3
> history
add 5.0 3.0 = 8.0
multiply 2.5 -2.0 = -5.0
> exit

## Static, class, and instance methods

Static methods: Operations.add, subtract, multiply, and divide in operations.py. They only use the two numbers passed in, so they don't need self or cls.
 
Class method: Calculation.create() in calculation.py. It receives cls, the class it was called on, and uses it to build a new object of that class.
 
Instance methods: ArithmeticCalculation.execute() uses the object's own stored self.a, self.b, and self.operation. CalculateCommand.execute() and HistoryCommand.execute() are also instance methods that use their stored calculation and history list.

## Factory, Command, and Strategy


Tracing add 5 3:
 
1. main() in cli.py reads the input and splits it into ["add", "5", "3"]. It checks that add is a known command and that there are two numbers.
2. build_calculation() converts "5" and "3" to floats.
3. Strategy: it looks up operations["add"] in the dictionary, which gives the Operations.add function. Each operation function is a strategy for doing the math.
4. Factory: it calls ArithmeticCalculation.create(5.0, 3.0, Operations.add), which builds the calculation object.
5. Command: main() wraps the calculation in CalculateCommand(calculation, history) and calls execute(). The command runs the calculation, gets 8.0, adds "add 5.0 3.0 = 8.0" to history, and returns the result.
6. main() prints 8.0.

## OOP


Encapsulation: A calculation keeps its own numbers and operation together (self.a, self.b, self.operation) along with the execute() method that uses them. HistoryCommand.execute() returns a copy of the history list, so code that receives it can't change the stored history.
 
Abstraction: Calculation is an abstract class that promises every calculation will have an execute() method, without saying how. It can't be created directly.
 
Inheritance: ArithmeticCalculation inherits from Calculation, so it reuses __init__ and create() without rewriting them. It only adds its own execute().
 
Polymorphism: CalculateCommand just calls self.calculation.execute(). It doesn't care which Calculation subclass it was given, as long as that class follows the execute() contract.
 
Composition: CalculateCommand is built from other objects: it holds a calculation and a history list. A calculation in turn holds an operation function.

## SOLID

Single responsibility: Each part has one job. Operations does the math, ArithmeticCalculation stores and runs one calculation, the commands handle running and history, and cli.py handles input and printing.
 
Open/closed: To add a new operation like power, I would add a power static method to Operations and add "power": Operations.power to the dictionary in cli.py. I would not need to change ArithmeticCalculation.execute() or CalculateCommand, because they just run whatever operation they're given. That's also why adding subtract, multiply, and divide after addition didn't require changing execute().
 
Liskov substitution: Any subclass of Calculation can replace ArithmeticCalculation as long as its execute() returns a number or raises a ValueError. CalculateCommand would work with it unchanged.
 
Interface segregation: Calculation only requires one method, execute(), instead of many unrelated ones.
 
Dependency inversion: CalculateCommand receives a Calculation instead of creating one, and a calculation receives its operation function instead of having addition hard-coded inside it.
 

## Tests and GitHub Actions

All tests pass with 100% line coverage, both locally and on GitHub.
 
Successful Actions run: https://github.com/apink634/is218-calculator-patterns/actions/runs/38151755812
 

## Coverage exclusions

Calculation.execute() in calculation.py
if __name__ == "__main__": in __main__.py

both skipped lines are just a placeholder and a starter switch