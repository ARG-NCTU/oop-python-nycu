from lec4 import is_even, is_even_with_return, bisection_cuberoot_approx

def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False

def test_is_even_with_return():
    assert is_even_with_return(4) is True
    assert is_even_with_return(5) is False

def test_bisection_cuberoot_approx():
    approx = bisection_cuberoot_approx(27, 0.01)
    assert abs(approx - 3.0) < 0.01