import pytest
from src.mit_ocw_exercises import lec6_recursion_dictionaries as lec6

def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13
def test_is_palindrome():
    assert lec6.is_palindrome('eve') is True
    assert lec6.is_palindrome('Able was I, ere I saw Elba') is True
    assert lec6.is_palindrome('Is this a palindrome') is False
    assert lec6.is_palindrome('A man, a plan, a canal, Panama') is True
def test_lyrics_to_frequencies():
    lyrics = ['hello', 'world', 'hello', 'python']
    result = lec6.lyrics_to_frequencies(lyrics)
    assert result == {'hello': 2, 'world': 1, 'python': 1}
def test_most_common_words():
    freqs = {'a': 5, 'b': 2, 'c': 5}
    words, count = lec6.most_common_words(freqs)
    assert set(words) == {'a', 'c'}
    assert count == 5

def test_words_often():
    freqs = {'a': 5, 'b': 2, 'c': 5, 'd': 1}
    # Copy as function modifies input
    from copy import deepcopy
    result = lec6.words_often(deepcopy(freqs), 2)
    # Should find ('a','c') with 5, ('b',) with 2
    result_sorted = sorted([(sorted(words), count) for words, count in result])
    assert result_sorted == [(['a', 'c'], 5), (['b'], 2)]
def test_fib_mem():
    assert lec6.fib_mem(1) == 1
    assert lec6.fib_mem(2) == 2
    assert lec6.fib_mem(5) == lec6.fib_mem(4) + lec6.fib_mem(3)

def test_fib_efficient():
    d = {1: 1, 2: 2}
    assert lec6.fib_efficient(3, d.copy()) == 3
    d = {1: 1, 2: 2}
    assert lec6.fib_efficient(6, d.copy()) == 21
