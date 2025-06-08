import add_path
import pytest
import mit_ocw_exercises.lec5_tuples_lists as lec5  

def test_quotient_and_remainder():
    # Test the quotient_and_remainder function
    dividend = 10
    divisor = 3
    result = lec5.quotient_and_remainder(dividend, divisor)
    assert isinstance(result, tuple), "Result should be a tuple"
    assert len(result) == 2, "Result should contain two elements"
    assert result[0] == 3, "Quotient should be 3"
    assert result[1] == 1, "Remainder should be 1"
def test_divide():
    # Test the divide function
    dividend = 10
    divisor = 2
    result = lec5.divide(dividend, divisor)
    assert isinstance(result, float), "Result should be a float"
    assert result == 5.0, "10 divided by 2 should be 5.0"
def test_divide_by_zero():
    # Test the divide function with zero divisor
    dividend = 10
    divisor = 0
    with pytest.raises(ZeroDivisionError):
        lec5.divide(dividend, divisor)
def test_divide_by_negative():
    # Test the divide function with negative divisor
    dividend = 10
    divisor = -2
    result = lec5.divide(dividend, divisor)
    assert isinstance(result, float), "Result should be a float"
    assert result == -5.0, "10 divided by -2 should be -5.0"
def test_divide_by_negative_zero():
    # Test the divide function with negative zero divisor
    dividend = 10
    divisor = -0
    with pytest.raises(ZeroDivisionError):
        lec5.divide(dividend, divisor)
