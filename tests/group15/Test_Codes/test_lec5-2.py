import lec5_tuples_lists as lec

def remove_dups_test():
    L1 = [1, 2, 3, 4, 5, 10]
    L2 = [1, 2, 3, 4]
    lec.remove_dups(L1, L2)
    assert L1 == [2, 4, 5, 10]
    print(L1, L2)
    L3 = ['a', 'ab', 'abc', 'abcd']
    L4 = ['c', 'a', 'ab', 'b']
    lec.remove_dups(L3, L4)
    assert L3 == ['ab', 'abc', 'abcd']
    print (L3, L4)
remove_dups_test()

def remove_dups_new_test():
    L1 = [1, 2, 3, 4, 5, 10]
    L2 = [1, 2, 3, 4]
    lec.remove_dups_new(L1, L2)
    assert L1 == [5, 10]
    print(L1, L2)
    L3 = ['a', 'ab', 'abc', 'abcd']
    L4 = ['c', 'a', 'ab', 'b']
    lec.remove_dups_new(L3, L4)
    assert L3 == ['abc', 'abcd']
    print (L3, L4)
remove_dups_new_test()