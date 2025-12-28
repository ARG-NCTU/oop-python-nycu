import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import add_path
from src.mit_ocw_exercises.lec6_recursion_dictionaries import fib, is_palindrome, lyrics_to_frequencies, fib_mem, fib_efficient, printMove, Towers, most_common_words, words_often

def test_fib():
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 3
    assert fib(4) == 5
    assert fib(5) == 8
    assert fib(10) == 89
    assert fib(20) == 10946

def test_is_palindrome():
    assert is_palindrome('eve') == True
    assert is_palindrome('streferts') == True
    assert is_palindrome('What can I say?') == False
    assert is_palindrome('mamba out') == False

def test_lyrics_to_frequencies():
    lyrics = ['hello', 'world', 'hello', 'mit', 'world', 'hello']
    freq = lyrics_to_frequencies(lyrics)
    assert freq == {'hello': 3, 'world': 2, 'mit': 1}
    
    lyrics = []
    freq = lyrics_to_frequencies(lyrics)
    assert freq == {}
    
    lyrics = ['one', 'two', 'three', 'two', 'one', 'one']
    freq = lyrics_to_frequencies(lyrics)
    assert freq == {'one': 3, 'two': 2, 'three': 1}

def test_most_common_words():
    freqs = {'hello': 3, 'world': 2, 'mit': 1}
    words, count = most_common_words(freqs)
    assert set(words) == {'hello'}
    assert count == 3

    freqs = {'a': 5, 'b': 5, 'c': 2}
    words, count = most_common_words(freqs)
    assert set(words) == {'a', 'b'}
    assert count == 5

def test_words_often():
    freqs = {'hello': 3, 'world': 2, 'mit': 1}
    result = words_often(freqs.copy(), 2)
    assert result == [(['hello'], 3), (['world'], 2)]

    freqs = {'a': 5, 'b': 5, 'c': 2, 'd': 1}
    result = words_often(freqs.copy(), 3)
    assert result == [(['a', 'b'], 5)]

    freqs = {'x': 1, 'y': 1}
    result = words_often(freqs.copy(), 2)
    assert result == []

#####################################