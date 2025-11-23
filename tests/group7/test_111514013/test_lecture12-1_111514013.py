def bubble_sort(L):
    # swap = False
    complexity = 0  # 計算複雜度
    for i in range(0, len(L)):
        for j in range(1, len(L)- i):
            complexity += 1
            if L[j-1] > L[j]:
                # swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
            print('bubble sort: ' + str(L))
    return L, complexity

print(bubble_sort([2, 31, 5, 6, 8]))
def test_bubble_sort():
    print("\n---- bubble sort tests ----")
    lst = [2, 31, 5, 6, 8]
    sorted_lst, complexity = bubble_sort(lst)
    print("Sorted list:", sorted_lst)
    assert sorted_lst == [2, 5, 6, 8, 31]
    assert complexity == 10  