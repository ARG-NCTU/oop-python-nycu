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
    L = []
    lec7.rev_list(L)
    assert L == []
    L = [1]
    lec7.rev_list(L)
    assert L == [1]

def test_rev_list_generalize():
    for _ in range(100):
        length = random.randint(0, 100)
        tar = [random.randint(0, 1000) for _ in range(length)]
        expected = tar[::-1]
        lec7.rev_list(tar)
        assert tar == expected