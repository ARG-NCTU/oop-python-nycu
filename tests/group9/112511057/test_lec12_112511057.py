import mit_ocw_exercises.lec12_sorting as lec12


def test_sorts_and_merge():
    L = [3,1,2]
    assert lec12.bubble_sort_np(L[:]) == [1,2,3]
    assert lec12.selection_sort_np(L[:]) == [1,2,3]

    left = [1,4]
    right = [2,3]
    assert lec12.merge(left, right) == [1,2,3,4]

    assert lec12.merge_sort_np([5,2,3,1]) == [1,2,3,5]
