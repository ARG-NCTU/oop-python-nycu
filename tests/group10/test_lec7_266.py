import add_path
import pytest
import mit_ocw_exercises.lec7_debug_except as lec7
import math

def test_rev_list():
    L = [1, 2, 3, 4]
    lec7.rev_list(L)
    assert L == [4, 3, 2, 1]

    L = [1]
    lec7.rev_list(L)
    assert L == [1]

    L = []
    lec7.rev_list(L)
    assert L == []

    L = [5, 6, 7, 8, 9]
    lec7.rev_list(L)
    assert L == [9, 8, 7, 6, 5]

    L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lec7.rev_list(L)
    assert L == [9, 8, 7, 6, 5, 4, 3, 2, 1]

def test_primes_list():
    assert lec7.primes_list(2) == [2]
    assert lec7.primes_list(3) == [2, 3]
    assert lec7.primes_list(4) == [2, 3]
    assert lec7.primes_list(5) == [2, 3, 5]
    assert lec7.primes_list(6) == [2, 3, 5]

def test_get_ratios():
    assert lec7.get_ratios([1, 2, 3], [1, 2, 3]) == [1.0, 1.0, 1.0]
    assert lec7.get_ratios([1, 2, 3], [1, 2, 4]) == [1.0, 1.0, 0.75]

    result = lec7.get_ratios([1, 2, 3], [1, 2, 0])
    assert result[0] == 1.0
    assert result[1] == 1.0
    assert math.isnan(result[2])

    result = lec7.get_ratios([1, 2, 3], [1, 0, 3])
    assert result[0] == 1.0
    assert math.isnan(result[1])
    assert result[2] == 1.0


def test_get_stats():
    test_grades = [
        [['peter', 'parker'], [80.0, 70.0, 85.0]], 
        [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
        [['captain', 'america'], [80.0, 70.0, 96.0]], 
    ]
    expected_output = [
        [['peter', 'parker'], [80.0, 70.0, 85.0], 78.33333333333333],
        [['bruce', 'wayne'], [100.0, 80.0, 74.0], 84.66666666666667],
        [['captain', 'america'], [80.0, 70.0, 96.0], 82.0],
    ]
    result = lec7.get_stats(test_grades)
    assert result == expected_output



def test_get_stats_empty_grades_raise():
    with pytest.raises(AssertionError, match="warning: no grades data"):
        lec7.get_stats([[['deadpool'], []]])