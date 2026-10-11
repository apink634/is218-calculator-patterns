class Operations:
    @staticmethod
    def add(a: float, b: float) -> float:
        # This method uses only a and b. No object state is needed.
        return a + b

    def subtract(a: float, b: float) -> float:
        # This method uses only a and b. No object state is needed.
        return a - b
    def multiply(a: float, b: float) -> float:
        # This method uses only a and b. No object state is needed.
        return a * b
    def divide(a: float, b: float) -> float:
        # This method uses only a and b. No object state is needed.
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b