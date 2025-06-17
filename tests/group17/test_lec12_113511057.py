
import lec_12.py as lec12
import pytest
import time
import random
# Test bubble_sort
def test_bubble_sort():
    testList = [1,5,8,2,4,6,98,46,45]
    assert lec12.bubble_sort(testList) == [1,2,4,5,6,8,45,46,98]


# Test selection_sort
def test_selection_sort():

    testList = [1,5,8,2,4,6,98,46,45]

    assert lec12.bubble_sort(testList) == [1,2,4,5,6,8,45,46,98]
  

