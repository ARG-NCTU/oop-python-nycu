import add_path
import mit_ocw_exercises.lec3_strings_algos as lec3
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("radar", True),           # Simple palindrome
    ("hello", False),          # Non-palindrome
    ("Racecar", True),         # Case-insensitive palindrome
    ("A man a plan a canal Panama", False),  # Space and special character sensitive
    ("", True),                # Empty string is a palindrome
    ("12321", True),           # Numeric palindrome
    ("12345", False),          # Non-palindromic number
    ("Noon", True),            # Mixed case palindrome
    ("Was it a car or a cat I saw?", False)  # Special characters make it non-palindromic
])
def test_is_palindrome(test_input, expected):
    assert lec3.is_palindrome(test_input) == expected
