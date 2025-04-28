import pytest
import lec4_functions as lec4
import math

def test_even():
    assert lec4.is_even_with_return(7) == False
    assert lec4.is_even_with_return(6) == True
    assert lec4.is_even_with_return(0) == True
    assert lec4.is_even_with_return(-4) == True 

def test_cuberoot():
    assert lec4.bisection_cuberoot_approx(5,0.01) == 1.708984375
    assert lec4.bisection_cuberoot_approx(99,0.01) == 4.62608528137207
    assert lec4.bisection_cuberoot_approx(1,0.01) == 0.998046875
    assert lec4.bisection_cuberoot_approx(1.01,0.01) == 1.002109375


def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    print('in g(x): x = ', x)
    h(x)
    return x

def test_function_in_function():
    assert g(3) == 3

