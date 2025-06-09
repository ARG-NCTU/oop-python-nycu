import lec_5.py as lec5
import pytest
def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(50, 4) == (12, 2)
    assert lec5.quotient_and_remainder(99, 10) == (9, 9)
    assert lec5.quotient_and_remainder(100, 25) == (4, 0)
    assert lec5.quotient_and_remainder(17, 5) == (3, 2)
    assert lec5.quotient_and_remainder(7, 7) == (1, 0)

    try:
        lec5.quotient_and_remainder(10, 0)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    assert lec5.quotient_and_remainder(15, 7) == (2, 1)


def test_sum_elem_method1():
    assert lec5.sum_elem_method1([10, 20, 30]) == 60
    assert lec5.sum_elem_method1([-10, 10, -5, 5]) == 0
    assert lec5.sum_elem_method1([100, 200, 300, 400]) == 1000
    assert lec5.sum_elem_method1([0, 0, 0]) == 0
    assert lec5.sum_elem_method1([999]) == 999
    assert lec5.sum_elem_method1([]) == 0
