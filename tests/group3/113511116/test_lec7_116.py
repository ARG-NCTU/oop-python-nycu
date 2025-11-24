import add_path
import mit_ocw_exercises.lec7_debug_except as lec7
import pytest

def test_rev_list():
    L = [1,2,3,4]
    lec7.rev_list(L)
    assert L == [4,3,2,1]

def test_primes_list():
    assert lec7.primes_list(10) == [2,3,5,7]
    assert lec7.primes_list(20) == [2,3,5,7,11,13,17,19]


def test_get_ratios():
    assert lec7.get_ratios([1,2,3], [1,2,3]) == [1.0, 1.0, 1.0]
    assert lec7.get_ratios([8, 5, 49], [2, 20, 7]) == [4.0, 0.25, 7.0]
    with pytest.raises(ValueError):
        lec7.get_ratios([1,2,'a'], [1,2,3])

    
  
def test_get_stats():
    # normal case: each person's avg is computed and returned
    data = [
        [['alice'], [50.0, 100.0]],
        [['bob'], [80.0]]
    ]
    stats = lec7.get_stats(data)
    assert stats == [
        [['alice'], [50.0, 100.0], 75.0],
        [['bob'], [80.0], 80.0]
    ]

    # if any student has empty grades, avg (final definition) asserts -> get_stats should propagate AssertionError
    with pytest.raises(AssertionError):
        lec7.get_stats([[['deadpool'], []]])

    
def test_avg():
    assert lec7.avg([80.0, 70.0, 85.0]) == 78.33333333333333
    assert lec7.avg([100.0, 80.0, 74.0]) == 84.66666666666667
    assert lec7.avg([80.0, 70.0, 96.0]) == 82.0

