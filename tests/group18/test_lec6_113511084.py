import os
import sys
import pytest

sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../src'))

import mit_ocw_exercises.lec6_recursion_dictionaries as lec6


def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13


def test_is_palindrome():
    assert lec6.is_palindrome('Able was I, ere I saw Elba') is True
    assert lec6.is_palindrome('eve') is True
    assert lec6.is_palindrome('Eva, can I see bees in a cave?') is True
    assert lec6.is_palindrome('Not a palindrome') is False


def test_lyrics_to_frequencies():
    lyrics = ['hello', 'world', 'hello']
    freqs = lec6.lyrics_to_frequencies(lyrics)
    assert freqs == {'hello': 2, 'world': 1}


def test_most_common_words():
    freqs = {'a': 3, 'b': 5, 'c': 5, 'd': 1}
    words, count = lec6.most_common_words(freqs)
    assert set(words) == {'b', 'c'}
    assert count == 5


def test_words_often():
    freqs = {'a': 5, 'b': 3, 'c': 5, 'd': 1}
    result = lec6.words_often(freqs.copy(), 3)
    assert result == [(['a', 'c'], 5), (['b'], 3)]


def test_fib_efficient():
    d = {1: 1, 2: 2}
    result = lec6.fib_efficient(6, d.copy())  # 13
    assert result == 13

    d = {1: 1, 2: 2}
    result2 = lec6.fib_efficient(1, d.copy())
    assert result2 == 1

    d = {1: 1, 2: 2}
    result3 = lec6.fib_efficient(2, d.copy())
    assert result3 == 2


# def test_fib_mem():
#     assert lec6.fib_mem(1) == 1
#     assert lec6.fib_mem(2) == 2
#     assert lec6.fib_mem(5) == lec6.fib_mem(4) + lec6.fib_mem(3)
