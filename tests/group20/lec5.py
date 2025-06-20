def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums) if nums else 0
    max_n = max(nums) if nums else 0
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

def list_operations(L1, L2):
    result = {}
    result['concat'] = L1 + L2
    L1_copy = L1[:]
    L1_copy.extend([0, 6])
    result['extend'] = L1_copy
    L = [2, 1, 3, 6, 3, 7, 0]
    L_copy = L[:]
    L_copy.remove(2)
    L_copy.remove(3)
    del L_copy[1]
    result['remove_del'] = L_copy
    result['pop'] = L.pop()
    s = "I<3 cs"
    result['string_to_list'] = list(s)
    result['split'] = s.split('<')
    L_str = ['a', 'b', 'c']
    result['join'] = ''.join(L_str)
    result['join_with_underscore'] = '_'.join(L_str)
    return result

def sort_lists(L):
    sorted_L = sorted(L)
    L_copy = L[:]
    L_copy.sort()
    result = {'sorted': sorted_L, 'sort': L_copy}
    L_copy.reverse()
    result['reverse'] = L_copy
    return result

def demonstrate_aliasing(L):
    alias = L
    alias.append('pink')
    return {'original': L, 'aliased': alias}

def demonstrate_cloning(L):
    clone = L[:]
    clone.append('black')
    return {'original': L, 'cloned': clone}

def nested_list_operations(base_list, append_list):
    nested = [base_list]
    nested.append(append_list)
    append_list.append('pink')
    return nested

def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
    return L1

def remove_dups_new(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
    return L1
