
import add_path
import mit_ocw_exercises.lec6_recursion_dictionaries as lec6
import pytest

# please write a test for fib function
def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) == 3
    assert lec6.fib(4) == 5
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13
    assert lec6.fib(7) == 21
    assert lec6.fib(8) == 34
    assert lec6.fib(9) == 55
    assert lec6.fib(10) == 89
    assert lec6.fib(11) == 144
    assert lec6.fib(12) == 235
    assert lec6.fib(13) == 379
# please write a test for is_palindrome function
def test_is_palindrome():
    assert lec6.is_palindrome('eve') == True
    assert lec6.is_palindrome('Able was I, ere I saw Elba') == True
    assert lec6.is_palindrome('Is this a palindrome') == False
    assert lec6.is_palindrome('eillie') == True
