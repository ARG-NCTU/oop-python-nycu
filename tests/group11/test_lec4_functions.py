import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lec4_functions import (
    is_even_with_return, is_even_without_return, is_even,
    bisection_cuberoot_approx,
    func_a, func_b, func_c, f
)

def test_is_even_functions():
    """測試 is_even 系列函數"""
    assert is_even_with_return(4) is True
    assert is_even_with_return(3) is False
    
    # without return 應該總是返回 None (implicit return)
    assert is_even_without_return(4) is None
    assert is_even_without_return(3) is None
    
    # 簡化版
    assert is_even(4) is True
    assert is_even(3) is False

def test_bisection_cuberoot():
    """測試二分法求立方根"""
    # 27 的立方根是 3
    res = bisection_cuberoot_approx(27, 0.01)
    assert abs(res**3 - 27) < 0.01
    
    # 8 的立方根是 2
    res = bisection_cuberoot_approx(8, 0.001)
    assert abs(res**3 - 8) < 0.001

def test_functions_as_args():
    """測試函數作為參數"""
    # func_a 只是 print，返回 None
    assert func_a() is None
    
    # func_b 返回參數
    assert func_b(10) == 10
    
    # func_c 接受一個函數 z，並返回 z()
    # 傳入 func_a，func_a 返回 None，所以 func_c 返回 None
    assert func_c(func_a) is None

def test_returning_functions():
    """測試返回函數"""
    # f() 返回一個函數 x(a, b) -> a+b
    my_adder = f()
    assert callable(my_adder)
    assert my_adder(3, 4) == 7
