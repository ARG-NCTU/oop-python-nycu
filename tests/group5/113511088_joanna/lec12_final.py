def bubble_sort_np(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j - 1] > L[j]:
                L[j], L[j - 1] = L[j - 1], L[j]
                swap = False
    return L

def selection_sort_np(L):
    for suffixSt in range(len(L)):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
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
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_np(L):
    if len(L) < 2:
        return L[:]
    mid = len(L) // 2
    left = merge_sort_np(L[:mid])
    right = merge_sort_np(L[mid:])
    return merge_np(left, right)
