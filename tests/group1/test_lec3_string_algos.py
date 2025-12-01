import os
import sys
import pytest

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