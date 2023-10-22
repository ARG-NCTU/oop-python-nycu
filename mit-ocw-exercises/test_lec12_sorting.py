from lec12_sorting import *
import pytest
import time
import random

@pytest.fixture
def int_list_factory_shuffled():
    def _int_list(n):
        data = list(range(n))
        random.shuffle(data)
        return data
    return _int_list


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
    assert selection_sort(testList) == [1,2,3,5,6,7,13,18,25]

    print('')
    print(selection_sort(testList))
    print(testList)

# Test merge_sort
def test_merge_sort():

    testList = [1,3,5,7,2,6,25,18,13]
    assert merge_sort(testList) == [1,2,3,5,6,7,13,18,25]
    
    print('')
    print(merge_sort(testList))
    print(testList)


# Test bubble_sort_time
def test_bubble_sort(int_list_factory_shuffled):
    testList1 = int_list_factory_shuffled(10)
    testList2 = int_list_factory_shuffled(100)
    testList3 = int_list_factory_shuffled(10000)
    start = time.time()
    bubble_sort(testList1)
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for bubble sort with 10 elements shuffled list: {end-start:.2e}')
    start = time.time()
    bubble_sort(testList2)                                                   
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for bubble sort with 100 elements shuffled list: {end-start:.2e}')
    start = time.time()
    bubble_sort(testList3)                                                   
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for bubble sort with 10000 elements shuffled list: {end-start:.2e}') 

# Test selection_sort_time
def test_selection_sort(int_list_factory_shuffled):
    testList1 = int_list_factory_shuffled(10)
    testList2 = int_list_factory_shuffled(100)                                
    testList3 = int_list_factory_shuffled(10000)        
    start = time.time()
    selection_sort(testList1)                                                   
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for selection sort with 10 elements shuffled list: {end-start:.2e}')                  
    start = time.time()
    selection_sort(testList2)                                                   
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for selection sort with 100 elements shuffled list: {end-start:.2e}')
    start = time.time()
    selection_sort(testList3)                                                   
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for selection sort with 10000 elements shuffled list: {end-start:.2e}')


# Test merge_sort_time
def test_merge_sort(int_list_factory_shuffled):
    testList1 = int_list_factory_shuffled(10)
    testList2 = int_list_factory_shuffled(100)                                
    testList3 = int_list_factory_shuffled(10000)        
    start = time.time()
    merge_sort(testList1)                                                   
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for merge sort with 10 elements shuffled list: {end-start:.2e}')                  
    start = time.time()
    merge_sort(testList2)                                                   
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for merge sort with 100 elements shuffled list: {end-start:.2e}')
    start = time.time()
    merge_sort(testList3)                                                   
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for merge sort with 10000 elements shuffled list: {end-start:.2e}')


