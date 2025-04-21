from lec5 import *

def test_quotient_and_remainder():
    assert quotient_and_remainder(5, 3) == (1, 2)
    assert quotient_and_remainder(10, 2) == (5, 0)

def test_get_data():
    test = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    assert get_data(test) == (1, 7, 2)

    tswift = ((2014, "Katy"), (2014, "Harry"), (2012, "Jake"),
              (2010, "Taylor"), (2008, "Joe"))
    assert get_data(tswift) == (2008, 2014, 5)

def test_sum_elem_methods():
    L = [1, 2, 3, 4]
    assert sum_elem_method1(L) == 10
    assert sum_elem_method2(L) == 10

def test_remove_dups():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    remove_dups(L1, L2)
    assert L1 == [3, 4]

def test_remove_dups_new():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    remove_dups_new(L1, L2)
    assert L1 == [3, 4]

