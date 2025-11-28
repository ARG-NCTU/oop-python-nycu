# test_lecture12-3_111514025.py
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

print(merge_sort([8, 7, 3, 3, 1, 0, 10]))
def test_merge_sort():
    print("\n---- merge sort tests ----")
    lst = [8, 7, 3, 3, 1, 0, 10]
    sorted_lst = merge_sort(lst)
    print("Sorted list:", sorted_lst)
    assert sorted_lst == [0, 1, 3, 3, 7, 8, 10]