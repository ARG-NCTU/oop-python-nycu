import math
import pytest
from lec4 import is_even_with_return, is_even, bisection_cuberoot_approx, f

def test_is_even_with_return():
    assert is_even_with_return(2) is True
    assert is_even_with_return(3) is False
    assert is_even_with_return(0) is True
    assert is_even_with_return(-4) is True

def test_is_even():
    assert is_even(10)
    assert not is_even(11)
    assert is_even(0)
    assert is_even(-2)

def test_bisection_cuberoot_approx():
    result = bisection_cuberoot_approx(27, 0.01)
    assert math.isclose(result, 3.0, rel_tol=1e-2)

    result = bisection_cuberoot_approx(64, 0.001)
    assert math.isclose(result, 4.0, rel_tol=1e-3)

    result = bisection_cuberoot_approx(125, 0.0001)
    assert math.isclose(result, 5.0, rel_tol=1e-4)

from lec4 import f

def test_returning_function_objects():
    result = f(4)
    assert result == 5  # since f(4) returns 5
