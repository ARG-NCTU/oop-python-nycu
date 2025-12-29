import lec_code.lec12 as lec12
import pytest


@pytest.mark.parametrize(
    "L",
    [
        [],
        [1],
        [2, 1],
        [3, 1, 2],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [2, 3, 2, 1, 3, 1],      # duplicates
        [-1, 0, -3, 2, 1],       # negatives
    ],
)
def test_bubble_sort_sorts_correctly(L, capsys):
    original = L[:]  # bubble_sort mutates input; keep copy
    out = lec12.bubble_sort(L)
    capsys.readouterr()  # flush prints
    assert out == sorted(original)
    # bubble_sort returns the same list object it mutated
    assert out is L