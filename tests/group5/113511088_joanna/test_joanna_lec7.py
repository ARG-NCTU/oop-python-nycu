from lec7_final import *
import math

def test_rev_list():
    assert rev_list([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert rev_list([]) == []

def test_primes_list():
    assert primes_list(2) == [2]
    assert primes_list(15) == [2, 3, 5, 7, 11, 13]
    assert primes_list(1) == []

def test_get_ratios():
    result = get_ratios([1, 4], [2, 4])
    assert result == [0.5, 1.0]

    result = get_ratios([1, 4], [0, 4])
    assert math.isnan(result[0]) and result[1] == 1.0

def test_avg():
    assert avg([80.0, 70.0, 85.0]) == 78.33333333333333

def test_get_stats():
    test_grades = [
        [['peter', 'parker'], [80.0, 70.0, 85.0]],
        [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
        [['captain', 'america'], [80.0, 70.0, 96.0]],
        [['deadpool'], []]
    ]
    stats = get_stats(test_grades)
    assert stats[0][2] == avg([80.0, 70.0, 85.0])
    assert stats[3][2] == 0.0
