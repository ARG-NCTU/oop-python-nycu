import lec_6.py as lec6
import pytest
# please write a test for fib function
def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) == 3
    assert lec6.fib(4) == 5
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13
    assert lec6.fib(7) == 21
    assert lec6.fib(8) == 34
    assert lec6.fib(9) == 55
    assert lec6.fib(10) == 89
    assert lec6.fib(11) == 144
    assert lec6.fib(12) == 233
def test_is_palindrome():
    assert lec6.is_palindrome('hello olleh') == True
    assert lec6.is_palindrome('I am genious') == False
    assert lec6.is_palindrome('madam') == True
    assert lec6.is_palindrome('vdiejssjeidv') == True
def test_most_common_words_and_palindrome():
    lyrics = [
        'love', 'me', 'do',
        'you', 'know', 'i', 'love', 'you',
        'ill', 'always', 'be', 'true',
        'so', 'please', 'love', 'me', 'do',
        'whoa', 'love', 'me', 'do'
    ]

    assert lec6.most_common_words(lec6.lyrics_to_frequencies(lyrics)) == (['love'], 4)
    assert lec6.is_palindrome('madam') == True
    assert lec6.is_palindrome('beatles') == False
