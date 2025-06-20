import lec5_tuples_lists as lec
import pytest

def test_quotient_and_remainder():
    assert lec.quotient_and_remainder(8,5) == (1,3)
    assert lec.quotient_and_remainder(100, 1) == (100, 0)
    print ("q&r test successful!!")

def test_get_data():
    test1 = ((1,'a'), (2, 'b'),(3, 'c'), (4, 'c') )
    assert lec.get_data(test1) == (1, 4, 3)
    print ("get data test successful!!")

if __name__ == "__main__":
    pytest.main([__file__])
    # Alternatively, you can run pytest from the command line:
    # pytest test_lec5-1.py