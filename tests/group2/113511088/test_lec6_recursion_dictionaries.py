# -*- coding: utf-8 -*-
import pytest

import lec6_recursion_dictionaries as lec6

def test_fib_base_and_small():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) == 3
    assert lec6.fib(4) == 5
    assert lec6.fib(5) == 8


def test_fib_invalid():
    with pytest.raises(ValueError):
        lec6.fib(-1)


def test_is_palindrome():
    assert lec6.is_palindrome("eve") is True
    assert lec6.is_palindrome("Able was I, ere I saw Elba") is True
    assert lec6.is_palindrome("Is this a palindrome") is False
    assert lec6.is_palindrome("") is True


def test_lyrics_to_frequencies():
    lyrics = ["a", "b", "a", "c", "b", "a"]
    freqs = lec6.lyrics_to_frequencies(lyrics)
    assert freqs == {"a": 3, "b": 2, "c": 1}


def test_most_common_words_single():
    freqs = {"a": 3, "b": 2, "c": 1}
    words, best = lec6.most_common_words(freqs)
    assert best == 3
    assert words == ["a"]


def test_most_common_words_tie():
    freqs = {"a": 3, "b": 3, "c": 1}
    words, best = lec6.most_common_words(freqs)
    assert best == 3
    assert set(words) == {"a", "b"}


def test_most_common_words_empty():
    with pytest.raises(ValueError):
        lec6.most_common_words({})


def test_words_often_does_not_mutate_original():
    freqs = {"a": 3, "b": 3, "c": 1}
    freqs_before = freqs.copy()

    result = lec6.words_often(freqs, 2)
    # should not mutate
    assert freqs == freqs_before

    # first group: a,b with 3
    assert result[0][1] == 3
    assert set(result[0][0]) == {"a", "b"}


def test_words_often_minTimes_invalid():
    with pytest.raises(ValueError):
        lec6.words_often({"a": 1}, 0)


def test_fib_mem_and_fib_efficient():
    assert lec6.fib_mem(0) == 1
    assert lec6.fib_mem(1) == 1
    assert lec6.fib_mem(5) == 8

    d = {0: 1, 1: 1}
    ans = lec6.fib_efficient(10, d)
    assert ans == 89  # 0-based fib: 1,1,2,3,5,8,13,21,34,55,89
    # memoization should have filled some entries
    assert 10 in d


def test_fib_efficient_invalid():
    with pytest.raises(ValueError):
        lec6.fib_efficient(-2, {0: 1, 1: 1})


def test_towers_prints_correct_number_of_moves(capsys):
    lec6.Towers(3, "P1", "P2", "P3")
    out = capsys.readouterr().out.strip().splitlines()

    # Towers(3) should output 2^3 - 1 = 7 moves
    assert len(out) == 7

    # sanity check first and last move (by this recursion order)
    assert out[0] == "move from P1 to P2"
    assert out[-1] == "move from P1 to P2"


def test_towers_invalid_n():
    with pytest.raises(ValueError):
        lec6.Towers(0, "P1", "P2", "P3")
