from src.mit_ocw_exercises.lec3_strings_algos import (
    is_palindrome,
    count_substring_match,
    count_substring_match_recursive
)

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("Racecar") == False  # 大小寫不一樣
    assert is_palindrome("A man, a plan, a canal, Panama") == False  # 包含空白與符號
    assert is_palindrome("abba") == True
    assert is_palindrome("abc") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_count_substring_match():
    assert count_substring_match("atgacatgcacaagtatgcat", "atgc") == 2
    assert count_substring_match("aaaa", "aa") == 3
    assert count_substring_match("abcd", "e") == 0
    assert count_substring_match("", "a") == 0
    assert count_substring_match("abc", "") == 4  # 每個位置都可以插入空字串

def test_count_substring_match_recursive():
    assert count_substring_match_recursive("atgacatgcacaagtatgcat", "atgc") == 2
    assert count_substring_match_recursive("aaaa", "aa") == 3
    assert count_substring_match_recursive("abcd", "e") == 0
    assert count_substring_match_recursive("", "a") == 0
    assert count_substring_match_recursive("abc", "") == 4
