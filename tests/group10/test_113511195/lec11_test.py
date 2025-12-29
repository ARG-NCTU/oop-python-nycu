import lec_code.lec11 as lec11
import pytest

def test_bisect_search1_empty_list_raises_indexerror():
    # Lecture code prints L[0] and L[-1] before checking empty -> IndexError
    with pytest.raises(IndexError):
        lec11.bisect_search1([], 0)

@pytest.mark.parametrize(
    "L,e,expected",
    [
        ([0], 0, True),
        ([0], 1, False),
        ([0, 1, 2, 3, 4], 0, True),
        ([0, 1, 2, 3, 4], 4, True),
        ([0, 1, 2, 3, 4], 2, True),
        ([0, 1, 2, 3, 4], 5, False),
        ([0, 1, 2, 3, 4], -1, False),
        (list(range(100)), 76, True),
        (list(range(100)), 100, False),
    ],
)
def test_bisect_search1_results_nonempty(L, e, expected, capsys):
    result = lec11.bisect_search1(L, e)
    capsys.readouterr()
    assert result is expected