import add_path
import mit_ocw_exercises.lec5_tuples_lists as lec5
import pytest

# please write a test for quotient_and_remainder function
def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(20, 6) == (3, 2)
    assert lec5.quotient_and_remainder(20, 7) == (2, 6)
    assert lec5.quotient_and_remainder(20, 8) == (2, 4)
    assert lec5.quotient_and_remainder(20, 9) == (2, 2)
    assert lec5.quotient_and_remainder(20, 10) == (2, 0)


def test_sum_elem_method1():
    assert sum_elem_method1([1, 2, 3, 4]) == 10
    assert sum_elem_method1([-1, -2, -3, -4]) == -10
    assert sum_elem_method1([13, 34, 0, 88, 88, 0, 9]) == 232
    assert sum_elem_method1([5]) == 5
    assert sum_elem_method1([]) == 0


def test_sum_elem_method2():
    assert sum_elem_method2([1, 2, 3, 4]) == 10
    assert sum_elem_method2([-1, -2, -3, -4]) == -10
    assert sum_elem_method2([13, 34, 0, 88, 88, 0, 9]) == 232
    assert sum_elem_method2([5]) == 5
    assert sum_elem_method2([]) == 0

