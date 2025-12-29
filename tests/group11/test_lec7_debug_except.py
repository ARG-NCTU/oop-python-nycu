import pytest
import add_path
from lec7_debug_except import rev_list, primes_list, float, get_ratios, get_stats, avg

# -----------------
# 測試 rev_list
# -----------------
def test_rev_list():
    """測試 rev_list (原地反轉列表)"""
    L = [1, 2, 3, 4]
    rev_list(L)
    assert L == [4, 3, 2, 1]

    L = [1, 2, 3]
    rev_list(L)
    assert L == [3, 2, 1]

    L = []
    rev_list(L)
    assert L == []

# -----------------
# 測試 primes_list
# -----------------
def test_primes_list():
    """測試 primes_list (質數列表)"""
    assert primes_list(2) == [2]
    assert primes_list(3) == [2, 3]
    assert primes_list(5) == [2, 3, 5]
    # 檢查是否包含非質數
    primes_15 = primes_list(15)
    assert 4 not in primes_15
    assert 9 not in primes_15
    assert 13 in primes_15

# -----------------
# 測試 get_ratios
# -----------------
def test_get_ratios_success():
    """測試 get_ratios 正常情況"""
    L1 = [1, 4]
    L2 = [2, 4]
    assert get_ratios(L1, L2) == [0.5, 1.0]

def test_get_ratios_zero_division():
    """測試 get_ratios 遇到除以零 (應返回 NaN)"""
    L1 = [1, 2]
    L2 = [0, 2]
    ratios = get_ratios(L1, L2)
    # NaN 不等於自己，利用此特性檢查
    assert ratios[0] != ratios[0] 
    assert ratios[1] == 1.0

def test_get_ratios_bad_arg():
    """測試 get_ratios 遇到錯誤參數 (長度不同等引發 ValueError)"""
    with pytest.raises(ValueError):
        get_ratios([1], [1, 2])

# -----------------
# 測試 get_stats & avg
# -----------------
def test_avg_normal():
    """測試 avg 正常計算"""
    assert avg([10.0, 20.0]) == 15.0

def test_avg_empty():
    """測試 avg 空列表 (觸發 assert 錯誤)"""
    with pytest.raises(AssertionError, match="warning: no grades data"):
        avg([])

def test_get_stats():
    """測試 get_stats"""
    test_grades = [
        [['peter', 'parker'], [80.0, 70.0, 90.0]], 
        [['bruce', 'wayne'], [100.0, 100.0, 100.0]]
    ]
    stats = get_stats(test_grades)
    # peter avg = 240/3 = 80
    assert stats[0][2] == 80.0
    # bruce avg = 100
    assert stats[1][2] == 100.0
