import math
import pytest

from src.mit_ocw_exercises.lec7_debug_except import rev_list, primes_list, get_ratios, avg
import add_path

def test_rev_list():
    data = [9, 8, 7, 6]
    expected = [6, 7, 8, 9]
    rev_list(data)
    assert data == expected

    data = []
    expected = []
    rev_list(data)
    assert data == expected

    data = [11]
    expected = [11]
    rev_list(data)
    assert data == expected

def test_primes_list():
    assert primes_list(5) == [2, 3, 5]
    assert primes_list(13) == [2, 3, 5, 7, 11, 13]
    assert primes_list(19) == [2, 3, 5, 7, 11, 13, 17, 19]
