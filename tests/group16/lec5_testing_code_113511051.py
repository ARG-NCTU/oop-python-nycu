import add_path
import mit_ocw_exercises.lec5_tuples_lists as lec5
import pytest


# please write a test for quotient_and_remainder function
def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(10, 6) == (1, 4)
    assert lec5.quotient_and_remainder(10, 7) == (1, 3)
    assert lec5.quotient_and_remainder(10, 8) == (1, 2)
    assert lec5.quotient_and_remainder(10, 9) == (1, 1)
    assert lec5.quotient_and_remainder(10, 10) == (1, 0)
    assert lec5.quotient_and_remainder(10, 1) == (1, 9)

    try:
        lec5.quotient_and_remainder(10, 0)
    except ZeroDivisionError:
         print("ZeroDivisionError")
    assert lec5.quotient_and_remainder(10, 1) == (1, 9)


def test_sum_elem_method1():
    assert lec5.sum_elem_method1([1, 2, 3]) == 6
    assert lec5.sum_elem_method1([-1, 2, -3, 4]) == 2
    assert lec5.sum_elem_method1([15, 65, 23]) == 103
    assert lec5.sum_elem_method1([6]) == 6
    assert lec5.sum_elem_method1([]) == 0


def test_sum_elem_method2():
    assert lec5.sum_elem_method2([1, 2, 3, 4]) == 10
    assert lec5.sum_elem_method2([-1, -2, -3, -4]) == -10
    assert lec5.sum_elem_method2([13, 34, 0, 88, 88, 0, 9]) == 232
    assert lec5.sum_elem_method2([5]) == 5
    assert lec5.sum_elem_method2([]) == 0

def new_test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(25, 4) == (6, 1)
    assert lec5.quotient_and_remainder(24, 7) == (3, 3)
    assert lec5.quotient_and_remainder(12, 7) == (1, 5)
    assert lec5.quotient_and_remainder(10, 9) == (1, 1)
    assert lec5.quotient_and_remainder(18, 10) == (1, 8)

    try:
        lec5.quotient_and_remainder(13, 0)
    except ZeroDivisionError:
         print("ZeroDivisionError")
    assert lec5.quotient_and_remainder(24, 13) == (1, 11)