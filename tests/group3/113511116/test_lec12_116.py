import add_path
import mit_ocw_exercises.lec12_sorting as lec12
import pytest

def test_bubble_sort():
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = lec12.bubble_sort(arr)
    assert sorted_arr == [11, 12, 22, 25, 34, 64, 90]

