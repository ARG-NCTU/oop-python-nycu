import add_path  # if your repo requires this to set up sys.path
import mit_ocw_exercises.lec5_tuples_lists as lec5
import pytest

def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(10, 3) == (3, 1)
    assert lec5.quotient_and_remainder(17, 5) == (3, 2)
    assert lec5.quotient_and_remainder(8, 4) == (2, 0)
    assert lec5.quotient_and_remainder(22, 7) == (3, 1)

def test_get_data():
    data1 = ((5, "apple"), (3, "banana"), (9, "apple"), (7, "cherry"))
    assert lec5.get_data(data1) == (3, 9, 3)
    data2 = ((100, "x"), (200, "y"), (300, "x"), (50, "z"))
    assert lec5.get_data(data2) == (50, 300, 3)
    data3 = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    assert lec5.get_data(data3) == (1, 7, 2)

def test_sum_elem_methods():
    assert lec5.sum_elem_method1([7, 8, 9]) == 24
    assert lec5.sum_elem_method1([4, 5, 6, 7]) == 22
    assert lec5.sum_elem_method2([10, 20]) == 30
    assert lec5.sum_elem_method2([1, 2, 3, 4, 5]) == 15
    assert lec5.sum_elem_method1([]) == 0
    assert lec5.sum_elem_method2([]) == 0

def test_remove_dups():
    L1 = [10, 20, 30, 40]
    L2 = [20, 50, 60]
    lec5.remove_dups(L1, L2)
    assert L1 == [10, 30, 40]

    L1 = [5, 6, 7, 8, 9]
    L2 = [6, 8, 10]
    lec5.remove_dups(L1, L2)
    assert L1 == [5, 7, 9]

def test_remove_dups_new():
    L1 = [21, 22, 23, 24]
    L2 = [22, 25]
    lec5.remove_dups_new(L1, L2)
    assert L1 == [21, 23, 24]

    L1 = [1, 3, 5, 7, 9]
    L2 = [3, 7]
    lec5.remove_dups_new(L1, L2)
    assert L1 == [1, 5, 9]

def test_quotient_and_remainder_zero_division():
    with pytest.raises(ZeroDivisionError):
        lec5.quotient_and_remainder(5, 0)
