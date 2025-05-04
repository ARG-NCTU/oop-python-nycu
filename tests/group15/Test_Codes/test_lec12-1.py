import lec12_sorting as lec

L = [4, 8, 3, 2, 10, 9, 1, 5, 7, 6]

def bubble_sort_test():
    assert lec.bubble_sort(L) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("bubble sort is so good!!")
bubble_sort_test()

def selection_sort_test():
    #assert lec.selection_sort(L) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    L1 = L
    lec.selection_sort(L1)
    print (L1)
    assert L1 == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("selection sort is also so good!!")
selection_sort_test()

def merge_test():
    Left = [0, 1, 2, 3, 4, 5]
    Right = [4, 6, 8, 10]
    Right2 = [10, 8, 6, 4, 3]
    print(lec.merge(Left, Right))
    assert lec.merge(Left, Right) == [0,1,2,3,4,4,5,6,8,10]
    print(lec.merge(Left, Right2))
merge_test()

def merge_sort_test():
    assert lec.merge_sort(L) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("merge sort is also very good!!")
merge_sort_test()
