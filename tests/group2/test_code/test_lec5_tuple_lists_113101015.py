import pytest
import lec5_tuples_lists as lec5
import math

def test_quoNrem():
    assert lec5.quotient_and_remainder(10,3) == (3,1)
    assert lec5.quotient_and_remainder(4,2) == (2,0)
    assert lec5.quotient_and_remainder(-10,3) == (-4, 2)
    try:
        assert lec5.quotient_and_remainder(10,0) == (3,1)
    except(ZeroDivisionError):
        pass

def test_getdata():
    assert lec5.get_data(((1,"a"),(2, "b"),(1,"a"),(7,"b"))) == (1,7,2)
    assert lec5.get_data(((1,"a"),(2, "b"),(1,"c"),(-7,"b"))) == (-7,2,3)
    assert lec5.get_data(((2014,"Katy"),
          (2014, "Harry"),
          (2012,"Jake"), 
          (2010,"Taylor"), 
          (2008,"Joe")) ) == (2008,2014,5)

def test_remove_dup():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    lec5.remove_dups_new(L1,L2)
    assert L1 == [3,4]
    ##
