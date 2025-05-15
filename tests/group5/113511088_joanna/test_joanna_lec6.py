from lec6_final import *

def test_towers_of_hanoi():
    moves = towers_of_hanoi(2, 'A', 'C', 'B')
    assert moves == ['move from A to B', 'move from A to C', 'move from B to C']

def test_fib():
    assert fib(0) == 1
    assert fib(4) == 5

def test_is_palindrome():
    assert is_palindrome("Able was I, ere I saw Elba")
    assert not is_palindrome("Hello world")

def test_lyrics_to_frequencies():
    sample = ['a', 'b', 'a', 'c', 'b', 'a']
    freqs = lyrics_to_frequencies(sample)
    assert freqs == {'a': 3, 'b': 2, 'c': 1}

def test_most_common_words():
    freqs = {'a': 3, 'b': 2, 'c': 3}
    words, count = most_common_words(freqs)
    assert set(words) == {'a', 'c'}
    assert count == 3

def test_words_often():
    freqs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
    result = words_often(freqs, 2)
    assert result == [(['a'], 4), (['b'], 3), (['c'], 2)]

def test_fib_mem():
    assert fib_mem(5) == 8

def test_fib_efficient():
    assert fib_efficient(5) == fib_mem(5)
    assert fib_efficient(10) == 89

