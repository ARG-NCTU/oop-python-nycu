import add_path
import lec7_debug_except as lec7 # type: ignore
import pytest
import random

def test_rev_list():
    L = [1, 2, 3, 4, 5, 6]
    lec7.rev_list(L)
    assert L == [6, 5, 4, 3, 2, 1]
    L = ['q', 'w', 'e', 'r', 't', 'y']
    lec7.rev_list(L)
    assert L == ['y', 't', 'r', 'e', 'w', 'q']