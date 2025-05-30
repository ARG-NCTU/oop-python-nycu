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

def test_get_ratios():
    assert get_ratios([2, 4], [2, 2]) == [1.0, 2.0]
    # 除零返回 nan
    res = get_ratios([1, 2], [0, 2])
    assert math.isnan(res[0])
    assert res[1] == 1.0
    # 异常输入
    with pytest.raises(ValueError):
        get_ratios([1, 2], [0])

def test_avg():
    assert avg([1, 2, 3]) == 2.0
    with pytest.raises(AssertionError):
        avg([])

def test_get_stats():
    test_grades = [
        [['peter', 'parker'], [80.0, 70.0, 85.0]],
        [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
        [['captain', 'america'], [80.0, 70.0, 96.0]],
    ]
    result = get_stats(test_grades)
    assert result[0][0] == ['peter', 'parker']
    assert result[0][1] == [80.0, 70.0, 85.0]
    assert result[0][2] == pytest.approx(78.333, rel=1e-2)

    # 空成绩列表断言异常
    test_grades = [[['deadpool'], []]]
    with pytest.raises(AssertionError):
        get_stats(test_grades)
