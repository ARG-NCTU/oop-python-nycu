import pytest
#11/25 modified merge_sort

def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + '&' + str(right) + ' to ' +str(result))
    return result

def merge_sort(L):
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
    
assert merge_sort([3, 2, 1]) == [1, 2, 3]
assert merge_sort([4, 3, 1, 8, 9, 6]) == [1, 3, 4, 6, 8, 9]
assert merge_sort([2, 3, 8, 5, 7]) == [2, 3, 5, 8, 7]
assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert merge_sort([]) == []
assert merge_sort([1]) == [1]

if __name__ == '__main__':
    pytest.main()