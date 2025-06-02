import pytest
from src.mit_ocw_exercises import lec6_recursion_dictionaries as lec6

def test_towers_of_hanoi(capsys):
    lec6.Towers(2, 'A', 'B', 'C')
    captured = capsys.readouterr().out
    assert "move from A to C" in captured
    assert "move from A to B" in captured
    assert "move from C to B" in captured

def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13



def test_fib_efficient():
    d = {1: 1, 2: 2}
    assert lec6.fib_efficient(5, d) == lec6.fib_efficient(4, d) + lec6.fib_efficient(3, d)
    # The memoization should work
    assert 5 in d
    assert 3 in d
    
def test_is_palindrome():
    assert lec6.is_palindrome("eve") is True
    assert lec6.is_palindrome("Able was I, ere I saw Elba") is True
    assert lec6.is_palindrome("Is this a palindrome") is False
    assert lec6.is_palindrome("") is True
    assert lec6.is_palindrome("A") is True

def test_lyrics_to_frequencies():
    lyrics = ["hello", "world", "hello"]
    freqs = lec6.lyrics_to_frequencies(lyrics)
    assert freqs["hello"] == 2
    assert freqs["world"] == 1

def test_most_common_words():
    freqs = {"a": 3, "b": 2, "c": 3}
    words, count = lec6.most_common_words(freqs)
    assert set(words) == {"a", "c"}
    assert count == 3

def test_words_often():
    freqs = {"a": 5, "b": 3, "c": 5, "d": 2}
    result = lec6.words_often(freqs.copy(), 3)
    assert ("a" in result[0][0] and "c" in result[0][0])
    assert result[0][1] == 5
    assert result[1][0] == ["b"]
    assert result[1][1] == 3

def test_fib_mem():
    assert lec6.fib_mem(1) == 1
    assert lec6.fib_mem(2) == 2
    assert lec6.fib_mem(5) == lec6.fib_mem(4) + lec6.fib_mem(3)
