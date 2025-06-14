import pytest
import lec4_functions as lec4
import math


def test_even():
    assert lec4.is_even_with_return(5) == False
    assert lec4.is_even_with_return(12) == True
    assert lec4.is_even_with_return(9) == False
    assert lec4.is_even_with_return(18) == True
    assert lec4.is_even_with_return(0) == True
    assert lec4.is_even_with_return(-10) == True     # negative even
    assert lec4.is_even_with_return(3.4) == False    # float check
    assert lec4.is_even_with_return(-6) == True      # check negative even
    assert lec4.is_even_with_return(7.2) == False    # check float


def test_cuberoot():
    # ε = 0.01 ；數值由 lec4.bisection_cuberoot_approx() 實際跑出的結果填入
    assert lec4.bisection_cuberoot_approx(20, 0.01)  == 2.71484375
    assert lec4.bisection_cuberoot_approx(30, 0.01) == 3.1072998046875
    assert lec4.bisection_cuberoot_approx(50, 0.01) == 3.684234619140625
    assert lec4.bisection_cuberoot_approx(250, 0.01) == 6.299614906311035
    assert lec4.bisection_cuberoot_approx(2,  0.01)  == 1.26171875
    assert lec4.bisection_cuberoot_approx(1,  0.01)  == 0.998046875
    assert lec4.bisection_cuberoot_approx(5,  0.01)  == 1.708984375


def f():
    def x(a, b):
        return a + b
    return x


def test_func_in_func():
    assert f()(2, 8) == 10
    assert f()(3, -3) == 0
    assert f()(0.25, 0.75) == 1.0
    # new combo
    assert f()(f()(1, 2), f()(3, 4)) == 10

