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










