from calculator.calculation import Calculation


class CalculateCommand:
    def __init__(self, calculation: Calculation, history: list[str]):
        # The command receives the calculation and the shared history list.
        self.calculation = calculation
        self.history = history

    def execute(self) -> float:
        # Run the calculation. If it fails (like dividing by zero),
        # the error stops this method here, so nothing is added to history.
        result = self.calculation.execute()

        # Only reached when the calculation succeeded.
        name = self.calculation.operation.__name__
        entry = f"{name} {self.calculation.a} {self.calculation.b} = {result}"
        self.history.append(entry)
        return result


class HistoryCommand:
    def __init__(self, history: list[str]):
        # Same shared history list that CalculateCommand writes to.
        self.history = history

    def execute(self) -> list[str]:
        # Return a copy so the caller can't change the stored history.
        return list(self.history)