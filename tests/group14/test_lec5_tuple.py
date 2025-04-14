import add_path
import mit_ocw_exercises.lec5_tuples_lists as lec5
import pytest

def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(20, 5) == (4, 0)
    assert lec5.quotient_and_remainder(10, 3) == (3, 1)
    assert lec5.quotient_and_remainder(7, 4) == (1, 3)

def test_get_data():
    test = ((3,"c"),(5, "g"),
			(2,"t"),(7,"k"))
    assert lec5.get_data(test) == (2, 7, 4)

def test_sum_elem_method1():
    assert lec5.sum_elem_method1( (1, 2, 3, 4, 5) ) == 15
    assert lec5.sum_elem_method1([3, 5, 6, 7, 8]) == 29

def test_sum_elem_method2():
    assert lec5.sum_elem_method2( (1, 2, 3, 4, 5) ) == 15
    assert lec5.sum_elem_method2([3, 5, 6, 7, 8]) == 29
    




