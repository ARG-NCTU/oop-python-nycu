from math_utils import subtract, divide

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(3, 3) == 0

def test_divide():
    assert divide(3, 2) == 1.5
    assert divide(2, 1) == 2


