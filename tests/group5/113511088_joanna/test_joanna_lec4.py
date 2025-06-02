from lec4_final import *

def test_is_even_with_return(capsys):
    assert is_even_with_return(4) == True
    assert is_even_with_return(3) == False

def test_is_even_without_return(capsys):
    is_even_without_return(3)
    captured = capsys.readouterr()
    assert "without return" in captured.out
    assert is_even_without_return(3) is None

def test_is_even():
    assert is_even(2)
    assert not is_even(5)

def test_bisection_cuberoot_approx():
    result = bisection_cuberoot_approx(27, 0.01)
    assert abs(result - 3.0) < 0.01

def test_func_call_chain():
    assert func_a() == "inside func_a"
    assert func_b(5) == 5
    assert func_c(func_a) == "inside func_a"

def test_function_returning_function():
    func = f_returning_function()
    assert func(3, 4) == 7

def test_scope_demo_f():
    assert scope_demo_f(5) == 2  # x starts at 1 and adds 1

def test_scope_demo_g():
    result = scope_demo_g(5, 10)
    assert result == (10, 11)

def test_nested_scope():
    assert nested_scope_g(3) == 4

def test_complicated_scope():
    assert complicated_scope_f(3) == 4
    assert complicated_scope_g(3) == 5
