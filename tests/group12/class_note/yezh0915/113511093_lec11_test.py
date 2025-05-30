import pytest
from src.mit_ocw_exercises import lec11_complexity_part2 as lec

def test_bisect_search1_found():
    L = list(range(100))
    assert lec.bisect_search1(L, 76) is True
    assert lec.bisect_search1(L, 0) is True
    assert lec.bisect_search1(L, 99) is True

def test_bisect_search1_not_found():
    L = list(range(100))
    assert lec.bisect_search1(L, -1) is False
    assert lec.bisect_search1(L, 100) is False

