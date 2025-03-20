import add_path
import pytest
import mit_ocw_exercises.lec6_recursion_dictionaries as lec6

def test_fibonacci():
    assert lec6.fibonacci(0) == 0
    assert lec6.fibonacci(1) == 1
    assert lec6.fibonacci(2) == 1
    assert lec6.fibonacci(3) == 2
    assert lec6.fibonacci(4) == 3
    assert lec6.fibonacci(5) == 5
    assert lec6.fibonacci(6) == 8
    assert lec6.fibonacci(7) == 13
    assert lec6.fibonacci(8) == 21
    assert lec6.fibonacci(9) == 34
    assert lec6.fibonacci(10) == 55
    assert lec6.fibonacci(11) == 89
    assert lec6.fibonacci(12) == 144
    assert lec6.fibonacci(13) == 233
    assert lec6.fibonacci(14) == 377
    assert lec6.fibonacci(15) == 61

def test_is_palindrome():
    assert lec6.is_palindrome('eve') == True
    assert lec6.is_palindrome('Able was I saw Elba') == True
    assert lec6.is_palindrome('Is this a palindrome') == False
    assert lec6.is_palindrome("HeleH") == True
    assert lec6.is_palindrome("redmeat") == False