import add_path
import mit_ocw_exercises.lec7_debug_except as lec7
import pytest
import math



def test_rev_list():
    L = [1, 2, 3, 4]
    lec7.rev_list(L)
    assert L == [4, 3, 2, 1]

    L = []
    lec7.rev_list(L)
    assert L == []

    L = [7]
    lec7.rev_list(L)
    assert L == [7]

def test_primes_list():
    assert lec7.primes_list(2) == [2]
    assert lec7.primes_list(10) == [2, 3, 5, 7]
    assert lec7.primes_list(15) == [2, 3, 5, 7, 11, 13]

def test_get_ratios():
    assert lec7.get_ratios([2, 4], [2, 2]) == [1.0, 2.0]
    # 除零返回 nan
    res = lec7.get_ratios([1, 2], [0, 2])
    assert math.isnan(res[0])
    assert res[1] == 1.0
    # 异常输入
    with pytest.raises(ValueError):
        lec7.get_ratios([1, 2], [0])

def test_avg():
    assert lec7.avg([1, 2, 3]) == 2.0
    with pytest.raises(AssertionError):
        lec7.avg([])

def test_get_stats():
    test_grades = [
        [['peter', 'parker'], [80.0, 70.0, 85.0]],
        [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
        [['captain', 'america'], [80.0, 70.0, 96.0]],
    ]
    result = lec7.get_stats(test_grades)
    assert result[0][0] == ['peter', 'parker']
    assert result[0][1] == [80.0, 70.0, 85.0]
    assert result[0][2] == pytest.approx(78.333, rel=1e-2)

    # 空成绩列表断言异常
    test_grades = [[['deadpool'], []]]
    with pytest.raises(AssertionError):
        lec7.get_stats(test_grades)
