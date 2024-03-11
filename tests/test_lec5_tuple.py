import add_path
import mit_ocw_exercises.lec5_tuples_lists as lec5
import pytest

def test_calculate_average(numbers):
    '''
    calculate_average(): calculate average of numbers

    Parameter:
        numbers: a list of numbers (type:list)

    Return:
        the average of numbers
    '''

    total = 0
    for i in range(len(numbers)):
        breakpoint()
        total += numbers[i]
    average = total / len(numbers)
    return average

def test_gcd(a, b):
    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a
    if (big % small == 0):
        return small
    else:
        return gcd(small, big % small)

def test_rev_list(L):
   """
   input: L, a list
   Modifies L such that its elements are in reverse order
   returns: nothing
   """
   for i in range(len(L)//2):
        j = len(L) - i - 1
        # breakpoint()
        temp = L[i]
        # breakpoint()
        L[i] = L[j]
        # breakpoint()
        L[j] = temp
        breakpoint()
   return L

def test_calculate_average()
numbers = [5, 10, 15, 20, 25, 30]
average_result = calculate_average(numbers)

print("Average:", average_result)
breakpoint()

assert average_result == 17.5

def test_calculate_gcd()
assert gcd(72, 96) == 24

def test_calculate_rev_list()
L = [1,2,3,4]
assert rev_list(L) == [4,3,2,1]

# please write a test for quotient_and_remainder function
def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(20, 6) == (3, 2)
    assert lec5.quotient_and_remainder(20, 7) == (2, 6)
    assert lec5.quotient_and_remainder(20, 8) == (2, 4)
    assert lec5.quotient_and_remainder(20, 9) == (2, 2)
    assert lec5.quotient_and_remainder(20, 10) == (2, 0)



