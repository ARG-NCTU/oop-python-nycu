import pytest
"""
This module contains unit tests for the `minkowskiDist` function from the `lec11_intro_to_ML` module.

Functions:
    test_minkowskiDist(): Tests the `minkowskiDist` function with various inputs and expected outputs.

Usage:
    Run this module with pytest to execute the tests.
"""
from lec11_intro_to_ML import minkowskiDist as g3_minkowskiDist

def test_minkowskiDist():
    assert g3_minkowskiDist([0, 0], [0, 0], 1) == 0
    assert g3_minkowskiDist([0, 0], [0, 0], 2) == 0
    assert g3_minkowskiDist([0, 0], [0, 0], 3) == 0
    assert g3_minkowskiDist([0, 0], [1, 1], 1) == 2
    assert g3_minkowskiDist([0, 0], [1, 1], 2) == 2**0.5
    assert g3_minkowskiDist([0, 0], [1, 1], 3) == 2**0.3333333333333333
    assert g3_minkowskiDist([0, 0], [3, 4], 1) == 7
    assert g3_minkowskiDist([0, 0], [3, 4], 2) == 5
    assert g3_minkowskiDist([0, 0], [3, 4], 3) == 91**0.3333333333333333
    assert g3_minkowskiDist([0, 0], [3, 4], 4) == 337**0.25
    assert g3_minkowskiDist([0, 0], [3, 4], 5) == 1267**0.2
    assert g3_minkowskiDist([0, 0], [3, 4], 6) == 4825**0.16666666666666666
if __name__ == "__main__":
    pytest.main()