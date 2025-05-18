import os
import sys
import pytest

sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../src'))

import mit_ocw_exercises.lec5_tuples_lists as lec5


def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(10, 3) == (3, 1)
    assert lec5.quotient_and_remainder(25, 5) == (5, 0)
    with pytest.raises(ZeroDivisionError):
        lec5.quotient_and_remainder(10, 0)


def test_get_data():
    test = ((3, "apple"), (9, "banana"), (3, "apple"), (5, "banana"))
    assert lec5.get_data(test) == (3, 9, 2)

    test = ((15, "dog"), (7, "cat"), (20, "bird"), (15, "dog"))
    assert lec5.get_data(test) == (7, 20, 3)


def test_sum_elem_method1():
    assert lec5.sum_elem_method1([1, 2, 3]) == 6
    assert lec5.sum_elem_method1([0]) == 0
    assert lec5.sum_elem_method1([]) == 0


def test_sum_elem_method2():
    assert lec5.sum_elem_method2([1, 2, 3]) == 6
    assert lec5.sum_elem_method2([10]) == 10
    assert lec5.sum_elem_method2([]) == 0


def test_remove_dups():
    l1 = [1, 2, 3, 4]
    l2 = [2, 4]
    lec5.remove_dups(l1, l2)
    assert l1 == [1, 3]


def test_remove_dups_new():
    l1 = [10, 20, 30]
    l2 = [10, 50]
    lec5.remove_dups_new(l1, l2)
    assert l1 == [20, 30]


def test_aliasing_behavior():
    warm = ['red', 'yellow']
    hot = warm
    hot.append('pink')
    assert warm == ['red', 'yellow', 'pink']
    assert hot is warm


def test_cloning_behavior():
    cool = ['blue', 'green']
    chill = cool[:]
    chill.append('grey')
    assert cool == ['blue', 'green']
    assert chill == ['blue', 'green', 'grey']
    assert chill is not cool


def test_sorting_mutation():
    warm = ['red', 'yellow', 'orange']
    result = warm.sort()
    assert warm == ['orange', 'red', 'yellow']
    assert result is None


def test_sorting_no_mutation():
    cool = ['grey', 'green', 'blue']
    sorted_cool = sorted(cool)
    assert cool == ['grey', 'green', 'blue']
    assert sorted_cool == ['blue', 'green', 'grey']


def test_nested_lists_behavior():
    warm = ['yellow', 'orange']
    hot = ['red']
    brightcolors = [warm]
    brightcolors.append(hot)
    hot.append('pink')
    assert brightcolors == [['yellow', 'orange'], ['red', 'pink']]