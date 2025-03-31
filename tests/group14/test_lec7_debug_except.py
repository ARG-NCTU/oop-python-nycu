import add_path
import pytest
import mit_ocw_exercises.lec7_debug_except as lec7

#lec7 need to ignore some lines ex ：99 - 122 ....

def test_primes_list():
    assert lec7.primes_list(2) == [2]
    assert lec7.primes_list(3) == [2, 3]
    assert lec7.primes_list(4) == [2, 3]
    assert lec7.primes_list(5) == [2, 3, 5]
    assert lec7.primes_list(6) == [2, 3, 5]
    assert lec7.primes_list(7) == [2, 3, 5, 7]
    assert lec7.primes_list(8) == [2, 3, 5, 7]
    assert lec7.primes_list(9) == [2, 3, 5, 7]

def test_rev_list():
    L = [1,2,3,4]
    lec7.rev_list(L)
    assert L == [4,3,2,1]

def test_get_stats():
    assert lec7.get_stats( [ ['Alice', [90, 80, 85]] , ['Bob', [70, 75, 80]] ]) == [ ['Alice',[90, 80, 85], 85.0 ], ['Bob',[70, 75, 80], 75.0] ]

def test_avg():
    assert lec7.avg([1,2,3]) == 2.0
    assert lec7.avg([1,2,3,4]) == 2.5

 