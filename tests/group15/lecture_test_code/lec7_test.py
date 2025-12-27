import pytest
import math
import lec7 as lec

def test_rev_list():
    """測試串列反轉函式"""
    # 基本情況 (偶數長度)
    L1 = [1, 2, 3, 4]
    lec.rev_list(L1)
    assert L1 == [4, 3, 2, 1]

    # 基本情況 (奇數長度)
    L2 = [1, 2, 3, 4, 5]
    lec.rev_list(L2)
    assert L2 == [5, 4, 3, 2, 1]

    # 邊界情況：空串列
    L3 = []
    lec.rev_list(L3)
    assert L3 == []

    # 邊界情況：只有一個元素的串列
    L4 = [10]
    lec.rev_list(L4)
    assert L4 == [10]

def test_primes_list():
    """測試質數生成函式"""
    # 基本情況
    assert lec.primes_list(15) == [2, 3, 5, 7, 11, 13]
    
    # 邊界情況
    assert lec.primes_list(2) == [2]

    # 測試修正後 n < 2 的情況
    assert lec.primes_list(1) == []
    assert lec.primes_list(0) == []
    assert lec.primes_list(-10) == []

def test_get_ratios():
    """測試比例計算函式，包含例外處理"""
    # 正常情況與除以零的情況
    ratios = lec.get_ratios([1, 4, 6], [2, 0, 3])
    assert ratios[0] == 0.5
    assert math.isnan(ratios[1])
    assert ratios[2] == 2.0

    # 測試傳入不同長度串列時是否拋出 ValueError
    with pytest.raises(ValueError, match='different lengths'):
        lec.get_ratios([1, 2], [1])

    # 測試傳入錯誤型別參數時是否拋出 ValueError
    with pytest.raises(ValueError, match='bad argument type'):
        lec.get_ratios([1, 'a'], [2, 3])

def test_avg():
    """單獨測試 avg 輔助函式"""
    assert lec.avg([80, 90, 100]) == 90.0
    assert lec.avg([]) == 0.0
    assert lec.avg([10.5, 20.5]) == 15.5

def test_get_stats():
    """測試主函式 get_stats"""
    test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]],
                   [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
                   [['deadpool'], []]]

    stats = lec.get_stats(test_grades)

    # 驗證 peter 的平均成績
    assert stats[0][0] == ['peter', 'parker']
    # 療法：將期望值修正為正確的計算結果，並使用 pytest.approx 比較浮點數
    assert stats[0][2] == pytest.approx(78.33333333333333)

    # 同樣地，我們也應該為 Bruce Wayne 使用 approx
    assert stats[1][2] == pytest.approx(84.66666666666667)
    
    # 驗證 deadpool 的平均成績
