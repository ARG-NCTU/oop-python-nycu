import pytest
from lec6_recursion_dict import (
    printMove, Towers, fib, is_palindrome,
    lyrics_to_frequencies, most_common_words, words_often,
    fib_mem, fib_efficient
)

def test_printMove(capsys):
    printMove('A', 'B')
    captured = capsys.readouterr()
    assert captured.out == 'move from A to B\n'
    printMove('P1', 'P3')
    captured = capsys.readouterr()
    assert captured.out == 'move from P1 to P3\n'

def test_Towers(capsys):
    Towers(1, 'A', 'B', 'C')
    captured = capsys.readouterr()
    assert captured.out == 'move from A to B\n'
    Towers(2, 'A', 'B', 'C')
    captured = capsys.readouterr()
    assert len(captured.out.split('\n')) == 4  # 3 moves + empty line
    expected_moves = [
        'move from A to C',
        'move from A to B',
        'move from C to B'
    ]
    for move in expected_moves:
        assert move in captured.out

def test_fib():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(5) == 8
    with pytest.raises(RecursionError):
        fib(-1)

def test_is_palindrome():
    assert is_palindrome('eve') is True
    assert is_palindrome('Able was I, ere I saw Elba') is True
    assert is_palindrome('Is this a palindrome') is False
    assert is_palindrome('') is True
    assert is_palindrome('a') is True

def test_lyrics_to_frequencies():
    lyrics = ['she', 'loves', 'you', 'she', 'you']
    freq = lyrics_to_frequencies(lyrics)
    assert freq == {'she': 2, 'loves': 1, 'you': 2}
    assert lyrics_to_frequencies([]) == {}

def test_most_common_words():
    freq = {'she': 2, 'loves': 1, 'you': 2}
    words, count = most_common_words(freq)
    assert sorted(words) == ['she', 'you']
    assert count == 2
    assert most_common_words({}) == ([], 0)

def test_words_often():
    freq = {'she': 5, 'loves': 3, 'you': 5, 'yeah': 2}
    result = words_often(freq, 3)
    assert len(result) == 2
    assert sorted(result[0][0]) == ['she', 'you']
    assert result[0][1] == 5
    assert result[1][0] == ['loves']
    assert result[1][1] == 3
    assert words_often({}, 1) == []

def test_fib_mem():
    assert fib_mem(0) == 1
    assert fib_mem(1) == 1
    assert fib_mem(2) == 2
    assert fib_mem(5) == 8
    with pytest.raises(RecursionError):
        fib_mem(-1)

def test_fib_efficient():
    assert fib_efficient(0) == 1
    assert fib_efficient(1) == 1
    assert fib_efficient(2) == 2
    assert fib_efficient(5) == 8
    assert fib_efficient(10) == 89
    with pytest.raises(RecursionError):
        fib_efficient(-1)
