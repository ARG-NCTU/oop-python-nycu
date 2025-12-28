import pytest
import math
import lec7_debug_except as lec


"""
lec7 測試檔（中文註解版）

本檔包含多個單元測試，用以驗證 `lec7_debug_except` 模組中函式的正確性：
- `rev_list`：就地反轉列表的行為（含邊界情況）
- `primes_list`：產生 <= n 的質數列表（含 n < 2 的處理）
- `get_ratios`：計算對應元素的商並處理例外（除以零、長度不符、型別錯誤）
- `avg`：平均數計算（空列表回傳 0.0）
- `get_stats`：將學生資料轉換成包含平均數的統計資料

註：只加入註解說明，不更動測試邏輯。
"""

def test_rev_list():
    """測試串列反轉函式

    測試要點：
    - 基本情況：偶數長度、奇數長度
    - 邊界情況：空串列、單元素串列
    """
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
    """測試質數生成函式

    測試要點：
    - 基本情況：n=15 回傳已知質數
    - 邊界情況：n=2
    - 異常情況：n < 2 應回傳空列表
    """
    # 基本情況
    assert lec.primes_list(15) == [2, 3, 5, 7, 11, 13]
    
    # 邊界情況
    assert lec.primes_list(2) == [2]

    # 測試修正後 n < 2 的情況
    assert lec.primes_list(1) == []
    assert lec.primes_list(0) == []
    assert lec.primes_list(-10) == []

def test_get_ratios():
    """測試比例計算函式，包含例外處理

    測試要點：
    - 正常與除以零情況：對應位置的商或 NaN
    - 長度不符：應拋出 ValueError，訊息包含 'different lengths'
    - 型別錯誤：例如數字除以非數字，應拋出 ValueError，訊息包含 'bad argument type'
    """
    # 正常情況與除以零的情況
    ratios = lec.get_ratios([1, 4, 6], [2, 0, 3])
    assert ratios[0] == 0.5
    assert math.isnan(ratios[1])
    assert ratios[2] == 2.0

    # 測試傳入不同長度串列時是否拋出 ValueError
    with pytest.raises(ValueError, match='different lengths'):
        lec.get_ratios([1, 2], [1])

    with pytest.raises(ValueError, match='bad argument type'):
        lec.get_ratios([1, 'a'], [2, 3])

def test_avg():
    assert lec.avg([80, 90, 100]) == 90.0
    assert lec.avg([]) == 0.0
    assert lec.avg([10.5, 20.5]) == 15.5

def test_get_stats():
    test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]],
                   [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
                   [['deadpool'], []]]

    stats = lec.get_stats(test_grades)
    assert stats[0][0] == ['peter', 'parker']
    assert stats[0][2] == pytest.approx(78.33333333333333)
    assert stats[1][2] == pytest.approx(84.66666666666667)
    

