
import add_path
import mit_ocw_exercises.lec6_recursion_dictionaries as lec6
import pytest

# please write a test for fib function
def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2

# please write a test for isPalindrome function
def test_isPalindrome():
    assert lec6.isPalindrome('eve') == True
    assert lec6.isPalindrome('Able was I, ere I saw Elba') == True
    assert lec6.isPalindrome('Is this a palindrome') == False
