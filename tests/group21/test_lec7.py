import add_path
import lec7_debug_except as lec7
import pytest
import math

def test_rev_list():
    L = [1,2,3,4]
    lec7.rev_list(L)
    assert L == [4,3,2,1]

def test_primes_list():
    assert lec7.primes_list(2) == [2]
    assert lec7.primes_list(3) == [2,3]
    assert lec7.primes_list(11) == [2,3,5,7,11]
    assert lec7.primes_list(12) == [2,3,5,7,11]   

def test_get_ratios():
    assert lec7.get_ratios([1,2,3], [1,2,3]) == [1.0, 1.0, 1.0]
    assert lec7.get_ratios([1,2,3], [3,2,1]) == [1/3, 1.0, 3.0]

def test_get_ratios_zero_division():
    # 測試除以零的情況
    result = lec7.get_ratios([10, 20, 30], [2, 0, 10])
    expected = [5.0, float('nan'), 3.0]
    
    # 檢查結果中每一個元素，對比數字和 NaN
    for r, e in zip(result, expected):
        if math.isnan(e):
            assert math.isnan(r)  # 使用 math.isnan() 來檢查是否為 NaN
        else:
            assert r == e

def test_get_ratios_invalid_input():
    # 測試不合法的參數情況（例如：L1 和 L2 長度不相等）
    L1 = [10, 20, 30]
    L2 = [2, 5]  # L2 長度比 L1 短
    with pytest.raises(ValueError):
        lec7.get_ratios(L1, L2)

def test_get_ratios_non_number():
    # 測試列表中包含非數字元素
    L1 = [10, 20, 'a']  # L1 中有一個非數字元素
    L2 = [2, 5, 10]
    with pytest.raises(ValueError):
        lec7.get_ratios(L1, L2)

def test_get_stats():
    class_list = [
        [['peter', 'parker'], [80.0, 70.0, 85.0]],
        [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
        [['tony', 'stark'], []]  # 測試空成績列表
    ]
    
    # 使用帶異常處理的 avg 函數
    result = lec7.get_stats(class_list)
    expected = [
        [['peter', 'parker'],[80.0, 70.0, 85.0], 78.33333333333333],
        [['bruce', 'wayne'], [100.0, 80.0, 74.0],84.66666666666667],
        [['tony', 'stark'],[], 0.0]  # 如果成績為空，返回 0.0
    ]
    
    assert result == expected

