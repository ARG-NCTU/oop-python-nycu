import pytest
import sys
import os
# Add current directory to sys.path to ensure imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lec6_recursion_dictionaries import (
    Towers, fib, fib_mem, fib_efficient, is_palindrome, 
    lyrics_to_frequencies, most_common_words, words_often
)

# -----------------
# 測試 Towers of Hanoi
# -----------------
def test_towers(capsys):
    """測試 Hanoi 塔 (檢查過輸出是否正確)"""
    Towers(1, 'A', 'B', 'Spare')
    captured = capsys.readouterr()
    assert "move from A to B" in captured.out

    Towers(2, 'A', 'B', 'Spare')
    captured = capsys.readouterr()
    # 2層塔應該有3步
    assert captured.out.count("move from") == 3
    # 檢查順序 verify output contains moves

# -----------------
# 測試 Fibonacci
# -----------------
def test_fib():
    """測試 fib (遞迴)"""
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(5) == 8

def test_fib_mem():
    """測試 fib_mem (修正後的版本)"""
    assert fib_mem(1) == 1
    assert fib_mem(2) == 2
    assert fib_mem(5) == 8

def test_fib_efficient():
    """測試 fib_efficient (字典 memoization)"""
    d = {1:1, 2:2}
    assert fib_efficient(5, d) == 8
    # d 應該被更新
    assert 5 in d
    assert d[5] == 8

# -----------------
# 測試 Palindrome
# -----------------
def test_is_palindrome():
    """測試 is_palindrome"""
    assert is_palindrome('eve') is True
    assert is_palindrome('Eve') is True # 大小寫忽略
    assert is_palindrome('Able was I, ere I saw Elba') is True
    assert is_palindrome('hello') is False
    assert is_palindrome('') is True # 空字串視為回文

# -----------------
# 測試 Dictionaries (Lyrics)
# -----------------
def test_lyrics_to_frequencies():
    """測試 lyrics_to_frequencies"""
    lyrics = ['she', 'loves', 'you', 'yeah', 'yeah']
    freqs = lyrics_to_frequencies(lyrics)
    assert freqs['she'] == 1
    assert freqs['yeah'] == 2
    assert 'loves' in freqs

def test_most_common_words():
    """測試 most_common_words"""
    freqs = {'a': 5, 'b': 2, 'c': 5}
    words, best = most_common_words(freqs)
    assert best == 5
    assert 'a' in words
    assert 'c' in words
    assert len(words) == 2

def test_words_often():
    """測試 words_often"""
    freqs = {'a': 5, 'b': 2, 'c': 5, 'd': 1}
    # minTimes = 3 -> should verify a and c
    result = words_often(freqs, 3)
    # result is list of tuples (list_of_words, count)
    # format: [(['a', 'c'], 5)]
    assert len(result) == 1
    assert result[0][1] == 5
    assert 'a' in result[0][0]
