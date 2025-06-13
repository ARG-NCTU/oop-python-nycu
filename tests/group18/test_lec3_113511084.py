import os
import sys
import pytest

sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../src'))

import mit_ocw_exercises.lec3_strings_algos as lec3

@pytest.mark.parametrize("s, expected", [
    ("racecar", True),        
    ("RaceCar", True),        
    ("hello", False),         
    ("", True),               
    ("a", True),              
    ("12321", True),          
    ("123321", True),
    ("123421", False),
    ("WasItACarOrACatISaw", True),  
    ("No lemon, no melon", False)   
])
def test_is_palindrome(s, expected):
    assert lec3.is_palindrome(s) == expected
