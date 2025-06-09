import pytest

def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        print('selection sort: ' + str(L))
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
        
def test_selection_sort():
    L = [5, 3, 8, 6, 2]
    selection_sort(L)
    assert L == [2, 3, 5, 6, 8], f"Expected [2, 3, 5, 6, 8] but got {L}"

    L = [1]
    selection_sort(L)
    assert L == [1], f"Expected [1] but got {L}"

    L = []
    selection_sort(L)
    assert L == [], f"Expected [] but got {L}"

    L = [4, 4, 4]
    selection_sort(L)
    assert L == [4, 4, 4], f"Expected [4, 4, 4] but got {L}"