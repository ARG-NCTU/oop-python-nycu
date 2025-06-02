import pytest
import lec4_functions as lec4
import math

def test_even():
    assert lec4.is_even_with_return(3) == False
    assert lec4.is_even_with_return(4) == True
    assert lec4.is_even_with_return(0) == True
    assert lec4.is_even_with_return(-2) == True #check for negative even numbers

def test_cuberoot():
    assert lec4.bisection_cuberoot_approx(10,0.01) == 2.154541015625
    assert lec4.bisection_cuberoot_approx(100,0.01) == 4.6417236328125
    assert lec4.bisection_cuberoot_approx(1,0.01) == 0.998046875
    assert lec4.bisection_cuberoot_approx(1.01,0.01) == 1.002109375

def f():
    def x(a, b):
        return a+b
    return x

def test_func_in_func():
    assert f()(1,5) == 6
    assert f()(1,-1) == 0
    assert f()(0.1,0.5) == 0.6
##
