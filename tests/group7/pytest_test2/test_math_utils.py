from math_utils import add, multiply
from math_utils2 import subtract, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 10) == 0

def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(10, 5) == 5

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) == None
