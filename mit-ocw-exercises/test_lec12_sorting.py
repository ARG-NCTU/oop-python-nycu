from lec12_sorting import *
import pytest

# Test bubble_sort
def test_bubble_sort():
    testList = [1,3,5,7,2,6,25,18,13]
    assert bubble_sort(testList) == [1,2,3,5,6,7,13,18,25]
    
    print('')
    print(bubble_sort(testList))
    print(testList)

# Test selection_sort
def test_selection_sort():

    testList = [1,3,5,7,2,6,25,18,13]
           
    print('')
    print(selection_sort(testList))
    print(testList)

# Test merge_sort
def test_merge_sort():

    testList = [1,3,5,7,2,6,25,18,13]
    
    #print('')
    #print(merge_sort(testList))

