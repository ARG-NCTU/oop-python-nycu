import os
import sys
import pytest
# Ensure repo root is on sys.path so module can be imported
from add_path import add_path
add_path()
# Ensure repo root is on sys.path so module can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import add_path  # keep existing repo pattern

from lec3_strings_algos import is_palindrome


def test_simple_palindrome():
    assert is_palindrome("radar")
    assert is_palindrome("level")


def test_mixed_case_and_spaces_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert is_palindrome("Was it a car or a cat I saw?")


def test_empty_and_single_character():
    assert is_palindrome("")
    assert is_palindrome("x")


def test_non_palindrome():
    assert not is_palindrome("hello")
    assert not is_palindrome("Python")


def test_numeric_and_spaces():
    assert is_palindrome("12321")
    assert is_palindrome("123 21")  # spaces should be ignored by the implementation


def test_alphanumeric_and_apostrophes():
    assert is_palindrome("No 'x' in Nixon")


def test_unicode_palindrome():
    # common Japanese palindrome "たけやぶやけた"
    assert is_palindrome("たけやぶやけた")


def test_only_special_characters():
    """Test strings with only special characters (should be palindromes after filtering)."""
    assert is_palindrome("!@#@!")
    assert is_palindrome("---")
    assert is_palindrome(".,.,.")


def test_only_spaces():
    """Test strings with only spaces (should be palindromes)."""
    assert is_palindrome("     ")


def test_mixed_case_palindrome():
    """Test that case is properly ignored."""
    assert is_palindrome("RaDaR")
    assert is_palindrome("LeVeL")
    assert is_palindrome("TacoCat")


def test_numbers_only():
    """Test numeric palindromes."""
    assert is_palindrome("0")
    assert is_palindrome("121")
    assert is_palindrome("99899")
    assert not is_palindrome("1234")


def test_long_palindrome():
    """Test with longer strings."""
    assert is_palindrome("A1B2C2B1A")
    assert is_palindrome("The quick brown fox jumps over the lazy dog, god yzal eht revo spmuj xof nworb kciuq ehT")


def test_single_repeated_character():
    """Test strings with single character repeated."""
    assert is_palindrome("aaaa")
    assert is_palindrome("AAAA")
    assert is_palindrome("a a a a")


def test_non_palindrome_similar_endings():
    """Test strings that almost look like palindromes but aren't."""
    assert not is_palindrome("abc")
    assert not is_palindrome("abcde")
    assert not is_palindrome("12345")


def test_whitespace_variations():
    """Test various whitespace characters."""
    assert is_palindrome("a b a")
    assert is_palindrome("a\tb\ta")  # tabs
    assert is_palindrome("a\nb\na")  # newlines


def test_leading_trailing_spaces():
    """Leading/trailing spaces should be ignored by the implementation."""
    assert is_palindrome(" radar ")
    assert is_palindrome("  A man, a plan, a canal: Panama  ")


def test_punctuation_heavy():
    """Test strings heavily punctuated."""
    assert is_palindrome("a!b!c!b!a")
    assert is_palindrome("(a)(b)(a)")
    assert is_palindrome("[x][y][x]")


def test_mixed_unicode_and_ascii():
    """Test mixed unicode and ASCII."""
    assert is_palindrome("a日a")
    assert is_palindrome("A中A")  # Fixed: "a中a" is a palindrome
    assert not is_palindrome("a日b")


def test_emoji_and_special():
    """Test with emoji and special unicode characters."""
    # Emoji should be handled by isalnum() - most emoji are not alphanumeric
    # but test that the function doesn't crash
    result = is_palindrome("😀😀")  # Should not raise
    assert isinstance(result, bool)


def test_consecutive_special_chars():
    """Test strings with consecutive special characters."""
    assert is_palindrome("a!!!b!!!a")
    assert is_palindrome("x   y   x")
