import pytest
from math import isclose

"""
This module contains unit tests for the `stdDev` function.

Functions:
    test_stdDev(): Tests the `stdDev` function with various inputs and expected outputs.

Usage:
    Run this module with pytest to execute the tests.
"""

from lec11_intro_to_ML import stdDev

def test_stdDev():
    # Test with an empty list (this should raise an error like ZeroDivisionError)
    with pytest.raises(ZeroDivisionError):
        stdDev([])

    # Test with a list of one element, standard deviation should be 0
    assert stdDev([5]) == 0

    # Test with a list of identical elements, standard deviation should be 0
    assert stdDev([3, 3, 3, 3, 3]) == 0

    # Test with a list of varying elements, comparing to known result
    assert isclose(stdDev([1, 2, 3, 4, 5]), 1.41421356237, rel_tol=1e-9)

    # Test with negative numbers
    assert isclose(stdDev([-1, -2, -3, -4, -5]), 1.41421356237, rel_tol=1e-9)

if __name__ == "__main__":
    pytest.main()
