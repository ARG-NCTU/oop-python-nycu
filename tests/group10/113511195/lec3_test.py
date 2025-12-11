import add_path
import lec3_strings_algos as lec3 # type: ignore
import pytest
import random

def test_is_palindrome():
    assert lec3.is_palindrome("racecar") == True
    assert lec3.is_palindrome("Racecar") == True
    assert lec3.is_palindrome("hello") == False
    assert lec3.is_palindrome("A man a plan a canal Panama") == False
    assert lec3.is_palindrome("AmanaplanacanalPanama") == True
    assert lec3.is_palindrome("") == True