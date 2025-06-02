import add_path
from mit_ocw_exercises.lec12_sorting import *
import pytest
import time
import random
# Test bubble_sort
def test_bubble_sort():
    testList = [1,5,8,2,4,6,98,46,45]
    assert bubble_sort(testList) == [1,2,4,5,6,8,45,46,98]
    
    print('')
    print(bubble_sort(testList))
    print(testList)

# Test selection_sort
def test_selection_sort():

    testList = [1,5,8,2,4,6,98,46,45]

    assert bubble_sort(testList) == [1,2,4,5,6,8,45,46,98]
    print('')
    print(selection_sort(testList))
    print(testList)

