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

def test_is_even_with_return_even(capsys):
    # 偶數應回傳 True 並印出提示
    assert is_even_with_return(4) is True
    captured = capsys.readouterr()
    assert 'with return' in captured.out


def test_is_even_with_return_odd(capsys):
    # 奇數應回傳 False 並印出提示
    assert is_even_with_return(3) is False
    captured = capsys.readouterr()
    assert 'with return' in captured.out


def test_is_even_without_return(capsys):
    # 不帶 return 的函式應回傳 None 並印出提示
    result = is_even_without_return(4)
    assert result is None
    captured = capsys.readouterr()
    assert 'without return' in captured.out


def test_is_even():
    # 基本的偶數／奇數判斷
    assert is_even(2) is True
    assert is_even(3) is False


@pytest.mark.parametrize("x,epsilon,expected", [
    (8, 0.01, 2.0),
    (27, 1e-6, 3.0),
    (1, 1e-8, 1.0),
])
def test_bisection_cuberoot_approx(x, epsilon, expected):
    # 立方根近似測試：結果與預期誤差小於 epsilon
    result = bisection_cuberoot_approx(x, epsilon)
    assert abs(result - expected) < epsilon


def test_func_a(capsys):
    # func_a 只印出訊息，不回傳
    result = func_a()
    assert result is None
    captured = capsys.readouterr()
    assert 'inside func_a' in captured.out


def test_func_b(capsys):
    # func_b 印訊息並回傳參數
    result = func_b(5)
    assert result == 5
    captured = capsys.readouterr()
    assert 'inside func_b' in captured.out


def test_func_c(capsys):
    # func_c 接受一個可呼叫物件，印訊息後執行該物件並回傳結果
    def dummy():
        print('dummy called')
        return 'ok'
    result = func_c(dummy)
    assert result == 'ok'
    captured = capsys.readouterr()
    assert 'inside func_c' in captured.out
    assert 'dummy called' in captured.out


def test_f_factory():
    # f_factory 應回傳一個可加總的函式
    add = f_factory()
    assert callable(add)
    assert add(2, 3) == 5
