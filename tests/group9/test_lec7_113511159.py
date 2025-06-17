import add_path
from mit_ocw_exercises.lec7_debug_except import rev_list, primes_list, get_ratios, avg, get_stats
import pytest
import math

def test_rev_list():
    L = [1, 2, 3, 4]
    rev_list(L)
    assert L == [4, 3, 2, 1]

    L2 = []
    rev_list(L2)
    assert L2 == []

    L3 = [42]
    rev_list(L3)
    assert L3 == [42]

def test_primes_list():
    assert primes_list(2) == [2]
    assert primes_list(3) == [2, 3]
    assert primes_list(10) == [2, 3, 5, 7]
    assert primes_list(15) == [2, 3, 5, 7, 11, 13]

def test_get_ratios():
    assert get_ratios([1, 4], [2, 4]) == [0.5, 1.0]

    res = get_ratios([1, 4], [0, 4])
    assert math.isnan(res[0]) and res[1] == 1.0

    try:
        get_ratios([1], ['a'])
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

def test_avg():
    assert avg([1, 2, 3, 4]) == 2.5

    try:
        avg([])
    except AssertionError as e:
        assert str(e) == 'warning: no grades data'
    else:
        assert False, "Expected AssertionError"

def test_get_stats():
    test_grades = [
        [['peter', 'parker'], [80.0, 70.0, 85.0]],
        [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
        [['captain', 'america'], [80.0, 70.0, 96.0]],
        [['deadpool'], []]
    ]
    try:
        result = get_stats(test_grades)
    except AssertionError as e:
        assert str(e) == 'warning: no grades data'
    else:
        assert False, "Expected AssertionError"


if __name__ == "__main__":
    test_rev_list()
    test_primes_list()
    test_get_ratios()
    test_avg()
    test_get_stats()
    print("All tests passed!")
