from math_utils import subtract, divide
def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(-1, 1) == -2
def test_divide():
    assert divide(2, 0) == None
    assert divide(20, 10) == 2
