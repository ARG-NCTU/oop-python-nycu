import lec_6.py as lec6
import pytest

def test_fib_alternate():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(3) == 3
    assert lec6.fib(5) == 8
    assert lec6.fib(7) == 21
    assert lec6.fib(9) == 55
    assert lec6.fib(13) == 233

def test_is_palindrome_alternate():
    assert lec6.is_palindrome('racecar') == True
    assert lec6.is_palindrome('step on no pets') == True
    assert lec6.is_palindrome('python') == False
    assert lec6.is_palindrome('never odd or even') == True
    assert lec6.is_palindrome('palindrome') == False

def test_most_common_words_and_palindrome_alternate():
    lyrics = [
        'hello', 'world', 'hello', 'python',
        'test', 'world', 'hello', 'openai',
        'hello', 'test', 'python', 'code',
        'test', 'test', 'openai', 'openai'
    ]

    assert lec6.most_common_words(lec6.lyrics_to_frequencies(lyrics)) == (['hello', 'test'], 4)
    assert lec6.is_palindrome('deed') == True
    assert lec6.is_palindrome('openai') == False
