import add_path
import mit_ocw_exercises.lec5_tuples_lists as lec5
import pytest


def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(5, 3) == (1, 2)
    assert lec5.quotient_and_remainder(10, 2) == (5, 0)
    assert lec5.quotient_and_remainder(0, 5) == (0, 0)
def test_get_data():
    test_data = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    min_n, max_n, unique_strings = lec5.get_data(test_data)
    assert min_n == 1
    assert max_n == 7
    assert unique_strings == 2

    tswift_data = ((2014, "Katy"), (2014, "Harry"), (2012, "Jake"), (2010, "Taylor"), (2008, "Joe"))
    min_year, max_year, num_people = lec5.get_data(tswift_data)
    assert min_year == 2008
    assert max_year == 2014
    assert num_people == 5
def test_sum_elem_method1():
    assert lec5.sum_elem_method1([1, 2, 3, 4]) == 10
    assert lec5.sum_elem_method1([]) == 0
    assert lec5.sum_elem_method1([10, -10, 20]) == 20

def test_sum_elem_method2():
    assert lec5.sum_elem_method2([1, 2, 3, 4]) == 10
    assert lec5.sum_elem_method2([]) == 0
    assert lec5.sum_elem_method2([10, -10, 20]) == 20
def test_remove_dups():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    lec5.remove_dups(L1, L2)
    assert L1 == [3, 4]
    assert L2 == [1, 2, 5, 6]

def test_remove_dups_new():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    lec5.remove_dups_new(L1, L2)
    assert L1 == [3, 4]
    assert L2 == [1, 2, 5, 6]



