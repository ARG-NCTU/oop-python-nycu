import random
import pytest
import math
import mit_ocw_data_science.lec4.lec4_module as lec4

def test_roll_die():
    # Test the roll_die function
    die = lec4.roll_die()
    assert die >= 1 and die <= 6, "Die roll should be between 1 and 6"

def test_roll():
    n = 15
    result = ''
    for i in range(n):
        result += str(lec4.roll_die())
    assert len(result) == n, "Result should be of length n"
