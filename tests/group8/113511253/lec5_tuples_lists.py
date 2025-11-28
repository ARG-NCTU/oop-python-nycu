def odd_tuples(a_tup):
    """Returns a new tuple with elements at odd indices (0, 2, 4...)"""
    return a_tup[0::2]

def sum_list(a_list):
    """Recursive sum of a list"""
    if len(a_list) == 0:
        return 0
    return a_list[0] + sum_list(a_list[1:])
