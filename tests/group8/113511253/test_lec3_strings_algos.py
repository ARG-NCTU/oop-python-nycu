import pytest
import sys
import os

# 為了 Lec3 我們直接 import，因為我們修過它，確定它沒問題
from tests.group8.113511253.lec3_strings_algos import is_palindrome, cheer_word, perfect_cube

def test_is_palindrome():
    assert is_palindrome("Racecar")
    assert not is_palindrome("python")

def test_cheer_word():
    result = cheer_word("MIT", 2)
    # 驗證結構：MIT(3) + Question(1) + Answers(2) = 6
    assert len(result) == 6
    assert "Give me" in result[0]
    assert result[-1] == "MIT !!!"

def test_perfect_cube():
    assert perfect_cube(27) == 3
    assert perfect_cube(-8) == -2
