import lec_code.lec11 as lec11
import pytest

def test_bisect_search1_empty_list_raises_indexerror():
    # Lecture code prints L[0] and L[-1] before checking empty -> IndexError
    with pytest.raises(IndexError):
        lec11.bisect_search1([], 0)