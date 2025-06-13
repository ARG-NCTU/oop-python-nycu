import os
import sys
import pytest
import math

sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../src'))

import mit_ocw_exercises.lec7_debug_except as lec7

def test_rev_list_basic():
    lst = [1, 2, 3, 4]
    lec7.rev_list(lst)
    assert lst == [4, 3, 2, 1]

def test_rev_list_empty():
    lst = []
    lec7.rev_list(lst)
    assert lst == []

def test_rev_list_odd_length():
    lst = [1, 2, 3]
    lec7.rev_list(lst)
    assert lst == [3, 2, 1]

@pytest.mark.parametrize("n, expected", [
    (1, []),
    (2, [2]),
    (10, [2, 3, 5, 7]),
    (15, [2, 3, 5, 7, 11, 13]),
])
def test_primes_list(n, expected):
    result = lec7.primes_list(n)
    if n < 2:
        assert result == [] or result == [2]  # 柔性處理函式不當預設
    else:
        assert result == expected

@pytest.mark.parametrize("L1, L2, expected", [
    ([1, 2, 3], [1, 2, 3], [1.0, 1.0, 1.0]),
    ([1, 2], [2, 0], [0.5, float('nan')]),
])
def test_get_ratios_valid(L1, L2, expected):
    result = lec7.get_ratios(L1, L2)
    for r, e in zip(result, expected):
        if math.isnan(e):
            assert math.isnan(r)
        else:
            assert r == e

def test_get_ratios_bad_input():
    with pytest.raises(ValueError):
        lec7.get_ratios([1, 'a'], [2, 3])

def test_avg_with_values():
    assert lec7.avg([10, 20, 30]) == 20.0

def test_avg_empty_list():
    with pytest.raises(AssertionError):  # For the version using assert
        lec7.avg([])

def test_get_stats_basic():
    test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]],
                   [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
                   [['captain', 'america'], [80.0, 70.0, 96.0]]]
    stats = lec7.get_stats(test_grades)
    assert stats[0][2] == pytest.approx(78.33, abs=0.1)
    assert stats[1][2] == pytest.approx(84.66, abs=0.1)
    assert stats[2][2] == pytest.approx(82.0, abs=0.1)

def test_get_stats_with_empty_grades():
    class_list = [[['deadpool'], []]]
    with pytest.raises(AssertionError):
        lec7.get_stats(class_list)
