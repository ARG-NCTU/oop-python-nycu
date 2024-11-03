import pytest
import add_path
import random

from mit_ocw_data_science.lec13.lecture13 import *

def test_minkowskiDist():
    assert minkowskiDist([0,0], [3,4], 2) == 5.0
    assert minkowskiDist([1,2,3], [4,5,6], 1) == 9.0
    assert minkowskiDist([1,2,3], [4,5,6], 2) == 5.196152422706632
    assert minkowskiDist([1,2,3], [4,5,6], 3) == 4.3267487109222245
