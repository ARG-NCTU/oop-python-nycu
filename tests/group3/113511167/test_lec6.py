from lec6 import fib, is_palindrome, lyrics_to_frequencies, words_often, fib_efficient

lyrics = ['she', 'loves', 'you', 'yeah', 'yeah', 
          'yeah','she', 'loves', 'you', 'yeah', 
          'yeah', 'yeah']

d = {0:1, 1:1}

def test_fib():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 3

def test_is_palindrome():
    assert is_palindrome('eve') == True
    assert is_palindrome('Able was I, ere I saw Elba') == True
    assert is_palindrome('Is this a palindrome') == False
    assert is_palindrome('a') == True
    assert is_palindrome('') == True

def lyrics_to_frequencies_test():
    assert lyrics_to_frequencies(lyrics) == {'she': 2, 'loves': 2, 'you': 2, 'yeah': 6}
    assert lyrics_to_frequencies(['a', 'b', 'a']) == {'a': 2, 'b': 1}

def words_often_test():
    assert words_often(lyrics_to_frequencies(lyrics), 2) == [(['yeah'], 6)]
    assert words_often(lyrics_to_frequencies(lyrics), 3) == [(['yeah'], 6)]
    assert words_often(lyrics_to_frequencies(lyrics), 4) == [(['yeah'], 6)]
    assert words_often(lyrics_to_frequencies(lyrics), 1) == [(['yeah'], 6), (['she', 'loves', 'you'], 2)]

def test_fib_efficient():
    assert fib_efficient(0,d) == 1
    assert fib_efficient(1,d) == 1
    assert fib_efficient(2,d) == 2
    assert fib_efficient(3,d) == 3
    assert fib_efficient(4,d) == 5
