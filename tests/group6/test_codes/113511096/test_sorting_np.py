def bubble_sort_np(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L

def selection_sort_np(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
    return L

def merge_np(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort_np(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort_np(L[:middle])
        right = merge_sort_np(L[middle:])
        return merge_np(left, right)

# --- Pytest Functions ---

def test_bubble_sort_np():
    lst = [5, 3, 18, 16, 32]
    sorted_lst = bubble_sort_np(lst)
    assert sorted_lst == [3, 5, 16, 18, 32]

def test_selection_sort_np():
    lst = [64, 25, 12, 22, 11]
    sorted_lst = selection_sort_np(lst)
    assert sorted_lst == [11, 12, 22, 25, 64]

def test_merge_sort_np():
    lst = [38, 27, 43, 3, 9, 82, 10]
    sorted_lst = merge_sort_np(lst)
    assert sorted_lst == [3, 9, 10, 27, 38, 43, 82]