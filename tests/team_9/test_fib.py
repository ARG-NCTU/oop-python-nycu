import add_path
import mit_ocw_data_science.fib_9 as lc
import pytest

def test_fib():
    a=lc.Fibo()
    assert a.cal(10) == 55
