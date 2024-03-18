import add_path
import pytest


def calculate_average(numbers):
    '''
    calculate_average(): calculate average of numbers

    Parameter:
        numbers: a list of numbers (type:list)

    Return:
        the average of numbers
    '''

    total = 0
    for i in range(len(numbers) ):
      breakpoint()
      total += numbers[i-1]
    average = total / len(numbers)
    return average
def gcd(a,b):

    '''
    gcd(): greatest common divisor
    for two or more integers, which are not all zero,
    gcd is the largest positive integer that divides each of the integers.

    Parameter:
        a, b: two positive number (type:int)

    Return:
        greatest common divisor of a, b (type:int)
    '''
    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a
    breakpoint()
    if big % small == 0:
        return small
    else:
        
        return gcd(small, big % small)
def rev_list(L):
   """
   input: L, a list
   Modifies L such that its elements are in reverse order
   returns: nothing
   """
   k=0
   for i in range(len(L)):
       k+=1
       j = len(L) - i-1
       breakpoint()
       temp =L[i]
       L[i] = L[j]
       L[j] = temp
       if k==2:
           break  


def test_calculate_average():
    numbers = [5, 10, 15, 20, 25, 30]

    average_result = calculate_average(numbers)

    print("Average:", average_result)
    assert average_result == 17.5

def test_gcd():
    





def test_rev_list():
    L=[1,2,3,4]
    rev_list(L)
    assert L == [4,3,2,1]