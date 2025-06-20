import pytest
from lec3 import (is_palindrome, check_vowels, cheer_word, 
                               find_perfect_cube, guess_cube_root, 
                               approximate_cube_root, bisection_cube_root)

def test_is_palindrome():
    assert is_palindrome("radar") is True
    assert is_palindrome("RaDaR") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("") is True
    assert is_palindrome("a") is True
    assert is_palindrome("race car") is False

def test_check_vowels():
    result = check_vowels("input")
    assert len(result) == 5
    assert result[1] == "Position 1: Found 'i' (i or u)"
    assert result[3] == "Position 3: Found 'u' (i or u)"
    assert result[0] == "Position 0: No i or u"
    result = check_vowels("")
    assert result == []

def test_cheer_word():
    result = cheer_word("cat", 2)
    assert len(result) == 6  # 3 chars + 1 spell + 2 cheers
    assert result[0] == "Give me an c! c"
    assert result[1] == "Give me an a! a"
    assert result[3] == "What does that spell?"
    assert result[4] == "cat!!!"
    result = cheer_word("xyz", 0)
    assert len(result) == 4  # 3 chars + 1 spell
    result = cheer_word("", 1)
    assert result == ["What does that spell?", "!!!"]

def test_find_perfect_cube():
    result = find_perfect_cube(27)
    assert result["found"] is True
    assert result["root"] == 3
    assert result["iterations"] > 0
    result = find_perfect_cube(30)
    assert result["found"] is False
    assert result["root"] is None
    result = find_perfect_cube(0)
    assert result["found"] is True
    assert result["root"] == 0

def test_guess_cube_root():
    result = guess_cube_root(27)
    assert result["is_perfect"] is True
    assert result["root"] == 3
    result = guess_cube_root(-8)
    assert result["is_perfect"] is True
    assert result["root"] == -2
    result = guess_cube_root(30)
    assert result["is_perfect"] is False
    assert result["root"] is None

def test_approximate_cube_root():
    result = approximate_cube_root(8, epsilon=0.1, increment=0.01)
    assert result["success"] is True
    assert abs(result["guess"] ** 3 - 8) < 0.1
    assert result["iterations"] > 0
    result = approximate_cube_root(9, epsilon=1e-10, increment=1.0)
    assert result["success"] is False
    result = approximate_cube_root(0, epsilon=0.1, increment=0.01)
    assert result["success"] is True
    assert result["guess"] == 0.0

def test_bisection_cube_root():
    result = bisection_cube_root(27, epsilon=0.01)
    assert result["success"] is True
    assert abs(result["guess"] ** 3 - 27) < 0.01
    assert result["iterations"] > 0
    result = bisection_cube_root(0.125, epsilon=0.001)
    assert result["success"] is True
    assert abs(result["guess"] ** 3 - 0.125) < 0.001
    result = bisection_cube_root(-1, epsilon=0.01)
    assert result["success"] is False
    assert result["guess"] is None
