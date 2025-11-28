import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lec2_branch_loops

def test_is_even():
    assert lec2_branch_loops.is_even(4) is True
    assert lec2_branch_loops.is_even(5) is False
    assert lec2_branch_loops.is_even(0) is True

def test_get_largest_odd():
    assert lec2_branch_loops.get_largest_odd([2, 4, 6, 7, 10, 3]) == 7
    assert lec2_branch_loops.get_largest_odd([2, 4, 6]) is None
    assert lec2_branch_loops.get_largest_odd([]) is None
