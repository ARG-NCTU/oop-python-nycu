import add_path
import pytest
import mit_ocw_exercises.lec7_debug_except as lec7
import math

def test_rev_list():
    L = [1, 3, 5]
    lec7.rev_list(L)
    assert L == [5, 3, 1]
    L = []
    lec7.rev_list(L)
    assert L == []
    L = [12]
    lec7.rev_list(L)
    assert L == [12]
    L = [1, 2, 3, 4, 5]
    lec7.rev_list(L)
    assert L == [5, 4, 3, 2, 1]

def test_primes_list():
    assert lec7.primes_list(2) == [2]
    assert lec7.primes_list(3) == [2, 3]
    assert lec7.primes_list(6) == [2, 3, 5]

def test_get_ratios():
    assert lec7.get_ratios([1, 2, 3], [1, 2, 3]) == [1.0, 1.0, 1.0]
    assert lec7.get_ratios([1, 2, 3], [1, 1, 4]) == [1.0, 2.0, 0.75]
    
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
        [['minju', 'k'], [90.0, 80.0, 95.0]], 
        [['hyewon', 'k'], [100.0, 80.0, 74.0]],
        [['yuri', 'j'], [50.0, 70.0, 66.0]], 
    ]
    expected_output = [
        [['minju', 'k'], [90.0, 80.0, 95.0], 88.33333333333333],
        [['hyewon', 'k'], [100.0, 80.0, 74.0], 84.66666666666667],
        [['yuri', 'j'], [50.0, 70.0, 66.0], 62.0],
    ]
    result = lec7.get_stats(test_grades)
    assert result == expected_output
