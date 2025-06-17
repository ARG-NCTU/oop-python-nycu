import pytest

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def test_fib():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 3
    assert fib(4) == 5
    assert fib(5) == 8
    assert fib(6) == 13
    assert fib(7) == 21
    assert fib(8) == 34
    assert fib(9) == 55
    assert fib(10) == 89
    assert fib(11) == 144
    assert fib(12) == 233
    assert fib(13) == 377
    assert fib(14) == 610
    assert fib(15) == 987