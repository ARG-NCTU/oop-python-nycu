import pytest
from src.mit_ocw_exercises.lec4_functions import (
    is_even_with_return,
    bisection_cuberoot_approx,
    f,
    g
)

def test_is_even_with_return():
    assert is_even_with_return(2) == True
    assert is_even_with_return(3) == False
    assert is_even_with_return(0) == True
def test_bisection_cuberoot_approx():
    epsilon = 0.01
    assert abs(bisection_cuberoot_approx(27, epsilon) - 3) < epsilon
    assert abs(bisection_cuberoot_approx(64, epsilon) - 4) < epsilon
    assert abs(bisection_cuberoot_approx(1, epsilon) - 1) < epsilon


if __name__ == "__main__":
    pytest.main()
