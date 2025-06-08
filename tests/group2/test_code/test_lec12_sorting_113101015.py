import pytest
import lec12_sorting as lec12
import math

def test_bubble_sort():
    List = [4,2,3,1]
    assert lec12.bubble_sort(List) == [1,2,3,4]
    List = [4,2,3,1,5,-1]
    assert lec12.bubble_sort(List) == [-1,1,2,3,4,5]

def test_merge_sort():
    List = [4,3,2,1]
    assert lec12.merge_sort(List) == [1,2,3,4]
    List = [4,2,3,1,5,-1]
    assert lec12.merge_sort(List) == [-1,1,2,3,4,5]
    #
