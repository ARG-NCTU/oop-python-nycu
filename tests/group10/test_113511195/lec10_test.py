import add_path
import lec10_complexity_part1 as lec10
import pytest

def test_linear_search():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert lec10.linear_search(L, 1) is True
    assert lec10.linear_search(L, 27) is True
    assert lec10.linear_search(L, 9) is True

    L = [1, 3, 4, 5, 9, 18, 27]
    assert lec10.linear_search(L, 0) is False
    assert lec10.linear_search(L, 2) is False
    assert lec10.linear_search(L, 28) is False

    assert lec10.linear_search([], 1) is False

    L = [1, 2, 2, 2, 3]
    assert lec10.linear_search(L, 2) is True

    L = [5, 1, 9, 3]
    assert lec10.linear_search(L, 9) is True
    assert lec10.linear_search(L, 2) is False