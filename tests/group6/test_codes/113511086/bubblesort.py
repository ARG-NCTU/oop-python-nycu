def bubble_sort(lst):
    """
    Sorts a list of numbers in ascending order using bubble sort.

    Args:
        lst (list): A list of comparable elements

    Returns:
        list: A sorted list
    """
    # Make a copy so we don't modify the original list
    result = lst.copy()
    n = len(result)

    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                # Swap
                result[j], result[j + 1] = result[j + 1], result[j]

    return result

