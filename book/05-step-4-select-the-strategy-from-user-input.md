# Step 4: Select the strategy from user input

A strategy is a way to do a job. Here, the operation functions are the strategies. The CLI selects one from a dictionary; the selected function does the arithmetic.

```
operations = {
    "add": Operations.add,
    "subtract": Operations.subtract,
    "multiply": Operations.multiply,
    "divide": Operations.divide,
}

# After checking the command and converting the two numbers:
operation = operations[command_name]
calculation = ArithmeticCalculation.create(a, b, operation)
```

Check that the command exists before looking it up. Convert operands with `float()` and catch invalid input. No separate strategy class is required.
---

[Back to the contents](../README.md) · [Start with forking](00-fork-and-submit.md)

Next: [Step 5: Let a command run the calculation](06-step-5-let-a-command-run-the-calculation.md)
