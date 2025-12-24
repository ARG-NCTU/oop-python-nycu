def is_even(i):
    """Returns True if i is even, otherwise False"""
    return i % 2 == 0

def get_largest_odd(numbers):
    """Returns the largest odd number in the list, or None"""
    odds = [n for n in numbers if n % 2 != 0]
    if not odds:
        return None
    return max(odds)
