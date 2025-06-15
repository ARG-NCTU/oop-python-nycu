import add_path
import mit_ocw_exercises.lec4_functions as lec4_functions
import pytest


def test_is_even_with_return():
    assert lec4_functions.is_even_with_return(2) is True
    assert lec4_functions.is_even_with_return(3) is False
    assert lec4_functions.is_even_with_return(0) is True

def test_is_even_without_return(capsys):
    lec4_functions.is_even_without_return(2)
    captured = capsys.readouterr()
    assert "without return" in captured.out

    lec4_functions.is_even_without_return(3)
    captured = capsys.readouterr()
    assert "without return" in captured.out

def test_is_even():
    assert lec4_functions.is_even(4) is True
    assert lec4_functions.is_even(7) is False

@pytest.mark.parametrize("x", [1, 8, 27, 1000])
def test_bisection_cuberoot_approx(x):
    epsilon = 0.01
    approx = lec4_functions.bisection_cuberoot_approx(x, epsilon)
    assert math.isclose(approx ** 3, x, abs_tol=epsilon)

def test_f_returns_function():
    func = lec4_functions.f()
    assert callable(func)
    assert func(3, 4) == 7
    assert func(-2, 5) == 3
