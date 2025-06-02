import pytest

def quotient_and_remainder(x, y):
    """
    Function that returns the quotient and remainder of two numbers
    x: int, y: int returns: tuple (quotient, remainder)

    """
    q = x // y
    r = x % y
    return (q, r)
    
(quot, rem) = quotient_and_remainder(5,3)
print(quot)
print(rem)

def test_quotient_and_remainder():
    assert quotient_and_remainder(5, 3) == (1, 2)
    assert quotient_and_remainder(10, 2) == (5, 0)
    assert quotient_and_remainder(7, 4) == (1, 3)
    assert quotient_and_remainder(9, 3) == (3, 0)
    assert quotient_and_remainder(8, 5) == (1, 3)
    assert quotient_and_remainder(0, 1) == (0, 0)
