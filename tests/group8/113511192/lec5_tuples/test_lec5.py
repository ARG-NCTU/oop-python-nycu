import add_path
import lec5 as lec5
import pytest


def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(100, 21) == (4, 16)
    assert lec5.quotient_and_remainder(100, 3) == (33, 1)
    assert lec5.quotient_and_remainder(20, 12) == (1, 8)
    assert lec5.quotient_and_remainder(20, 5) == (4, 0)
    assert lec5.quotient_and_remainder(5, 2) == (2, 1)
    assert lec5.quotient_and_remainder(0, 5) == (0, 0)
    
    try:
        lec5.quotient_and_remainder(5, 0)
    except ZeroDivisionError:
         print("ZeroDivisionError")

def test_get_data():
    t = ((1, "a"), (5, "b"), (2, "a"), (7, "c"))
    assert lec5.get_data(t) == (1, 7, 3)

    t = ((10, "apple"), (5, "apple"), (20, "banana"))
    assert lec5.get_data(t) == (5, 20, 2)


def test_sum_elem_method1():
    assert lec5.sum_elem_method1([]) == 0
    assert lec5.sum_elem_method1([100]) == 100
    assert lec5.sum_elem_method1([1, 2, 3, 4, 5]) == 15
    assert lec5.sum_elem_method1([-1, 2, -3, 4, -5]) == -3
    assert lec5.sum_elem_method1([-20, -19, -18]) == -57
    assert lec5.sum_elem_method1([0, 100, 0]) == 100


def test_sum_elem_method2():
    assert lec5.sum_elem_method2([]) == 0
    assert lec5.sum_elem_method2([100]) == 100
    assert lec5.sum_elem_method2([1, 2, 3, 4, 5]) == 15
    assert lec5.sum_elem_method2([-1, 2, -3, 4, -5]) == -3
    assert lec5.sum_elem_method2([-20, -19, -18]) == -57
    assert lec5.sum_elem_method2([0, 100, 0]) == 100

