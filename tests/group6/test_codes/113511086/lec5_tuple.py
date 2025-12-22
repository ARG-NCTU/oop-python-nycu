def quotient_and_remainder(x, y):
    """
    Returns the quotient and remainder of x divided by y.
    """
    return (x // y, x % y)


def sum_elem_method1(lst):
    """
    Sums elements of a list using indexing.
    """
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total


def sum_elem_method2(lst):
    """
    Sums elements of a list by iterating over elements.
    """
    total = 0
    for elem in lst:
        total += elem
    return total
