import add_path
import mit_ocw_exercises.lec7_debug_except as l7 # type: ignore
import pytest

import math

def test_rev_list():

    L = [1, 2, 3, 4]
    l7.rev_list(L)
    assert L == [4, 3, 2, 1]

    L = []
    l7.rev_list(L)
    assert L == []

    L = [42]
    l7.rev_list(L)
    assert L == [42]

    L = ['r', 'a', 'c', 'e', 'a', 'c', 'a', 'r']
    l7.rev_list(L)
    assert L == ['r', 'a', 'c', 'a', 'e', 'c', 'a', 'r']