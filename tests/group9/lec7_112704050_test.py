import pytest
from lec7_112704050 import rev_list

def test_rev_list():

    L = [1,2,3,4]
    rev_list(L)
    expected = [4,3,2,1]
    assert L == expected

    L = [1]
    rev_list(L)
    expected = [1]
    assert L == expected

    L = [-11,2,32,4]
    rev_list(L)
    expected = [4,32,2,-11]
    assert L == expected

    L = [0,0,0,0]
    rev_list(L)
    expected = [0,0,0,0]
    assert L == expected

    L = [-1,-2,-3,-10]
    rev_list(L)
    expected = [-10,-3,-2,-1]
    assert L == expected

import pytest
from lec7_112704050 import primes_list,find_primes

def test_find_primes():

    result = find_primes(2)
    assert result == 2 
    result = find_primes(3)
    assert result == 3 
    result = find_primes(5)
    assert result == 5 
    result = find_primes(5)
    assert result == 5 

    result = find_primes(1)
    assert result == False
    result = find_primes(-3)
    assert result == False
    result = find_primes(10)
    assert result == False 
    result = find_primes(20)
    assert result == False 
    result = find_primes(0)
    assert result == False 

def test_primes_list():
    result = primes_list(2)
    expected = [2]
    assert result == expected
    result = primes_list(3)
    expected = [2, 3]
    assert result == expected
    result = primes_list(4)
    expected = [2, 3]
    assert result == expected
    result = primes_list(-1)
    expected = []
    assert result == expected
    result = primes_list(53)
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    assert result == expected
    result = primes_list(54)
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    assert result == expected
    result = primes_list(1)
    expected = []
    assert result == expected
    result = primes_list(0)
    expected = []
    assert result == expected


import pytest
from lec7_112704050 import calculate_stat

def test_calculate_stat_output():
    test_grades = [
        [['peter', 'parker'], [80.0, 70.0, 85.0]],
        [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
        [['captain', 'america'], [80.0, 70.0, 96.0]],
        [['deadpool'], []],
        [["Edward", "Lee"], [100, 99, 98, 94]]
    ]

    new_list, highest = calculate_stat(test_grades)

    # 檢查 new_list 長度
    assert len(new_list) == 5

    # 檢查 Edward Lee 的平均是否正確
    edward_avg = next((x[1] for x in new_list if x[0] == ["Edward", "Lee"]), None)
    assert edward_avg == pytest.approx(97.75, rel=1e-2)

    # 檢查最高分是否正確
    assert highest == pytest.approx(97.75, rel=1e-2)

    # 檢查 deadpool 的平均是否為 False
    deadpool_avg = next((x[1] for x in new_list if x[0] == ["deadpool"]), None)
    assert deadpool_avg == False











