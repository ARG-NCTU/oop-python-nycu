import add_path
import mit_ocw_exercises.lec7_debug_except as l7 # type: ignore
import pytest

import math

def test_rev_list():

    L = [1, 2, 3, 4]
    l7.rev_list(L)
    assert L == [4, 3, 2, 1]

    L = []
    l7.rev_list(L)
    assert L == []

    L = [42]
    l7.rev_list(L)
    assert L == [42]

    L = ['r', 'a', 'c', 'e', 'a', 'c', 'a', 'r']
    l7.rev_list(L)
    assert L == ['r', 'a', 'c', 'a', 'e', 'c', 'a', 'r']


def test_primes_list():
    assert l7.primes_list(2) == [2]
    assert l7.primes_list(15) == [2, 3, 5, 7, 11, 13]
    assert l7.primes_list(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def test_get_ratios():
    assert l7.get_ratios([1, 4], [2, 4]) == [0.5, 1.0]
    assert l7.get_ratios([], []) == []

    result = l7.get_ratios([1, 2, 3], [0, 2, 1])
    assert result[1:3] == [1.0, 3.0]
    assert math.isnan(result[0])

    with pytest.raises(ValueError):
        l7.get_ratios([1, 2, 3], [1, 2])

def test_avg():
    assert l7.avg([11, 45, 14]) == pytest.approx(23.33333)

    with pytest.raises(AssertionError):
        l7.avg([])

def test_get_stats():
    test_list = [
        [['alice', 'smith'], [90.0, 80.0, 70.0]],
        [['bob', 'jones'], [100.0, 85.0]],
        [['charlie', 'brown'], [75.0, 95.0, 85.0, 65.0]]
    ]
    expected = [
        [['alice', 'smith'], [90.0, 80.0, 70.0], pytest.approx(80.0)],
        [['bob', 'jones'], [100.0, 85.0], pytest.approx(92.5)],
        [['charlie', 'brown'], [75.0, 95.0, 85.0, 65.0], pytest.approx(80.0)]
    ]
    assert l7.get_stats(test_list) == expected

    test_list_with_empty = [
        [['david', 'johnson'], []]
    ]
    with pytest.raises(AssertionError):
        l7.get_stats(test_list_with_empty)
    