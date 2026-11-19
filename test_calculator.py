"""Module with tests"""
import pytest
from calculator import Calculator

def test_1():
    """Test for 0,0 (no division)"""
    mycalc  = Calculator(0, 0)
    assert mycalc.add() == 0
    assert mycalc.subtract() == 0
    assert mycalc.multiply() == 0

def test_2():
    """Test for integers"""
    mycalc  = Calculator(9, 3)
    assert mycalc.add() == 12
    assert mycalc.subtract() == 6
    assert mycalc.multiply() == 27
    assert mycalc.divide() == 3

def test_3():
    """Test for floats"""
    mycalc  = Calculator(3.3333, 2.2222)
    assert mycalc.add() == 5.5555
    assert mycalc.subtract() == 1.1111
    assert mycalc.multiply() == pytest.approx(7.40725926)
    assert mycalc.divide() == pytest.approx(1.5)

def test_zero_division():
    """Test for dividing by 0"""
    mycalc = Calculator(1, 0)
    with pytest.raises(ValueError):
        mycalc.divide()
        
