import pytest
import lec7_debug_except as lec7
import math

def test_rev_list():
    L = []
    lec7.rev_list(L)
    assert L == []
    L = ['a']
    lec7.rev_list(L)
    assert L == ['a']
    L = ["johnny","hate","OOP"]
    lec7.rev_list(L)
    assert L == ["OOP","hate","johnny"] #test string
def test_primes_list():
    assert lec7.primes_list(2) == [2]
    assert lec7.primes_list(3) == [2, 3]
    assert lec7.primes_list(4) == [2, 3]
    assert lec7.primes_list(5) == [2, 3, 5]
    assert lec7.primes_list(6) == [2, 3, 5]
    assert lec7.primes_list(7) == [2, 3, 5, 7]
    assert lec7.primes_list(8) == [2, 3, 5, 7]
    assert lec7.primes_list(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_get_ratios():
    assert lec7.get_ratios([2, 4, 6, 8], [2, 4, 6, 8]) == [1.0, 1.0, 1.0, 1.0]

    assert lec7.get_ratios([1, 2, 3], [0.5, 0.5, 0.5]) == [2, 4, 6]

    result = lec7.get_ratios([1, 2, 3], [0, 2, 3]) #zerodivisionerror
    assert math.isnan(result[0])
    assert result[1] == 1.0
    assert result[2] == 1.0


def test_get_stats():
    test_grades = [
        [["Howard Hung"],[113,10,1014]],
         [["Lawrence Hsia"],[113,10,1018]],
         [["Johnny Chang"],[113,10,1015]]
    ]
    expected_output = [
        [["Howard Hung"],[113,10,1014],379],
         [["Lawrence Hsia"],[113,10,1018],380.33333333333333],
         [["Johnny Chang"],[113,10,1015],379.33333333333333]
    ]
    result = lec7.get_stats(test_grades)
    assert result == expected_output


def test_get_stats_empty_grades_raise():
    with pytest.raises(AssertionError, match="warning: no grades data"):
        lec7.get_stats([[['Niromot'], []]])
