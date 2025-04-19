import pytest
from lec5_112704050 import bmi_counting

def test_bmi_count_health():
    result = bmi_counting()
    assert result == (True , 0)
    result = bmi_counting(57,1.74)
    assert result == (True , 0)
    result = bmi_counting(57,1.55)
    assert result == (True , 0)
    result = bmi_counting(45,1.55)
    assert result == (True , 0)
    result = bmi_counting(45,1.37)
    assert result == (True , 0)    
    result = bmi_counting(100,2.24)
    assert result == (True , 0)
    result = bmi_counting(100,2.05)
    assert result == (True , 0)

def test_bmi_count_overweight():
    result = bmi_counting(57,1.54)
    assert result == (False , 2)
    result = bmi_counting(45,1.36)
    assert result == (False , 2)   
    result = bmi_counting(100,2.04)
    assert result == (False , 2)

def test_bmi_count_thin():
    result = bmi_counting(100,2.34)
    assert result == (False , 1)
    result = bmi_counting(45,1.57)
    assert result == (False , 1)
    result = bmi_counting(57,1.77)
    assert result == (False , 1)

from lec5_112704050 import get_data

def test_get_data():
    sample_data = (
        (1, "a", 170),
        (2, "b", 199),
        (3, "b", 18),
        (4, "a", 1),
        (5, "a", 15)
    )
    expected = (5, 199, 1, 2)
    assert get_data(sample_data) == expected

    sample_data = (
        (1, "a", 195),
        (2, "b", 196),
        (3, "c", 197),
        (4, "d", 199),
        (5, "e", 198)
    )
    expected = (5, 199, 195, 5)
    assert get_data(sample_data) == expected

    sample_data = (
        (1, "a", 1),
        (2, "b", 1),
        (1, "c", 1),
        (5, "d", 1),
        (5, "e", 1)
    )
    expected = (3, 1, 1, 5)
    assert get_data(sample_data) == expected

import numpy as np
from lec5_112704050 import add,minus,multiple

def test_add():
    data = np.random.randint(0,100,10)
    result = add(data)
    expected = np.sum(data)
    assert result == expected
    data = [1,2,3,4,5,6,7,8,9,10]
    result = add(data)
    expected = 55
    assert result == expected

def test_minus():
    data = np.random.randint(0,100,10)
    result = minus(data)
    expected = -np.sum(data)
    assert result == expected
    data = [1,2,3,4,5,6,7,8,9,10]
    result = minus(data)
    expected = -55
    assert result == expected

def test_multiple():
    data = [1,2,3,4,5,6,7,8,9,10]
    result = multiple(data)
    expected = 3628800
    assert result == expected
    data = np.random.randint(0,100,10)
    result = multiple(data)
    expected = np.prod(data)
    assert result == expected

from lec5_112704050 import append_use, alot_list , sort_use, simple_copy

def test_append():
    data = ["apple", "banana", "candy"]
    result = append_use(data)
    expected = ["apple", "banana", "candy" , "pink"]
    assert result == (["apple", "banana", "candy"],expected, expected)

def test_simple_copy():
    data = ["apple", "banana", "candy"]
    result = simple_copy(data)
    expected = ["apple", "banana", "candy", "orange"]   
    assert result == (expected , ["apple", "banana", "candy"]) 

def test_sort_use():
    data = ["bpple", "canana", "aandy"]
    result = sort_use(data)
    expected = ["aandy", "bpple", "canana"]
    assert result == (None , expected)

def test_alot_list():
    data = ["apple", "banana", "candy"]
    result = alot_list(data)
    expected1 = [["apple", "banana", "candy"],["red"]]
    expected2 = [["apple", "banana", "candy"],["red", "pink"]]
    assert result == (expected1, expected2)

import pytest
from lec5_112704050 import present_or_not,present_or_not_new

def test_present_or_not():
    all = ["Alice" , "Bandy", "Cindy", "Diago", "Edward", "Fred"]
    absense = ["Alice","Bandy" ,"Diago","Cindy"]     
    result = ['Bandy', 'Diago', 'Edward', 'Fred']
    assert result == present_or_not(all,absense) 
    all = ["1","2","3","4","5","6","7"]  
    absense = ["1","2","5"]
    result = ['2', '3', '4', '6', '7']
    assert result == present_or_not(all,absense) 

def test_present_or_not_new():
    all = ["Alice" , "Bandy", "Cindy", "Diago", "Edward", "Fred"]
    absense = ["Alice","Bandy" ,"Diago","Cindy"]     
    result = ['Edward', 'Fred']
    assert result == present_or_not_new(all,absense)   
    all = ["1","2","3","4","5","6","7"]  
    absense = ["1","2","5"]
    result = ['3', '4', '6', '7']
    assert result == present_or_not_new(all,absense)   
