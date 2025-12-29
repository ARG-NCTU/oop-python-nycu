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


@pytest.mark.parametrize(
    "L",
    [
        [],
        [1],
        [2, 1],
        [3, 1, 2],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [2, 3, 2, 1, 3, 1],
        [-1, 0, -3, 2, 1],
    ],
)
def test_selection_sort_sorts_correctly(L, capsys):
    original = L[:]
    out = lec12.selection_sort(L)
    capsys.readouterr()
    assert out == sorted(original)
    assert out is L

@pytest.mark.parametrize(
    "L",
    [
        [],
        [1],
        [2, 1],
        [3, 1, 2],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [2, 3, 2, 1, 3, 1],
        [-1, 0, -3, 2, 1],
    ],
)
def test_merge_sort_sorts_correctly_and_does_not_mutate_input(L, capsys):
    original = L[:]
    out = lec12.merge_sort(L)
    capsys.readouterr()
    assert out == sorted(original)
    # merge_sort returns a new list; input should remain unchanged
    assert L == original
    assert out is not L

@pytest.mark.parametrize(
    "L",
    [
        [],
        [1],
        [2, 1],
        [3, 1, 2],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [2, 3, 2, 1, 3, 1],
        [-1, 0, -3, 2, 1],
    ],
)
def test_bubble_sort_np_sorts_correctly(L):
    original = L[:]
    out = lec12.bubble_sort_np(L)
    assert out == sorted(original)
    assert out is L  # still mutates and returns same object