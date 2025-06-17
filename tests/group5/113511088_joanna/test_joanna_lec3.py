from lec3_final import *

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False

def test_find_max():
    assert find_max([1, 9, 3, 7]) == 9

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOUxyz") == 5
