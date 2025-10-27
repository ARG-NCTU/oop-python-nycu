import add_path
import lec5_tuples_lists as lec5 # type: ignore
import pytest
import random


def test_quotient_and_remainder():
    # fresh inputs / expected outputs
    assert lec5.quotient_and_remainder(37, 5) == (7, 2)
    assert lec5.quotient_and_remainder(41, 6) == (6, 5)
    assert lec5.quotient_and_remainder(42, 7) == (6, 0)
    assert lec5.quotient_and_remainder(99, 8) == (12, 3)
    assert lec5.quotient_and_remainder(100, 33) == (3, 1)
    for _ in range(1, 100):
        x,y = random.randint(1,1000), random.randint(1,100)
        assert lec5.quotient_and_remainder(x,y) == (x // y, x % y)
    with pytest.raises(ZeroDivisionError):
        lec5.quotient_and_remainder(10, 0)

def test_sum_elem_method1():
    assert lec5.sum_elem_method1([7]) == 7
    assert lec5.sum_elem_method1([]) == 0
    assert lec5.sum_elem_method1([3, -2, 5, -7, 9]) == 8
    assert lec5.sum_elem_method1([10, 20, 30, 40, 50]) == 150
    assert lec5.sum_elem_method1(list(range(1, 101))) == 5050  # 1..100


def test_sum_elem_method2():
    assert lec5.sum_elem_method2([7]) == 7
    assert lec5.sum_elem_method2([]) == 0
    assert lec5.sum_elem_method2([3, -2, 5, -7, 9]) == 8
    assert lec5.sum_elem_method2([10, 20, 30, 40, 50]) == 150
    assert lec5.sum_elem_method2(list(range(1, 101))) == 5050  # 1..100
