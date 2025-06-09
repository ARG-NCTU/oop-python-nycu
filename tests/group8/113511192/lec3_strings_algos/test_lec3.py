import pytest
from lec3_strings_algos import is_palindrome  # Replace with the actual module name

@pytest.mark.parametrize("s,expected", [
    ("Racecar", True),         # mixed case
    ("madam", True),           # basic palindrome
    ("MadAm", True),           # case-insensitive check
    ("12321", True),           # numeric string
    ("", True),                # empty string is a palindrome
    ("a", True),               # single character
    ("hello", False),          # not a palindrome
    ("Python", False),         # different start and end
    ("No lemon no melon", False), # phrase with spaces (not ignored in this simple version)
])
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected
