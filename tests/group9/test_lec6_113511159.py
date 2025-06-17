import add_path
import lec6_113511159 as mod
import pytest

def test_fib():
    assert mod.fib(0) == 1
    assert mod.fib(1) == 1
    assert mod.fib(5) == 8
    assert mod.fib(6) == 13

def test_is_palindrome():
    assert mod.is_palindrome('Able was I, ere I saw Elba') is True
    assert mod.is_palindrome('eve') is True
    assert mod.is_palindrome('A man, a plan, a canal, Panama') is True
    assert mod.is_palindrome('Not a palindrome') is False

def test_lyrics_to_frequencies():
    lyrics = ['hello', 'hello', 'world']
    expected = {'hello': 2, 'world': 1}
    assert mod.lyrics_to_frequencies(lyrics) == expected

def test_most_common_words():
    data = {'a': 3, 'b': 5, 'c': 5, 'd': 1}
    result = mod.most_common_words(data)
    assert sorted(result[0]) == ['b', 'c']
    assert result[1] == 5

def test_words_often():
    data = {'a': 10, 'b': 5, 'c': 5, 'd': 2, 'e': 1}
    expected = [(['a'], 10), (['b', 'c'], 5)]
    assert mod.words_often(data.copy(), 5) == expected

def test_fib_mem():
    assert mod.fib_mem(1) == 1
    assert mod.fib_mem(2) == 2
    assert mod.fib_mem(5) == 8

def test_fib_efficient():
    d = {1: 1, 2: 2}
    assert mod.fib_efficient(5, d.copy()) == 8
    assert mod.fib_efficient(6, {1: 1, 2: 2}) == 13