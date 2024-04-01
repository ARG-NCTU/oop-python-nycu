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
    for i in range(len(numbers)):
      breakpoint()
      total += numbers[i]
    average = total / len(numbers)
    return average



def num_gcd(a,b):

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
    if big % small == 0:
        #breakpoint()
        return small
    else:
        #breakpoint()
        return num_gcd(small, big % small)



def rev_list(L):
   """
   input: L, a list
   Modifies L such that its elements are in reverse order
   returns: nothing
   """

   for i in range(len(L)//2):
       j = len(L) - i - 1
       temp = L[i]
       L[i] = L[j]
       L[j] = temp
       breakpoint()



def test_calculate_average():
	assert calculate_average([5,10,15,20,25,30])==17.5

def test_num_gcd():
	assert num_gcd(72,96)==24

def test_rev_list():
	L=[1,2,3,4]
	rev_list(L)
	assert L==[4,3,2,1]
