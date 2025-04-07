#import add_path
#import mit_ocw_exercises.lec5_tuples_lists as lec5  
import practice.lec5_tuples_lists as lec5
import pytest
def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(5,3) == (1,2)
    assert lec5.quotient_and_remainder(5,2) == (2,1)
    assert lec5.quotient_and_remainder(10,5) == (2,0)
    assert lec5.quotient_and_remainder(10,3) == (3,1)
    assert lec5.quotient_and_remainder(10,4) == (2,2)
    assert lec5.quotient_and_remainder(10,6) == (1,4)
    assert lec5.quotient_and_remainder(10,7) == (1,3)
    assert lec5.quotient_and_remainder(10,8) == (1,2)
    assert lec5.quotient_and_remainder(10,9) == (1,1)
    assert lec5.quotient_and_remainder(10,10) == (1,0)

    try:
        lec5.quotient_and_remainder(10,0)
        
    except ZeroDivisionError as e:
        assert str(e) == "division by zero"
        