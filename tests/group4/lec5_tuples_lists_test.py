import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import add_path
from src.mit_ocw_exercises.lec5_tuples_lists import quotient_and_remainder, get_data, sum_elem_method1, sum_elem_method2, remove_dups, remove_dups_new

def test_quotient_and_remainder():
    (quot, rem) = quotient_and_remainder(5,3)
    assert quot == 1
    assert rem == 2
    (quot, rem) = quotient_and_remainder(10000,40)
    assert quot == 250
    assert rem == 0
    (quot, rem) = quotient_and_remainder(0,5)
    assert quot == 0
    assert rem == 0
    (quot, rem) = quotient_and_remainder(15646,15)
    assert quot == 1043
    assert rem == 1

def test_get_data():
    anime = ((4,"cat"),
              (100, "tiger"),
              (50,"monkey"), 
              (70,"penguin"), 
              (500,"elephant"))    
    (min, max, num_) = get_data(anime)
    assert min == 4
    assert max == 500
    assert num_ == 5

def test_sum_elem_methods():
    L = [1, 2, 3, 4, 5]
    assert sum_elem_method1(L) == 15
    assert sum_elem_method2(L) == 15
    L = [-59, 8888, -605, 42]
    assert sum_elem_method1(L) == 8266
    assert sum_elem_method2(L) == 8266
    L = []
    assert sum_elem_method1(L) == 0
    assert sum_elem_method2(L) == 0

def test_remove_dups():
    L1 = [1, 2, 3, 2, 1, 4, 5]
    L2 = [1, 2, 3, 5]
    remove_dups(L1, L2)
    assert  L1== [2, 2, 4]
    L1 = [1, 2, 3, 2, 1, 4, 5]
    L2 = [1, 2, 3, 5]
    remove_dups_new(L1, L2)
    assert  L1== [4]
    L1 = ['a', 'b', 'a', 'c', 'b', 'd']
    L2 = ['d', 't', 'x', 'a', 'c']
    remove_dups(L1, L2)
    assert L1 == ['b', 'c', 'b']
    L1 = ['a', 'b', 'a', 'c', 'b', 'd']
    L2 = ['d', 't', 'x', 'a', 'c']
    remove_dups_new(L1, L2)
    assert L1 == ['b', 'b']
    L1 = [22626, 313, 42, 22626, 7, 42, 313]
    L2 = []
    remove_dups(L1, L2)
    assert L1 == [22626, 313, 42, 22626, 7, 42, 313]
    remove_dups_new(L1, L2)
    assert L1 == [22626, 313, 42, 22626, 7, 42, 313]
