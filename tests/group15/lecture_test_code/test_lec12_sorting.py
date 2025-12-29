import pytest
import lec12_sorting as S


@pytest.mark.parametrize(
    "arr",
    [
        [],
        [1],
        [2, 1],
        [1, 2, 3],
        [3, 2, 1],
        [5, -1, 3, 3, 0, -1],
        [2, 2, 2, 2],
    ],
)
def test_bubble_sort_returns_sorted_and_mutates(arr, capsys):
    a = arr[:]
    out = S.bubble_sort(a)
    _ = capsys.readouterr().out
    assert out == sorted(arr)
    assert a == sorted(arr)
    assert out is a


@pytest.mark.parametrize(
    "arr",
    [
        [],
        [1],
        [2, 1],
        [1, 2, 3],
        [3, 2, 1],
        [5, -1, 3, 3, 0, -1],
        [2, 2, 2, 2],
    ],
)
def test_selection_sort_inplace_and_prints(arr, capsys):
    a = arr[:]
    ret = S.selection_sort(a)
    out = capsys.readouterr().out
    assert ret is None
    assert a == sorted(arr)
    assert "selection sort:" in out or arr == []


@pytest.mark.parametrize(
    "left,right,expected",
    [
        ([], [], []),
        ([1], [], [1]),
        ([], [1], [1]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 2], [2, 2, 3], [1, 2, 2, 2, 2, 3]),
        ([-3, -1, 2], [-2, 0, 1], [-3, -2, -1, 0, 1, 2]),
    ],
)
def test_merge_print_version(left, right, expected, capsys):
    out = S.merge(left, right)
    _ = capsys.readouterr().out
    assert out == expected


@pytest.mark.parametrize(
    "arr",
    [
        [],
        [1],
        [2, 1],
        [1, 2, 3],
        [3, 2, 1],
        [5, -1, 3, 3, 0, -1],
        [2, 2, 2, 2],
    ],
)
def test_merge_sort_print_version(arr, capsys):
    a = arr[:]
    out = S.merge_sort(a)
    printed = capsys.readouterr().out
    assert out == sorted(arr)
    assert a == arr
    assert "merge sort:" in printed or arr == []


@pytest.mark.parametrize(
    "arr",
    [
        [],
        [1],
        [2, 1],
        [1, 2, 3],
        [3, 2, 1],
        [5, -1, 3, 3, 0, -1],
        [2, 2, 2, 2],
    ],
)
def test_bubble_sort_np_silent_and_sorted(arr, capsys):
    a = arr[:]
    out = S.bubble_sort_np(a)
    printed = capsys.readouterr().out
    assert out == sorted(arr)
    assert a == sorted(arr)
    assert printed.strip() == ""


@pytest.mark.parametrize(
    "arr",
    [
        [],
        [1],
        [2, 1],
        [1, 2, 3],
        [3, 2, 1],
        [5, -1, 3, 3, 0, -1],
        [2, 2, 2, 2],
    ],
)
def test_selection_sort_np_inplace_and_silent(arr, capsys):
    a = arr[:]
    ret = S.selection_sort_np(a)
    printed = capsys.readouterr().out
    assert ret is None
    assert a == sorted(arr)
    assert printed.strip() == ""


@pytest.mark.parametrize(
    "left,right,expected",
    [
        ([], [], []),
        ([1], [], [1]),
        ([], [1], [1]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 2], [2, 2, 3], [1, 2, 2, 2, 2, 3]),
        ([-3, -1, 2], [-2, 0, 1], [-3, -2, -1, 0, 1, 2]),
    ],
)
def test_merge_np(left, right, expected, capsys):
    out = S.merge_np(left, right)
    printed = capsys.readouterr().out
    assert out == expected
    assert printed.strip() == ""


@pytest.mark.parametrize(
    "arr",
    [
        [],
        [1],
        [2, 1],
        [1, 2, 3],
        [3, 2, 1],
        [5, -1, 3, 3, 0, -1],
        [2, 2, 2, 2],
    ],
)
def test_merge_sort_np(arr, capsys):
    a = arr[:]
    out = S.merge_sort_np(a)
    printed = capsys.readouterr().out
    assert out == sorted(arr)
    assert a == arr
    assert printed.strip() == ""
