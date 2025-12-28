import pytest
import add_path
import lec6_recursion_dictionaries as lec6 # type: ignore
import time

def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) == 3
    assert lec6.fib(4) == 5
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13
    assert lec6.fib(7) == 21
    assert lec6.fib(8) == 34
    assert lec6.fib(9) == 55
    assert lec6.fib(10) == 89

def test_fib_efficient():
    d = {1: 1, 2: 2}
    assert lec6.fib_efficient(5, d) == 8
    assert lec6.fib_efficient(6, d) == 13
    assert d[6] == 13

def test_whichIsEfficient():
    d = {1: 1, 2: 2}
    n = 30
    t1 = time.time()
    lec6.fib_efficient(n, d)
    t2 = time.time()
    lec6.fib(n)
    t3 = time.time()
    assert (t2 - t1) < (t3 - t2)