import pytest
from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation


def test_add():
    assert Operations.add(5, 3) == 8
    assert Operations.add(-5, 3) == -2                     # negative
    assert Operations.add(2.5, 1.5) == pytest.approx(4.0)  # decimal
    assert Operations.add(0, 0) == 0                       # zero

def test_subtract():
    assert Operations.subtract(5, 3) == 2
    assert Operations.subtract(-5, 3) == -8                       # negative
    assert Operations.subtract(5.5, 2.25) == pytest.approx(3.25)  # decimal
    assert Operations.subtract(0, 7) == -7                        # zero

def test_multiply():
    assert Operations.multiply(5, 3) == 15
    assert Operations.multiply(-2, -3) == 6                      # negative x negative
    assert Operations.multiply(2.5, 4) == pytest.approx(10.0)    # decimal
    assert Operations.multiply(7, 0) == 0                        # zero

def test_divide():
    assert Operations.divide(6, 3) == 2
    assert Operations.divide(-9, 3) == -3                        # negative
    assert Operations.divide(7.5, 2.5) == pytest.approx(3.0)     # decimal
    assert Operations.divide(0, 5) == 0                          # zero

def test_divide_by_zero():
    try:
        Operations.divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
    else:
        assert False, "Expected ValueError for division by zero"

def test_calculation_with_subtract():
    calculation = ArithmeticCalculation.create(5, 3, Operations.subtract)
    result = calculation.execute()
    assert result == 2

def test_calculation_with_multiply():
    calculation = ArithmeticCalculation.create(5, 3, Operations.multiply)
    result = calculation.execute()
    assert result == 15

def test_calculation_with_divide():
    calculation = ArithmeticCalculation.create(15, 3, Operations.divide)
    result = calculation.execute()
    assert result == 5