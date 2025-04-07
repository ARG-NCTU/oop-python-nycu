from lec5 import quotient_and_remainder, get_data, sum_elem_method1, sum_elem_method2

def test_quotient_and_remainder():
    assert quotient_and_remainder(5, 3) == (1, 2)

def test_get_data():
    data = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    assert get_data(data) == (1, 7, 2)

def test_sum():
    L = [1, 2, 3]
    assert sum_elem_method1(L) == 6
    assert sum_elem_method2(L) == 6

