import pytest

def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        print('selection sort: ' + str(L))
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
        
assert selection_sort([3, 2, 1]) == [1, 2, 3]
assert selection_sort([4, 3, 1, 8, 9, 6]) == [1, 3, 4, 6, 8, 9]
assert selection_sort([2, 3, 8, 5, 7]) == [2, 3, 5, 8, 7]
assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert selection_sort([]) == []
assert selection_sort([1]) == [1]

if __name__ == '__main__':
    pytest.main()