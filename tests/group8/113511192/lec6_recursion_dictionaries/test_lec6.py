import add_path
import lec6 as lec6
import pytest

def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) == 3
    assert lec6.fib(4) == 5
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13
    assert lec6.fib(7) == 21

def test_is_palindrome():
    assert lec6.is_palindrome('level') == True
    assert lec6.is_palindrome('Was it a cat i saw') == True
    assert lec6.is_palindrome('Is this a palindrome') == False
    assert lec6.is_palindrome('refer') == True
    assert lec6.is_palindrome('hello') == False

def test_lyrics_to_frequencies():
    words = ['she', 'loves', 'you', 'she', 'loves', 'you', 'yeah']
    expected = {'she': 2, 'loves': 2, 'you': 2, 'yeah': 1}
    assert lec6.lyrics_to_frequencies(words) == expected


def test_most_common_words():
    lyrics = ['i', 'i', 'you', 'you', 'you', 'he']
    freq = lec6.lyrics_to_frequencies(lyrics)
    assert lec6.most_common_words(freq) == (['you'], 3)

def test_words_often():
    lyrics = ['a', 'b', 'b', 'c', 'c', 'c']
    freq = lec6.lyrics_to_frequencies(lyrics)
    assert lec6.words_often(freq, 3) == [(['c'], 3)]
    assert lec6.words_often(freq, 2) == [(['b'], 2)]
