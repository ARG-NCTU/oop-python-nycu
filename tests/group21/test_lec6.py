import pytest
import lec6  # 假設你將原始程式碼檔案命名為 hw.py

def test_fib():
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) == 3
    assert lec6.fib(4) == 5

def test_fib_efficient():
    d = {1: 1, 2: 2}
    assert lec6.fib_efficient(1, d) == 1
    assert lec6.fib_efficient(2, d) == 2
    assert lec6.fib_efficient(4, d) == 5
    assert lec6.fib_efficient(10, d) == 89  # 10th fib where f(1)=1, f(2)=2

def test_is_palindrome():
    assert lec6.isPalindrome("eve") is True
    assert lec6.isPalindrome("Able was I, ere I saw Elba") is True
    assert lec6.isPalindrome("This is not a palindrome") is False

def test_lyrics_to_frequencies():
    lyrics = ['a', 'b', 'a', 'c', 'b', 'a']
    result = lec6.lyrics_to_frequencies(lyrics)
    assert result == {'a': 3, 'b': 2, 'c': 1}

def test_most_common_words():
    freqs = {'a': 3, 'b': 2, 'c': 3}
    words, count = lec6.most_common_words(freqs)
    assert set(words) == {'a', 'c'}
    assert count == 3

def test_words_often():
    freqs = {'a': 5, 'b': 3, 'c': 5, 'd': 2}
    result = lec6.words_often(freqs.copy(), 3)
    # first round: a and c (5), then b (3)
    assert result == [(['a', 'c'], 5), (['b'], 3)]

