import add_path
import mit_ocw_exercises.lec7_debug_except as lec7
import pytest


def test_rev_list():
    L = [1, 2, 3, 4, 5, 6]
    lec7.rev_list(L)
    assert L == [6, 5, 4, 3, 2, 1]
    L = ['a', 'b', 'c']
    lec7.rev_list(L)
    assert L == ['c', 'b', 'a']
    L = []
    lec7.rev_list(L)
    assert L == []
    L = [1]
    lec7.rev_list(L)
    assert L == [1]

def test_primes_list():
    assert lec7.primes_list(2) == [2]
    assert lec7.primes_list(10) == [2, 3, 5, 7]
    assert lec7.primes_list(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert lec7.primes_list(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def test_get_ratios():
    assert lec7.get_ratios([1, 2, 3], [1, 2, 3]) == [1.0, 1.0, 1.0]
    assert lec7.get_ratios([0, 0, 0], [5, 2, 4]) == [0.0, 0.0, 0.0]
    assert lec7.get_ratios([8, 5, 49], [2, 20, 7]) == [4.0, 0.25, 7.0]
    assert lec7.get_ratios([], []) == []



def test_get_stats():
    name_and_grades = [("Alice", [90, 94, 92]), ("Bob", [80, 85, 84]), ("Charlie", [70, 98, 72])]
    assert lec7.get_stats(name_and_grades) == [["Alice", [90, 94, 92], 92.0], ["Bob", [80, 85, 84], 83.0], ["Charlie", [70, 98, 72], 80.0]]

def test_avg():
    assert lec7.avg([1, 2, 3]) == 2.0
    assert lec7.avg([0, 0, 0]) == 0.0
    assert lec7.avg([95, 84, 91]) == 90.0
    assert lec7.avg([45, 87, 62, 97, 58]) == 69.8