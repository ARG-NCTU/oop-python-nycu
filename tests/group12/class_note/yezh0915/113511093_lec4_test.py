import add_path
import mit_ocw_exercises.lec4_functions as lec4
import pytest


def test_is_even_with_return():
    assert lec4.is_even_with_return(2) == True
    assert lec4.is_even_with_return(3) == False
    assert lec4.is_even_with_return(0) == True
def test_bisection_cuberoot_approx():
    epsilon = 0.01
    assert lec4.abs(bisection_cuberoot_approx(27, epsilon) - 3) < epsilon
    assert lec4.abs(bisection_cuberoot_approx(64, epsilon) - 4) < epsilon
    assert lec4.abs(bisection_cuberoot_approx(1, epsilon) - 1) < epsilon
def test_function_object_f():
    func = f()
    assert lec4.func(2, 3) == 5
    assert lec4.func(10, 20) == 30
def test_scope_g():
    result = g(3)
    assert lec4.result == 4



if __name__ == "__main__":
    pytest.main()
