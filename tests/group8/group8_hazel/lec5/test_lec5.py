#########################
## EXAMPLE: returning a tuple
#########################
import lec5
import pytest

def test_quotient_and_remainder():
    """
    Function that returns the quotient and remainder of two numbers
    x: int, y: int returns: tuple (quotient, remainder)

    """
    assert lec5.quotient_and_remainder(168,8)==(21,0)
    assert lec5.quotient_and_remainder(91,11)==(8,3)

#########################
## EXAMPLE: iterating over tuples
#########################
def test_get_data():
    """
    aTuple, tuple of tuples (int, string)
    Extracts all integers from aTuple and sets 
    them as elements in a new tuple. 
    Extracts all unique strings from from aTuple 
    and sets them as elements in a new tuple.
    Returns a tuple of the minimum integer, the
    maximum integer, and the number of unique strings
    """
    test = ((1,"a"),(2, "b"),
        (1,"a"),(7,"b"))
    assert lec5.get_data(test)==(1,7,2)
    tswift = ((2014,"Katy"),
          (2014, "Harry"),
          (2012,"Jake"), 
          (2010,"Taylor"), 
          (2008,"Joe"))   
    assert lec5.get_data(tswift)==(2008,2014,5)

#########################
## EXAMPLE: sum of elements in a list
#########################
def test_sum_elem_method1():
    L=[1,2,3,4]
    assert lec5.sum_elem_method1(L)==10
  
def test_sum_elem_method2():
    L=[1,2,3,4]
    assert lec5.sum_elem_method2(L)==10

