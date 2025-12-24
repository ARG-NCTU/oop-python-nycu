import os
import sys
import pytest

"""Tests for `lec3_strings_algos.py` covering common edge cases and robustness.

Small additions: ensure repository path helper is invoked so imports succeed
when tests run from different working directories.
"""

# Ensure repo root is on sys.path so module can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import add_path  # keep existing repo pattern
# call the function defined in the module
add_path.add_path()

from lec3_strings_algos import is_palindrome


# ==================== Basic Palindrome Tests ====================
def test_simple_palindrome():
    """Test basic single-word palindromes."""
    assert is_palindrome("radar")
    assert is_palindrome("level")
    assert is_palindrome("civic")


def test_non_palindrome():
    """Test basic non-palindromes."""
    assert not is_palindrome("hello")
    assert not is_palindrome("Python")
    assert not is_palindrome("world")


# ==================== Edge Cases: Empty and Single Character ====================
def test_empty_string():
    """Empty string is technically a palindrome."""
    assert is_palindrome("")


def test_single_character():
    """Single character is always a palindrome."""
    assert is_palindrome("a")
    assert is_palindrome("Z")
    assert is_palindrome("5")


# ==================== Case Sensitivity ====================
def test_mixed_case_palindrome():
    """Test that case is properly ignored."""
    assert is_palindrome("RaDaR")
    assert is_palindrome("LeVeL")
    assert is_palindrome("TacoCat")
    assert is_palindrome("MoM")


def test_all_uppercase():
    """Test all uppercase palindromes."""
    assert is_palindrome("RADAR")
    assert is_palindrome("LEVEL")


def test_all_lowercase():
    """Test all lowercase palindromes."""
    assert is_palindrome("radar")
    assert is_palindrome("level")


# ==================== Spaces and Whitespace ====================
def test_spaces_ignored():
    """Test that spaces are properly ignored."""
    assert is_palindrome("race car")
    assert is_palindrome("a b a")
    assert is_palindrome("a man a plan a canal panama")


def test_only_spaces():
    """Test strings with only spaces."""
    assert is_palindrome("     ")
    assert is_palindrome(" ")


def test_multiple_spaces():
    """Test with multiple consecutive spaces."""
    assert is_palindrome("a  b  a")
    assert is_palindrome("a   b   a")


def test_tab_and_newline_characters():
    """Test various whitespace characters."""
    assert is_palindrome("a\tb\ta")  # tabs
    assert is_palindrome("a\nb\na")  # newlines


# ==================== Punctuation and Special Characters ====================
def test_mixed_case_spaces_punctuation():
    """Test realistic sentences with mixed case and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert is_palindrome("Was it a car or a cat I saw?")
    assert is_palindrome("Madam, I'm Adam")


def test_only_special_characters():
    """Test strings with only special characters (should be palindromes after filtering)."""
    assert is_palindrome("!@#@!")
    assert is_palindrome("---")
    assert is_palindrome(".,.,.")
    assert is_palindrome("!!!")


def test_punctuation_heavy():
    """Test strings heavily punctuated."""
    assert is_palindrome("a!b!c!b!a")
    assert is_palindrome("(a)(b)(a)")
    assert is_palindrome("[x][y][x]")


def test_consecutive_special_chars():
    """Test strings with consecutive special characters."""
    assert is_palindrome("a!!!b!!!a")
    assert is_palindrome("x---y---x")


# ==================== Numbers ====================
def test_numeric_palindromes():
    """Test numeric palindromes."""
    assert is_palindrome("0")
    assert is_palindrome("121")
    assert is_palindrome("12321")
    assert is_palindrome("99899")


def test_numeric_non_palindromes():
    """Test numeric non-palindromes."""
    assert not is_palindrome("1234")
    assert not is_palindrome("123")


def test_numbers_only():
    """Test strings with only numbers."""
    assert is_palindrome("12321")
    assert not is_palindrome("1234")


def test_mixed_alphanumeric():
    """Test mixed letters and numbers."""
    assert is_palindrome("A1B2C2B1A")
    assert is_palindrome("1a2b2a1")
    assert not is_palindrome("1a2b3")


# ==================== Long Strings ====================
def test_long_palindrome():
    """Test with longer strings."""
    assert is_palindrome("A1B2C2B1A")
    assert is_palindrome("abcdefedcba")
    long_pal = "a" * 100 + "b" + "a" * 100
    assert is_palindrome(long_pal)


def test_long_non_palindrome():
    """Test long non-palindrome strings."""
    assert not is_palindrome("abcdefghijklmnop")
    long_non_pal = "a" * 100 + "b" + "c" * 100
    assert not is_palindrome(long_non_pal)


# ==================== Repeated Characters ====================
def test_single_repeated_character():
    """Test strings with single character repeated."""
    assert is_palindrome("aaaa")
    assert is_palindrome("AAAA")
    assert is_palindrome("a a a a")
    assert is_palindrome("zzzzz")


def test_two_characters_palindrome():
    """Test palindromes with two alternating characters."""
    assert is_palindrome("abba")
    assert is_palindrome("ab ba")
    assert is_palindrome("a b b a")


# ==================== Almost Palindromes ====================
def test_non_palindrome_similar_endings():
    """Test strings that almost look like palindromes but aren't."""
    assert not is_palindrome("abc")
    assert not is_palindrome("abcde")
    assert not is_palindrome("12345")


