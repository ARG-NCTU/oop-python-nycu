import pytest
import add_path
from lec3_strings_algos import is_palindrome
# ↑ replace 'your_module_filename' with the actual .py file name (without .py)

def test_basic_palindrome():
    assert is_palindrome("madam") is True

def test_non_palindrome():
    assert is_palindrome("race a car") is False

def test_phrase_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") is True

def test_empty_space_palindrome():
    assert is_palindrome(" ") is True
