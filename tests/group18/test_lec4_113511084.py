import os
import sys
import pytest

sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../src'))

import mit_ocw_exercises.lec4_functions as lec4

@pytest.mark.parametrize("i, expected", [
    (0, True),
    (2, True),
    (3, False),
    (100, True),
    (101, False)
])
def test_is_even_with_return(i, expected):
    assert lec4.is_even_with_return(i) == expected

@pytest.mark.parametrize("i, expected", [
    (0, True),
    (1, False),
    (10, True),
    (99, False)
])
def test_is_even(i, expected):
    assert lec4.is_even(i) == expected

def function_returning_adder():
    def x(a, b):
        return a + b
    return x

def test_function_returning_function():
    adder = function_returning_adder()
    assert adder(3, 4) == 7
    assert adder(-1, 1) == 0
    assert callable(adder)
