
import pytest
from lec12_sorting import bubble_sort_np, selection_sort_np, merge_sort_np, merge_np


def test_bubble_sort_np():

    L1 = [5, 1, 4, 2, 8]
    assert bubble_sort_np(L1) == [1, 2, 4, 5, 8]
    L2 = [1, 2, 3]
    assert bubble_sort_np(L2) == [1, 2, 3]
    L3 = [3, 2, 1]
    assert bubble_sort_np(L3) == [1, 2, 3]
    L4 = [2, 1, 3, 2, 1]
    assert bubble_sort_np(L4) == [1, 1, 2, 2, 3]
    L5 = [-10, 5, 0, -2]
    assert bubble_sort_np(L5) == [-10, -2, 0, 5]
    assert bubble_sort_np([]) == []
    assert bubble_sort_np([42]) == [42]
def test_selection_sort_np():

    L1 = [5, 1, 4, 2, 8]
    return_val = selection_sort_np(L1) 
    assert return_val is None          
    assert L1 == [1, 2, 4, 5, 8]      
    L3 = [3, 2, 1]
    selection_sort_np(L3)
    assert L3 == [1, 2, 3]
    L4 = [2, 1, 3, 2, 1]
    selection_sort_np(L4)
    assert L4 == [1, 1, 2, 2, 3]
    
    L_empty = []
    selection_sort_np(L_empty)
    assert L_empty == []
    L_single = [42]
    selection_sort_np(L_single)
    assert L_single == [42]
def test_merge_sort_np():
    L1 = [5, 1, 4, 2, 8]
    L1_original = L1[:]
    
    result = merge_sort_np(L1)
    assert result == [1, 2, 4, 5, 8]   
    assert L1 == L1_original         
    L3 = [3, 2, 1]
    assert merge_sort_np(L3) == [1, 2, 3]
    L4 = [2, 1, 3, 2, 1]
    assert merge_sort_np(L4) == [1, 1, 2, 2, 3]
    assert merge_sort_np([]) == []
    assert merge_sort_np([42]) == [42]
def test_merge_np():

    left = [1, 3, 5]
    right = [2, 4, 6]
    assert merge_np(left, right) == [1, 2, 3, 4, 5, 6]

    left_short = [1, 5]
    right_long = [2, 4, 6, 8]
    assert merge_np(left_short, right_long) == [1, 2, 4, 5, 6, 8]
 
   
