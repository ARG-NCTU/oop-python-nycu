import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import add_path
from src.mit_ocw_exercises.lec7_debug_except import rev_list, primes_list, get_ratios, get_stats, avg

def test_rev_list():
    L = [1, 2, 3, 4, 5, 6]
    rev_list(L)
    assert L == [6, 5, 4, 3, 2, 1]
    L = ['a', 'b', 'c']
    rev_list(L)
    assert L == ['c', 'b', 'a']
    L = []
    rev_list(L)
    assert L == []
    L = [1]
    rev_list(L)
    assert L == [1]

def test_primes_list():
    assert primes_list(2) == [2]
    assert primes_list(10) == [2, 3, 5, 7]
    assert primes_list(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert primes_list(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def test_get_ratios():
    assert get_ratios([1, 2, 3], [1, 2, 3]) == [1.0, 1.0, 1.0]
    assert get_ratios([0, 0, 0], [5, 2, 4]) == [0.0, 0.0, 0.0]
    assert get_ratios([8, 5, 49], [2, 20, 7]) == [4.0, 0.25, 7.0]
    assert get_ratios([], []) == []

def test_get_stats():
    name_and_grades = [("Alice", [90, 94, 92]), ("Bob", [80, 85, 84]), ("Charlie", [70, 98, 72])]
    assert get_stats(name_and_grades) == [["Alice", [90, 94, 92], 92.0], ["Bob", [80, 85, 84], 83.0], ["Charlie", [70, 98, 72], 80.0]]

def test_avg():
    assert avg([1, 2, 3]) == 2.0
    assert avg([0, 0, 0]) == 0.0
    assert avg([95, 84, 91]) == 90.0
    assert avg([45, 87, 62, 97, 58]) == 69.8

def test_avg_capfd(capfd):
    try:
        avg([])
    except AssertionError:
        pass