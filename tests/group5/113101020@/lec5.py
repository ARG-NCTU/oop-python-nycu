def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums += (t[0],)
        if t[1] not in words:
            words += (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

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

def remove_dups(L1, L2):
    for e in L1[:]:
        if e in L2:
            L1.remove(e)

def remove_dups_new(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
