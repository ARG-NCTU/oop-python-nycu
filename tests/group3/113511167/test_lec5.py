from lec5 import quotient_and_remainder, get_data, sum_elem_method1, sum_elem_method2

def test_quotient_and_remainder():
    assert quotient_and_remainder(5, 3) == (1, 2)
    assert quotient_and_remainder(10, 2) == (5, 0)
    assert quotient_and_remainder(7, 4) == (1, 3)
    assert quotient_and_remainder(0, 1) == (0, 0)


def test_get_data():
    test_data = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    assert get_data(test_data) == (1, 7, 2)
    
    tswift = ((2014, "Katy"), (2014, "Harry"), (2012, "Jake"), (2010, "Taylor"), (2008, "Joe"))
    assert get_data(tswift) == (2008, 2014, 5)

def test_sum_1():
    tset_data = [1, 2, 3, 4, 5]
    assert sum_elem_method1(tset_data) == 15
    assert sum_elem_method1([]) == 0
    assert sum_elem_method1([10]) == 10
    assert sum_elem_method1([-1, -2, -3]) == -6

def test_sum_2(): 
    test_data = [1, 2, 3, 4, 5]
    assert sum_elem_method2(test_data) == 15
    assert sum_elem_method2([]) == 0
    assert sum_elem_method2([10]) == 10
    assert sum_elem_method2([-1, -2, -3]) == -6