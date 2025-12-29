import pytest

from lec7_debug_except import rev_list

def test_rev_list():
    L = [1, 2]
    rev_list(L)
    assert L == [2, 1]
