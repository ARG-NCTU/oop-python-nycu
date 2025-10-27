import lec_test_codes.add_path
import mit_ocw_exercises.lec11_complexity_part2 as l11
import pytest


#############################
# Test bisect_search1
#############################
def test_bisect_search1_found():
    L = list(range(0, 100))
    assert l11.bisect_search1(L, 0) is True
    assert l11.bisect_search1(L, 50) is True
    assert l11.bisect_search1(L, 99) is True


def test_bisect_search1_not_found():
    L = list(range(0, 100))
    assert l11.bisect_search1(L, -1) is False
    assert l11.bisect_search1(L, 100) is False
    with pytest.raises(IndexError) as e:
        l11.bisect_search1([], 5)
    assert "list index out of range" in str(e.value)