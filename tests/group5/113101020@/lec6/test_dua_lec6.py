# test_dua_lec6.py
import pytest
from dua_lec6 import (
    printMove, Towers, fib, is_palindrome,
    lyrics_to_frequencies, most_common_words,
    words_often, fib_efficient
)

def test_printMove():
    assert printMove('A', 'B') == 'move from A to B'
    assert printMove(1, 3) == 'move from 1 to 3'

def test_Towers_n1():
    assert Towers(1, 'A', 'B', 'C') == ['move from A to B']

def test_Towers_n2():
    moves = Towers(2, 'A', 'B', 'C')
    # 對於 2 片盤子，應該有 3 步
    assert len(moves) == 3
    assert moves == [
        'move from A to C',
        'move from A to B',
        'move from C to B'
    ]

def test_fib():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(5) == 8
    # 小心指數增長，測一個中等值
    assert fib(10) == 89

@pytest.mark.parametrize("s,expected", [
    ("", True),
    ("A man, a plan, a canal: Panama", True),
    ("Able was I ere I saw Elba", True),
    ("Hello, world!", False),
])
def test_is_palindrome(s, expected):
    assert is_palindrome(s) is expected

def test_lyrics_to_frequencies():
    lyrics = ["la", "la", "ti", "do", "do", "do"]
    freqs = lyrics_to_frequencies(lyrics)
    assert freqs == {"la": 2, "ti": 1, "do": 3}

def test_most_common_words_single():
    freqs = {"a": 3, "b": 1, "c": 2}
    words, count = most_common_words(freqs)
    assert set(words) == {"a"} and count == 3

def test_most_common_words_multiple():
    freqs = {"a": 3, "b": 3, "c": 1}
    words, count = most_common_words(freqs)
    assert set(words) == {"a", "b"} and count == 3

def test_words_often():
    freqs = {"a": 3, "b": 3, "c": 2, "d": 1}
    result = words_often(freqs, minTimes=2)
    # 第一組: ['a','b'],3 ; 第二組: ['c'],2
    assert result[0] == (["a", "b"], 3)
    assert result[1] == (["c"], 2)
    # 不包含出現次數 1 的 'd'
    assert all(count >= 2 for _, count in result)

def test_fib_efficient_matches_fib():
    for n in [0, 1, 5, 10, 20]:
        assert fib_efficient(n) == fib(n)

def test_fib_efficient_performance():
    # 大 n 不會爆爆栈
    assert fib_efficient(100) == fib_efficient(99) + fib_efficient(98)
