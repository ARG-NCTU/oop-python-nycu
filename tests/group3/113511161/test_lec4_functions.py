import add_path
import mit_ocw_exercises.lec4_functions as lec4
import pytest
import random
def test_is_even_with_return():
    assert lec4.is_even_with_return(2) == True
    assert lec4.is_even_with_return(3) == False
    assert lec4.is_even_with_return(0) == True
    assert lec4.is_even_with_return(-2) == True
    assert lec4.is_even_with_return(-3) == False
    assert lec4.is_even_with_return(100) == True
    assert lec4.is_even_with_return(101) == False

def test_is_even():
    assert lec4.is_even(2) == True
    assert lec4.is_even(3) == False

def test_bisection_cuberoot_approx():
    for i in range(10):
        x=random.randint(1, 100)
        epsilon=random.uniform(0.1, 0.5)
        assert lec4.bisection_cuberoot_approx(x, epsilon)- x**(1/3) <= epsilon

def test_f():
    assert lec4.f(2) == 3
    assert lec4.f(3) == 4
    assert lec4.f(4) == 5
def test_g():
    assert lec4.g(2) == 3
    assert lec4.g(3) == 4
    assert lec4.g(4) == 5