def test_off_by_one():
    """Test strings that are off by one character."""
    assert not is_palindrome("abca")  # radar with 'a' instead of 'd'
    assert not is_palindrome("levil")  # level with 'i' instead of 'e'


# ==================== Unicode ====================
def test_unicode_palindrome():
    """Test with unicode characters (Japanese palindrome)."""
    assert is_palindrome("たけやぶやけた")


def test_mixed_unicode_and_ascii():
    """Test mixed unicode and ASCII."""
    assert is_palindrome("a日a")
    assert is_palindrome("A中A")  # Fixed: "a中a" is a palindrome
    assert not is_palindrome("a日b")


def test_various_unicode_scripts():
    """Test various unicode scripts."""
    assert is_palindrome("αβα")  # Greek
    assert is_palindrome("абв ба")  # Cyrillic (with space)


# ==================== Emoji and Special Unicode ====================
def test_emoji_handling():
    """Test with emoji - function should not crash."""
    # Emoji should be handled by isalnum() - most emoji are not alphanumeric
    # but test that the function doesn't crash
    result = is_palindrome("😀😀")
    assert isinstance(result, bool)
    
    result = is_palindrome("😀a😀")
    assert isinstance(result, bool)


# ==================== Combination Edge Cases ====================
def test_extreme_whitespace_mix():
    """Test extreme combinations of whitespace."""
    assert is_palindrome("   a   b   a   ")
    assert is_palindrome("\t\ta\t\tb\t\ta\t\t")


def test_mixed_everything():
    """Test with a mix of everything: case, punctuation, numbers, spaces."""
    assert is_palindrome("A1!b@2B!1a")
    assert is_palindrome("MaDaM, I'm AdaM!")


def test_apostrophe_and_special_marks():
    """Test with apostrophes and special marks."""
    assert is_palindrome("Madam, I'm Adam")
    assert is_palindrome("No 'x' in Nixon")


# ==================== Robustness: No Crashes ====================
def test_does_not_crash_on_unusual_input():
    """Ensure function is robust and doesn't crash on unusual inputs."""
    # These should all return a boolean without crashing
    assert isinstance(is_palindrome(""), bool)
    assert isinstance(is_palindrome("!@#$%^&*()"), bool)
    assert isinstance(is_palindrome("   \t\n   "), bool)
    assert isinstance(is_palindrome("🎉🎉🎉"), bool)


# ==================== Return Type Validation ====================
def test_returns_boolean():
    """Ensure function always returns a boolean."""
    assert isinstance(is_palindrome("test"), bool)
    assert isinstance(is_palindrome(""), bool)
    assert isinstance(is_palindrome("a"), bool)
