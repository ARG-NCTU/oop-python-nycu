import pytest

def bubble_sort(L):
    swap = False
    while not swap:
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L


def test_bubble_sort():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
def test_bubble_sort_empty():
    assert bubble_sort([]) == []
def test_bubble_sort_single_element():
    assert bubble_sort([42]) == [42]
def test_bubble_sort_duplicates():
    assert bubble_sort([3, 1, 2, 2, 3]) == [1, 2, 2, 3, 3]
