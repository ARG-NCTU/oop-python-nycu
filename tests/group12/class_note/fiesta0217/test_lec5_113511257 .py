#import add_path
import pytest
#import mit_ocw_exercises.lec5_tuples_lists as lec5  

def test_quotient_and_remainder():
    # Test the quotient_and_remainder function
    dividend = 10
    divisor = 3
    result = lec5.quotient_and_remainder(dividend, divisor)
    assert isinstance(result, tuple), "Result should be a tuple"
    assert len(result) == 2, "Result should contain two elements"
    assert result[0] == 3, "Quotient should be 3"
    assert result[1] == 1, "Remainder should be 1"
    assert lec5.quotient_and_remainder(10, 5) == (2, 0), "Quotient should be 2 and remainder should be 0 for 10 divided by 5"
