import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lec5_tuples_lists import (
    quotient_and_remainder, get_data, 
    sum_elem_method1, sum_elem_method2,
    remove_dups, remove_dups_new
)

def test_quotient_and_remainder():
    """測試商數與餘數"""
    assert quotient_and_remainder(5, 3) == (1, 2)
    assert quotient_and_remainder(10, 2) == (5, 0)
    assert quotient_and_remainder(7, 4) == (1, 3)

def test_get_data():
    """測試 tuple 資料提取 (min, max, unique_words)"""
    # 測試與 lec5 範例相同
    test_data = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    min_n, max_n, unique_words = get_data(test_data)
    assert min_n == 1
    assert max_n == 7
    assert unique_words == 2  # "a", "b"

    # 測試更多資料
    tswift = ((2014,"Katy"), (2014, "Harry"), (2012,"Jake"), (2010,"Taylor"))
    min_year, max_year, count = get_data(tswift)
    assert min_year == 2010
    assert max_year == 2014
    assert count == 4 # Katy, Harry, Jake, Taylor

def test_sum_elem():
    """測試列表求和"""
    L = [1, 2, 3, 4]
    assert sum_elem_method1(L) == 10
    assert sum_elem_method2(L) == 10
    
    L_empty = []
    assert sum_elem_method1(L_empty) == 0
    assert sum_elem_method2(L_empty) == 0

def test_remove_dups():
    """測試移除重複 (原地修改，且有迭代時修改的潛在問題)"""
    # 這是原始代碼的邏輯，雖然可能有 bug (跳過元素)，但我們要測試其行為是否符合現狀
    # 原始代碼：
    # for e in L1:
    #   if e in L2: L1.remove(e)
    # L1=[1,2,3,4], L2=[1,2,5,6]
    # Remove 1 -> L1 becomes [2,3,4], next iter checks index 1 which is '3', skipping '2'
    # 所以 2 不會被移除
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    remove_dups(L1, L2)
    # 預期結果根據 python list iteration 行為：1 被移除，2 被跳過，3 保留，4 保留
    # 實際結果應為 [2, 3, 4]
    assert L1 == [2, 3, 4] 

def test_remove_dups_new():
    """測試移除重複 (正確版本，複製後迭代)"""
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    remove_dups_new(L1, L2)
    # 預期：1 和 2 都在 L2 中，都應該被移除
    assert L1 == [3, 4]
