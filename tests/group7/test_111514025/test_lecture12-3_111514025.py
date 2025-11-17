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
    
def test_merge_sort():
    print("\n---- merge sort tests ----")
    lst = [38, 27, 43, 3, 9, 82, 10]
    sorted_lst = merge_sort(lst)
    print("Sorted list:", sorted_lst)
    assert sorted_lst == [3, 9, 10, 27, 38, 43, 82]