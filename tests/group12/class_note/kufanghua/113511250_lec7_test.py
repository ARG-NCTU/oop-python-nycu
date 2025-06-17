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

