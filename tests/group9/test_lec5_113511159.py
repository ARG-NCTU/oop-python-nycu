import add_path
import mit_ocw_exercises.lec5_tuples_lists as lec5
import pytest

def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(20, 6) == (3, 2)
    assert lec5.quotient_and_remainder(5, 3) == (1, 2)
    assert lec5.quotient_and_remainder(0, 2) == (0, 0)
    with pytest.raises(ZeroDivisionError):
        lec5.quotient_and_remainder(10, 0)

def test_get_data():
    sample = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    assert lec5.get_data(sample) == (1, 7, 2)

def test_sum_elem_method1():
    assert lec5.sum_elem_method1([1, 2, 3]) == 6
    assert lec5.sum_elem_method1([]) == 0

def test_sum_elem_method2():
    assert lec5.sum_elem_method2([1, 2, 3]) == 6
    assert lec5.sum_elem_method2([]) == 0
