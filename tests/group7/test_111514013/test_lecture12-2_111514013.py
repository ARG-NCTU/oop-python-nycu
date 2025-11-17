def selection_sort(L):
    suffixSt = 0
    complexity = 0  # 計算複雜度
    while suffixSt != len(L):
        print('selection sort: ' + str(L))
        for i in range(suffixSt, len(L)):
            complexity += 1
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1

    return L, complexity

print(selection_sort([4, 2, 2, 22, 61]))

def test_selection_sort():
    print("\n---- selection sort tests ----")
    lst = [4, 2, 2, 22, 61]
    sorted_lst, complexity = selection_sort(lst)
    print("Sorted list:", sorted_lst)
    assert sorted_lst == [2, 2, 4, 22, 61]
    assert complexity == 15  # 計算實際比較次數