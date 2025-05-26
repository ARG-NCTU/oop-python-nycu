import pytest
from dua_lec4 import (
    is_even_with_return,
    is_even_without_return,
    is_even,
    bisection_cuberoot_approx,
    func_a,
    func_b,
    func_c,
    f_factory,
)

def test_is_even_with_return(capsys):
    assert is_even_with_return(2) is True
    captured = capsys.readouterr()
    assert 'with return' in captured.out
    assert is_even_with_return(3) is False

def test_is_even_without_return(capsys):
    result = is_even_without_return(2)
    captured = capsys.readouterr()
    assert 'without return' in captured.out
    assert result is None

def test_is_even():
    assert is_even(0) is True
    assert is_even(1) is False
    assert is_even(100) is True
    assert is_even(101) is False

def test_bisection_cuberoot_approx():
    for x in [0, 1, 8, 27, 64]:
        approx = bisection_cuberoot_approx(x, 0.0001)
        expected = x ** (1/3) if x > 0 else 0.0
        assert abs(approx - expected) < 0.001

def test_func_b_and_c(capsys):
    assert func_b(5) == 5
    captured = capsys.readouterr()
    assert 'inside func_b' in captured.out
    result = func_c(func_a)
    captured = capsys.readouterr()
    assert 'inside func_c' in captured.out
    assert 'inside func_a' in captured.out
    assert result is None

def test_factory():
    f = f_factory()
    assert callable(f)
    assert f(3, 4) == 7

