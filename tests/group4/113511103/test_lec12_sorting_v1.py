# lec12 bubble sort 演算法
def bubble_sort(L):
    L = L.copy()  # 保留原始輸入
    for i in range(len(L)):
        for j in range(0, len(L)-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L

# ====================== 測試區 ======================

def test_empty_list():
    assert bubble_sort([]) == []

def test_single_element():
    assert bubble_sort([42]) == [42]

def test_already_sorted():
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_reverse_sorted():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_all_identical():
    assert bubble_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

def test_with_duplicates():
    assert bubble_sort([4, 1, 3, 2, 4]) == [1, 2, 3, 4, 4]

def test_with_negatives():
    assert bubble_sort([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]

def test_with_floats():
    assert bubble_sort([1.5, 2.1, 0.3, 1.5]) == [0.3, 1.5, 1.5, 2.1]

def test_mixed_types_integers_floats():
    assert bubble_sort([3, 1.1, 2, 1.1]) == [1.1, 1.1, 2, 3]

def test_large_random_list():
    import random
    data = random.sample(range(-1000, 1000), 100)
    assert bubble_sort(data) == sorted(data)