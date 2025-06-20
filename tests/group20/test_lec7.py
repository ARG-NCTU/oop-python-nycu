import pytest
from lec7 import rev_list, primes_list, get_ratios, get_stats, avg
import math

def test_rev_list():
    L = [1, 2, 3, 4]
    rev_list(L)
    assert L == [4, 3, 2, 1]
    L = [1]
    rev_list(L)
    assert L == [1]
    L = []
    rev_list(L)
    assert L == []

def test_primes_list():
    assert primes_list(2) == [2]
    assert primes_list(15) == [2, 3, 5, 7, 11, 13]
    with pytest.raises(ValueError):
        primes_list(1)  # Assumes n > 1

def test_get_ratios(capsys):
    result = get_ratios([1, 4], [2, 4])
    assert result == [0.5, 1.0]
    captured = capsys.readouterr()
    assert captured.out.count("success") == 2
    assert captured.out.count("executed no matter what!") == 2

    result = get_ratios([1, 2], [0, 4])
    assert math.isnan(result[0]) and result[1] == 0.5
    captured = capsys.readouterr()
    assert captured.out.count("success") == 1
    assert captured.out.count("executed no matter what!") == 2

    with pytest.raises(ValueError):
        get_ratios([1], [2, 3])
    with pytest.raises(ValueError):
        get_ratios([1], ['a'])

def test_avg():
    assert avg([80.0, 70.0, 85.0]) == 78.33333333333333
    assert avg([100.0]) == 100.0
    with pytest.raises(AssertionError):
        avg([])

def test_get_stats():
    class_list = [
        [['peter', 'parker'], [80.0, 70.0, 85.0]],
        [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
        [['deadpool'], []]
    ]
    result = get_stats(class_list)
    assert result[0] == [['peter', 'parker'], [80.0, 70.0, 85.0], 78.33333333333333]
    assert result[1] == [['bruce', 'wayne'], [100.0, 80.0, 74.0], 84.66666666666667]
    with pytest.raises(AssertionError):
        assert result[2] == [['deadpool'], [], 0.0]  # Triggers avg assertion
