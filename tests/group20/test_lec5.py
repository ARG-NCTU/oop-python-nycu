import pytest
from lec5 import (
    quotient_and_remainder, get_data, sum_elem_method1, sum_elem_method2,
    list_operations, sort_lists, demonstrate_aliasing, demonstrate_cloning,
    nested_list_operations, remove_dups, remove_dups_new
)

def test_quotient_and_remainder():
    assert quotient_and_remainder(5, 3) == (1, 2)
    assert quotient_and_remainder(10, 5) == (2, 0)
    assert quotient_and_remainder(0, 7) == (0, 0)
    with pytest.raises(ZeroDivisionError):
        quotient_and_remainder(5, 0)

def test_get_data():
    test = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    assert get_data(test) == (1, 7, 2)
    tswift = ((2014, "Katy"), (2014, "Harry"), (2012, "Jake"), (2010, "Taylor"), (2008, "Joe"))
    assert get_data(tswift) == (2008, 2014, 5)
    assert get_data(()) == (0, 0, 0)

def test_sum_elem_method1():
    assert sum_elem_method1([1, 2, 3, 4]) == 10
    assert sum_elem_method1([]) == 0
    assert sum_elem_method1([0]) == 0

def test_sum_elem_method2():
    assert sum_elem_method2([1, 2, 3, 4]) == 10
    assert sum_elem_method2([]) == 0
    assert sum_elem_method2([-1, 1]) == 0

def test_list_operations():
    L1 = [2, 1, 3]
    L2 = [4, 5, 6]
    result = list_operations(L1, L2)
    assert result['concat'] == [2, 1, 3, 4, 5, 6]
    assert result['extend'] == [2, 1, 3, 0, 6]
    assert result['remove_del'] == [6, 7, 0]
    assert result['pop'] == 0
    assert result['string_to_list'] == ['I', '<', '3', ' ', 'c', 's']
    assert result['split'] == ['I', '3 cs']
    assert result['join'] == 'abc'
    assert result['join_with_underscore'] == 'a_b_c'

def test_sort_lists():
    L = [9, 6, 0, 3]
    result = sort_lists(L)
    assert result['sorted'] == [0, 3, 6, 9]
    assert result['sort'] == [0, 3, 6, 9]
    assert result['reverse'] == [9, 6, 3, 0]
    assert L != result['sort']  # Original L unchanged

def test_demonstrate_aliasing():
    L = ['red', 'yellow', 'orange']
    result = demonstrate_aliasing(L)
    assert result['original'] == ['red', 'yellow', 'orange', 'pink']
    assert result['aliased'] == ['red', 'yellow', 'orange', 'pink']
    assert result['original'] is result['aliased']

def test_demonstrate_cloning():
    L = ['blue', 'green', 'grey']
    result = demonstrate_cloning(L)
    assert result['original'] == ['blue', 'green', 'grey']
    assert result['cloned'] == ['blue', 'green', 'grey', 'black']
    assert result['original'] is not result['cloned']

def test_nested_list_operations():
    base = ['yellow', 'orange']
    append = ['red']
    result = nested_list_operations(base, append)
    assert result == [['yellow', 'orange'], ['red', 'pink']]
    assert append == ['red', 'pink']
    assert base == ['yellow', 'orange']

def test_remove_dups():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    result = remove_dups(L1, L2)
    assert result == [3, 4] or result == [2, 3, 4]  # May skip elements
    assert L1 == result

def test_remove_dups_new():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    result = remove_dups_new(L1, L2)
    assert result == [3, 4]
    assert L1 == [3, 4]
