# test_dua_example.py

import pytest
from dua_example import *

def test_towers_output(capfd):
    Towers(2, "A", "C", "B")
    out, _ = capfd.readouterr()
    expected = "move from A to B\nmove from A to C\nmove from B to C\n"
    assert out == expected

def test_fib_basic():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(5) == 8
    assert fib(6) == 13

def test_fib_efficient_vs_fib_mem():
    d = {1: 1, 2: 2}
    for n in range(1, 10):
        assert fib_efficient(n, d) == fib_mem(n)

def test_palindrome():
    assert is_palindrome("Able was I, ere I saw Elba") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("no lemon, no melon") == True
    assert is_palindrome("hello world") == False

def test_lyrics_to_frequencies():
    freqs = lyrics_to_frequencies(['a', 'b', 'a', 'c', 'b', 'a'])
    assert freqs == {'a': 3, 'b': 2, 'c': 1}

def test_most_common_words():
    freqs = {'a': 3, 'b': 2, 'c': 1}
    result = most_common_words(freqs)
    assert result == (['a'], 3)

def test_words_often():
    freqs = {'a': 5, 'b': 4, 'c': 2, 'd': 1}
    result = words_often(freqs.copy(), 2)
    assert result == [(['a'], 5), (['b'], 4), (['c'], 2)]
