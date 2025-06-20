# test_main.py

import math
import pytest
from main import rev_list, primes_list, get_ratios, get_stats, avg

def test_rev_list():
    L = [1, 2, 3, 4]
    rev_list(L)
    assert L == [4, 3, 2, 1]

    L2 = []
    rev_list(L2)
    assert L2 == []

    L3 = [7]
    rev_list(L3)
    assert L3 == [7]


def test_primes_list():
    assert primes_list(2) == [2]
    assert primes_list(10) == [2, 3, 5, 7]
    assert primes_list(1) == []
    assert primes_list(0) == []
    assert primes_list(17) == [2, 3, 5, 7, 11, 13, 17]  # Prime itself included


def test_get_ratios_normal():
    result = get_ratios([1, 4], [2, 2])
    assert result == [0.5, 2.0]


def test_get_ratios_zero_division():
    result = get_ratios([1, 4], [0, 2])
    assert math.isnan(result[0])
    assert result[1] == 2.0


def test_get_ratios_bad_input():
    with pytest.raises(ValueError):
        get_ratios([1, 'a'], [2, 1])


def test_get_stats_normal():
    class_list = [
        [['peter', 'parker'], [80.0, 70.0, 85.0]],
        [['bruce', 'wayne'], [100.0, 90.0]]
    ]
    result = get_stats(class_list)
    assert result[0][2] == pytest.approx(78.33, 0.01)
    assert result[1][2] == pytest.approx(95.0, 0.01)


def test_get_stats_with_empty_grades():
    class_list = [
        [['deadpool'], []]
    ]
    with pytest.raises(AssertionError):
        get_stats(class_list)
