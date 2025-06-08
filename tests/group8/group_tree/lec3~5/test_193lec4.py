import pytest
from lec4 import (
    is_even_with_return,
    is_even_without_return,
    is_even,
    bisection_cuberoot_approx,
    func_a,
    func_b,
    func_c,
    f,
    g,
)

def test_is_even_with_return():
    assert is_even_with_return(2) == True
    assert is_even_with_return(3) == False

def test_is_even_without_return(capsys):
    is_even_without_return(2)
    captured = capsys.readouterr()
    assert "without return" in captured.out

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False

def test_bisection_cuberoot_approx():
    assert pytest.approx(bisection_cuberoot_approx(27, 0.01), 0.01) == 3
    assert pytest.approx(bisection_cuberoot_approx(64, 0.01), 0.01) == 4

def test_func_a(capsys):
    func_a()
    captured = capsys.readouterr()
    assert "inside func_a" in captured.out

def test_func_b():
    assert func_b(5) == 5

def test_func_c(capsys):
    func_c(func_a)
    captured = capsys.readouterr()
    assert "inside func_a" in captured.out
    assert "inside func_c" in captured.out

def test_f():
    func = f(6)
    assert func == 7

