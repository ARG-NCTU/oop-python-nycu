import pytest
import math
from examples_lec4_113511070 import (
    is_even_with_return,
    is_even_without_return,
    is_even,
    bisection_cuberoot_approx,
    func_a,
    func_b,
    func_c,
    f,
    f_scope,
    g_scope,
)

def test_is_even_with_return_true(capsys):
    assert is_even_with_return(4) is True
    captured = capsys.readouterr()
    assert 'with return' in captured.out

def test_is_even_with_return_false():
    assert is_even_with_return(3) is False

def test_is_even_without_return(capsys):
    assert is_even_without_return(5) is None
    captured = capsys.readouterr()
    assert 'without return' in captured.out

@pytest.mark.parametrize("n,expected", [(0,True),(1,False),(10**6+1,False)])
def test_is_even(n, expected):
    assert is_even(n) is expected

def test_bisection_cuberoot_approx():
    approx = bisection_cuberoot_approx(27, 1e-6)
    assert math.isclose(approx, 3.0, rel_tol=1e-4)

def test_func_b_and_c(capsys):
    ret = func_b(7)
    assert ret == 7
    assert func_c(func_a) is None
    out = capsys.readouterr().out
    assert 'inside func_b' in out
    assert 'inside func_c' in out

def test_f_returns_callable():
    fn = f()
    assert callable(fn)
    assert fn(2,3) == 5

def test_f_scope_and_g_scope(capsys):
    val = f_scope(5)
    assert val == 6
    out1 = capsys.readouterr().out
    assert 'in f(x): x =' in out1

    val2 = g_scope(5)
    assert val2 == 6
    out2 = capsys.readouterr().out
    assert 'in g(x): x =' in out2
    assert 'in h(x): x =' in out2
