import pytest
import math

from src.mit_ocw_exercises.lec7_debug_except import rev_list, primes_list, get_ratios, get_stats, avg

def test_rev_list():
    L = [1, 2, 3, 4]
    rev_list(L)
    assert L == [4, 3, 2, 1]

    L = []
    rev_list(L)
    assert L == []

    L = [7]
    rev_list(L)
    assert L == [7]

def test_primes_list():
    assert primes_list(2) == [2]
    assert primes_list(10) == [2, 3, 5, 7]
    assert primes_list(15) == [2, 3, 5, 7, 11, 13]

