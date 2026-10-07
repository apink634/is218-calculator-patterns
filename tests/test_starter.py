"""These tests cover only the starter. Add tests for every feature you build."""
import pytest
from calculator.operations import Operations
from calculator.calculation import Calculation, ArithmeticCalculation

@pytest.mark.parametrize("a,b,expected", [(5, 3, 8), (-5, 3, -2), (0, 0, 0), (1.5, 2.25, 3.75)])
def test_add(a, b, expected):
    assert Operations.add(a, b) == pytest.approx(expected)

def test_factory_stores_values_and_operation():
    calculation = ArithmeticCalculation.create(5, 3, Operations.add)
    assert isinstance(calculation, Calculation)
    assert calculation.a == 5
    assert calculation.b == 3
    assert calculation.operation is Operations.add
    assert calculation.execute() == 8

def test_operation_can_be_replaced():
    calculation = ArithmeticCalculation.create(5, 3, lambda a, b: a * b)
    assert calculation.execute() == 15

def test_abstract_calculation_cannot_be_created():
    with pytest.raises(TypeError):
        Calculation.create(5, 3, Operations.add)
