import pytest
import lec6

def test_fib():
    """assumes x an int >= 0
       returns Fibonacci of x"""
    assert lec6.fib(1)==1
    assert lec6.fib(2)==2
    assert lec6.fib(3)==3
    assert lec6.fib(4)==5

def test_is_palindrome():
    assert lec6.is_palindrome("Tree Lee RT")==True
    assert lec6.is_palindrome("Tree Lee")==False
    assert lec6.is_palindrome("YesseY") ==True