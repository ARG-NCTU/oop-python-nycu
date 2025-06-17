import pytest
from src.mit_ocw_exercises import lec6_recursion_dictionaries as lec6

def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13
def test_is_palindrome():
    assert lec6.is_palindrome('eve') is True
    assert lec6.is_palindrome('Able was I, ere I saw Elba') is True
    assert lec6.is_palindrome('Is this a palindrome') is False
    assert lec6.is_palindrome('A man, a plan, a canal, Panama') is True

