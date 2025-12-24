import os
import sys
import pytest

# --- Path Setup ---
# Add the directory containing this file to the path so we can import add_path
sys.path.append(os.path.dirname(__file__))

# Try importing the helper; if it fails, rely on the manual sys.path append below
try:
    from add_path import add_path
    add_path()
except ImportError:
    pass

# Ensure repo root is on sys.path so module can be imported (Standard Pattern)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# --- Logic Import ---
from lec3_strings_algos import is_palindrome

# --- Tests ---

@pytest.mark.parametrize("candidate", [
    "radar",
    "level",
    "A man, a plan, a canal: Panama",  # Mixed case + punctuation
    "Was it a car or a cat I saw?",
    "",                                # Empty string edge case
    "x",                               # Single char edge case
    "12321",                           # Numeric
    "123 21",                          # Numeric with space
    "No 'x' in Nixon",                 # Alphanumeric with apostrophe
    "たけやぶやけた",                   # Unicode (Japanese)
])
def test_is_palindrome_true(candidate):
    """
    Test inputs that SHOULD be identified as palindromes.
    """
    assert is_palindrome(candidate), f"Expected '{candidate}' to be a palindrome"


@pytest.mark.parametrize("candidate", [
    "helloworld",
    "Pythonandc++",
    "987654",
    "not a palindrome"
])
def test_is_palindrome_false(candidate):
    """
    Test inputs that should NOT be identified as palindromes.
    """
    assert not is_palindrome(candidate), f"Expected '{candidate}' NOT to be a palindrome"