from factory import *

def test_addition():
    add = factory.getOperator('+')
    result = add.operate(2,3)
    assert result == 5

def test_subtraction():
    subtract = factory.getOperator('-')
    result = subtract.operate(3,2)
    assert result == 1

def test_multiplication():
    multiply = factory.getOperator('*')
    result = multiply.operate(2,3)
    assert result == 6

def test_division():
    divide = factory.getOperator('/')
    result = divide.operate(3,2)
    assert result == 1.5

