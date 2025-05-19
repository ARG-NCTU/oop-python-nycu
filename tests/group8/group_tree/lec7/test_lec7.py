import lec7
import pytest

def test_rev_list():
    L = [1, 2, 3, 4]
    lec7.rev_list(L)
    assert L == [4, 3, 2, 1]

    L = []
    lec7.rev_list(L)
    assert L == []

    L = [1]
    lec7.rev_list(L)
    assert L == [1]

def test_primes_list():
    assert lec7.primes_list(2) == [2]
    assert lec7.primes_list(10) == [2, 3, 5, 7]
    assert lec7.primes_list(3) == [2, 3]  # Edge case: n <= 1

def test_get_ratios():
    assert lec7.get_ratios([1, 2, 3], [1, 2, 3]) == [1.0, 1.0, 1.0]
    assert lec7.get_ratios([1, 2, 3], [2, 3, 3]) == [0.5, 0.6666666666666666, 1.0]
    with pytest.raises(ValueError):
        lec7.get_ratios([1, 2], [1])  # Mismatched list lengths

def test_avg():
    assert lec7.avg([80.0, 70.0, 85.0]) == 78.33333333333333
    assert lec7.avg([0]) == 0.0  # Exception handling for empty list

