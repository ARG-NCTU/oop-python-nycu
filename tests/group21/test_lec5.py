import pytest
import lec5
import add_path
def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(5, 3) == (1, 2)
    assert lec5.quotient_and_remainder(10, 2) == (5, 0)
    assert lec5.quotient_and_remainder(7, 7) == (1, 0)

def test_get_data():
    data = ((1,"a"),(2, "b"), (1,"a"),(7,"b"))
    assert lec5.get_data(data) == (1, 7, 2)

    tswift = ((2014,"Katy"), (2014, "Harry"), (2012,"Jake"), (2010,"Taylor"), (2008,"Joe"))
    assert lec5.get_data(tswift) == (2008, 2014, 5)

def test_sum_elem_method1():
    assert lec5.sum_elem_method1([1,2,3,4]) == 10
    assert lec5.sum_elem_method1([]) == 0
    assert lec5.sum_elem_method1([-1, -2, -3]) == -6

def test_sum_elem_method2():
    assert lec5.sum_elem_method2([1,2,3,4]) == 10
    assert lec5.sum_elem_method2([]) == 0
    assert lec5.sum_elem_method2([-1, -2, -3]) == -6

def test_remove_dups():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    lec5.remove_dups(L1, L2)

def test_remove_dups_new():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    lec5.remove_dups_new(L1, L2)
    assert L1 == [3, 4]
    assert L2 == [1, 2, 5, 6]

