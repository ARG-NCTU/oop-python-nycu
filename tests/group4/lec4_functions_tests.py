import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import add_path
from src.mit_ocw_exercises.lec4_functions import is_even_with_return,is_even_without_return,is_even,bisection_cuberoot_approx

def test_is_even_with_return():
    assert is_even_with_return(4) == True
    assert is_even_with_return(7) == False
    assert is_even_with_return(0) == True
    assert is_even_with_return(1) == False

def test_is_even_without_return():
    assert is_even_without_return(4) is None
    assert is_even_without_return(7) is None
    assert is_even_without_return(0) is None
    assert is_even_without_return(1) is None    

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    assert is_even(1) == False

def test_bisection_cuberoot_approx():
    epsilon = 0.01
    assert abs(bisection_cuberoot_approx(27, epsilon) - 3) < epsilon
    assert abs(bisection_cuberoot_approx(8, epsilon) - 2) < epsilon
    assert abs(bisection_cuberoot_approx(1, epsilon) - 1) < epsilon
    assert abs(bisection_cuberoot_approx(0, epsilon) - 0) < epsilon

#still need to add more tests here