import lec6_recursion_dictionaries as lec
import pytest

def test_fib():
    assert lec.fib(0) == 1
    assert lec.fib(1) == 1
    assert lec.fib(2) == 2
    assert lec.fib(3) == 3
    assert lec.fib(4) == 5
    assert lec.fib(10) == 89
    print (lec.fib(20))
test_fib()

def test_is_palindrome():
    assert lec.is_palindrome("racecar") == True
    assert lec.is_palindrome("A man, a plan, a canal: Panama") == True
    assert lec.is_palindrome("Tony") == False
    print ("is palindrome test successful!!")
test_is_palindrome()

