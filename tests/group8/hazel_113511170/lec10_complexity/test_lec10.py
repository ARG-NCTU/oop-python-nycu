import lec10 as lc
import pytest
import time
import random
import numpy as np

def sample_data():
    data = [6,7,8,9,10]
    return data

def test_linear_search():
    assert lc.linear_search(sample_data(), 10) == True 
    assert lc.linear_search(sample_data(), 3) == False
    assert lc.linear_search([], 3) == False
    empty_list=[]
    assert lc.linear_search(empty_list, 3) == False

def test_linear_search_int_list(sample_data):
    assert lc.linear_search(sample_data, 3) == True 
    assert lc.linear_search(sample_data, 6) == False


# create a list of integers, with parameter n for number of elements
def int_list(n):
    return list(range(n))

def test_linear_search_int_list():
    assert lc.linear_search(int_list(10), 4) == True
    assert lc.linear_search(int_list(10000), 4) == True
    #assert lec10.linear_search(int_list(100000000), 4) == True

# create a fixture factory that takes a parameter n for number of elements
@pytest.fixture
def int_list_factory():
    def _int_list(n):
        return list(range(n))
    return _int_list

#@pytest.mark.slow
def test_linear_search_int_list_factory(int_list_factory):
    assert lc.linear_search(int_list_factory(10), 4) == True
    assert lc.linear_search(int_list_factory(10000), 4) == True
    assert lc.linear_search(int_list_factory(100000000), 4) == True

# create a fixture for num_elements with parameters 10, 10000, 1000000
@pytest.fixture(params=[10, 10000, 10000000])
def num_elements(request):
    return request.param

def test_linear_search_int_list_factory_enum(int_list_factory, num_elements):
    assert lc.linear_search(int_list_factory(num_elements), 4) == True


@pytest.fixture
def sample1():
    data = [1,2,3,2,3]
    return data

# test intersection
def test_intersect(sample1):
    assert lc.intersect(sample1, [2, 3, 4]) == [2, 3]
    assert lc.intersect(sample1, [4, 5, 6]) == []
    assert lc.intersect([], [4, 5, 6]) == []

# check elements in a list via python built-in function
def test_intersect_in(sample1):
    assert 2 in sample1
    assert 4 not in sample1
