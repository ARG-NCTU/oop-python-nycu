import add_path
import lec10_complexity_part1 as lec10
import pytest

def test_linear_search():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert lec10.linear_search(L, 1) is True
    assert lec10.linear_search(L, 27) is True
    assert lec10.linear_search(L, 9) is True