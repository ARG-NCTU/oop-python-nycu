import pytest
from lec6_recursion_dictionaries import printMove, Towers, fib, is_palindrome, lyrics_to_frequencies, most_common_words, words_often, fib_efficient, fib_mem

def test_towers(capsys):
    Towers(2, 'P1', 'P2', 'P3')
    output = capsys.readouterr().out.strip().splitlines()
    expected = ['move from P1 to P3', 'move from P1 to P2', 'move from P3 to P2']
    assert output == expected

def test_fib():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 3
    assert fib(4) == 5
    assert fib(5) == 8

def test_is_palindrome():
    assert is_palindrome('eve')
    assert is_palindrome('Able was I, ere I saw Elba')
    assert not is_palindrome('Is this a palindrome')

def test_lyrics_to_frequencies():
    lyrics = ["love", "you", "love", "me"]
    freqs = lyrics_to_frequencies(lyrics)
    assert freqs == {"love": 2, "you": 1, "me": 1}

def test_most_common_words():
    freqs = {"a": 3, "b": 5, "c": 5, "d": 2}
    words, count = most_common_words(freqs)
    assert count == 5
    assert set(words) == {"b", "c"}

def test_words_often():
    freqs = {"a": 5, "b": 3, "c": 5, "d": 2}
    result = words_often(freqs.copy(), 3)
    assert len(result) == 2
    for words, count in result:
        if count == 5:
            assert set(words) == {"a", "c"}
        elif count == 3:
            assert set(words) == {"b"}
        else:
            pytest.fail("Unexpected frequency")

def test_fib_efficient():
    d = {1: 1, 2: 2}
    assert fib_efficient(3, d) == 3
    d = {1: 1, 2: 2}
    assert fib_efficient(4, d) == 5
    d = {1: 1, 2: 2}
    assert fib_efficient(10, d) == 89

def test_fib_mem_error():
    with pytest.raises(NameError):
        fib_mem(3)
