import pytest
import lec3

def test_is_palindrome():
    assert lec3.is_palindrome("Tree Lee RT")==False
    assert lec3.is_palindrome("TreeLee")==False
    assert lec3.is_palindrome("YesseY") ==True