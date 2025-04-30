def quotient_and_remainder(x, y):
    return (x // y, x % y)

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    return (min(nums), max(nums), len(words))

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

