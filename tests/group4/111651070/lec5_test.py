## EXAMPLE: returning a tuple
def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)

def test_quotient_and_remainder():
    (quot, rem) = quotient_and_remainder(5,3)
    assert quot == 1
    assert rem == 2
    (quot, rem) = quotient_and_remainder(20,7)
    assert quot == 2
    assert rem == 6

## EXAMPLE: iterating over tuples
def get_data(aTuple):
    nums = ()    # empty tuple
    words = ()
    for t in aTuple:
        # concatenating with a singleton tuple
        nums = nums + (t[0],)
        # only add words haven't added before
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

def test_get_data():
    test = ((1,"a"),(2, "b"),
            (1,"c"),(7,"b"))
    (a, b, c) = get_data(test)
    assert a == 1
    assert b == 7
    assert c == 3
    ##########################
    test = ((2014,"Katy"),
            (2014, "Harry"),
            (2012,"Jake"),
            (2010,"Taylor"),
            (2008,"Joe"))
    (a, b, c) = get_data(test)
    assert a == 2008
    assert b == 2014
    assert c == 5

## EXAMPLE: sum of elements in a list
def sum_elem_method1(L):
  total = 0
  for i in range(len(L)):
      total += L[i]
  return total

def sum_elem_method2(L):
    total = 0
    for i in L:
        total += i
    return total

def test_sum_elem_method1():
    assert sum_elem_method1([1,2,3,4]) == 10
    assert sum_elem_method1([0,0,0]) == 0
    assert sum_elem_method1([-1,-2,-3]) == -6

def test_sum_elem_method2():
    assert sum_elem_method2([1,2,3,4]) == 10
    assert sum_elem_method2([0,0,0]) == 0
    assert sum_elem_method2([-1,-2,-3]) == -6

## EXAMPLE: various list operations
## put print(L) at different locations to see how it gets mutated
def list_concatenate(L1, L2):
    L3 = L1 + L2
    L1.extend([0,6])
    return L3, L1

def test_list_concatenate():
    L1 = [2,1,3]
    L2 = [4,5,6]
    L3, L1 = list_concatenate(L1, L2)
    assert L3 == [2, 1, 3, 4, 5, 6]
    assert L1 == [2, 1, 3, 0, 6]

def remove_element(L, n):
    L.remove(n)
    return L

def test_remove_element():
    L = [2, 1, 3, 6, 3, 7, 0]
    L = remove_element(L, 2)
    assert L == [1, 3, 6, 3, 7, 0]
    L = remove_element(L, 3)
    assert L == [1, 6, 3, 7, 0]   # only removes the first 3
    L = remove_element(L, 6)
    assert L == [1, 3, 7, 0]
    del(L[2])
    assert L == [1, 3, 0]
    assert L.pop() == 0

def split_and_join(s, sign, L):
    s1 = s.split(sign)
    s2 = sign.join(L)
    return s1, s2

def test_split_and_join():
    s = "I<3 cs"
    assert list(s) == ['I', '<', '3', ' ', 'c', 's']
    s1, s2 = split_and_join(s, '<', ['a', 'b', 'c'])
    assert s1 == ['I', '3 cs']
    assert s2 == 'a<b<c'

def test_sort_and_reverse():
    L = [9, 6, 0, 3]
    L.sort()
    assert L == [0, 3, 6, 9]
    L.reverse()
    assert L == [9, 6, 3, 0]

## EXAMPLE: aliasing
def test_append():
    warm = ['red', 'yellow', 'orange']
    hot = warm
    hot.append('pink')
    assert hot == ['red', 'yellow', 'orange', 'pink']
    assert warm == ['red', 'yellow', 'orange', 'pink']

## EXAMPLE: cloning
def test_clone():
    cool = ['blue', 'green', 'grey']
    chill = cool[:]
    chill.append('black')
    assert chill == ['blue', 'green', 'grey', 'black']
    assert cool == ['blue', 'green', 'grey']

## EXAMPLE: sorting with/without mutation
def test_string_sort():
    warm = ['red', 'yellow', 'orange']
    assert warm == ['red', 'yellow', 'orange']
    sorted_warm = sorted(warm) # return
    assert sorted_warm == ['orange', 'red', 'yellow']
    assert warm == ['red', 'yellow', 'orange']
    warm = ['red', 'yellow', 'orange']
    sorted_warm = warm.sort() # change directly
    assert sorted_warm == None
    assert warm == ['orange', 'red', 'yellow']

## EXAMPLE: lists of lists of lists...
def test_lists_of_lists():
    warm = ['yellow', 'orange']
    hot = ['red']
    brightcolors = [warm]
    brightcolors.append(hot)
    assert brightcolors == [['yellow', 'orange'], ['red']]
    hot.append('pink')
    assert hot == ['red', 'pink']
    assert brightcolors == [['yellow', 'orange'], ['red', 'pink']] # 只有改hot但brightcolors一樣會被改

## EXAMPLE: mutating a list while iterating over it
def remove_dups_in_L1(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e) # 第二次迴圈進行時，L1的第一個element已經被刪掉了，因此當前會從3開始檢查，有2的話才會刪除

def remove_dups_new(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

def test_remove_dups_in_L1():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    remove_dups_in_L1(L1, L2)
    assert L1 == [2, 3, 4] # 2還在
    assert L2 == [1, 2, 5, 6]

def test_remove_dups_new():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    remove_dups_new(L1, L2)
    assert L1 == [3, 4] # 2被刪掉了
    assert L2 == [1, 2, 5, 6]

## EXERCISE: Test yourself by predicting what the output is and
##           what gets mutated then check with the Python Tutor
def test_exercise():
    cool = ['blue', 'green']
    warm = ['red', 'yellow', 'orange']
    colors1 = [cool]
    assert colors1 == [['blue', 'green']]
    colors1.append(warm) # 改warm會連帶改到colors1
    assert colors1 == [['blue', 'green'], ['red', 'yellow', 'orange']]
    warm.remove('red')
    assert warm == ['yellow', 'orange']
    assert colors1 == [['blue', 'green'], ['yellow', 'orange']]
    flat = cool + warm # 改warm不會連帶影響到flat
    assert flat == ['blue', 'green', 'yellow', 'orange']
    flat.sort()
    assert flat == ['blue', 'green', 'orange', 'yellow']
    new_flat = sorted(flat, reverse = True)
    assert new_flat == ['yellow', 'orange', 'green', 'blue']
    cool[1] = 'black'
    assert cool == ['blue', 'black']
    assert flat == ['blue', 'green', 'orange', 'yellow']