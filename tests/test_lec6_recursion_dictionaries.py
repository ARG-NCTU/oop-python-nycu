
import add_path
import mit_ocw_exercises.lec6_recursion_dictionaries as lec6
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
    
    
# please write a test for is_palindrome function
def test_is_palindrome():
    assert lec6.is_palindrome('eve') == True
    assert lec6.is_palindrome('Able was I, ere I saw Elba') == True
    assert lec6.is_palindrome('Is this a palindrome') == False
    assert lec6.is_palindrome('eillie') == True
    assert lec6.is_palindrome('cookieliileikooc') == True

fuchengguo = ['wuo','due','ni','i','i','i','bu','wan']
beatles = lec6.lyrics_to_frequencies(fuchengguo)
def test_lyrics_to_frequencies():
    assert lec6.lyrics_to_frequencies(fuchengguo) == {'wuo': 1, 'due': 1, 'ni': 1, 'i': 3, 'bu': 1, 'wan': 1}
def test_most_common_words():
    assert lec6.most_common_words(beatles) == (['i'], 3)
def test_words_often():
    assert lec6.words_often(beatles, 3) == [(['i'], 3)]
    assert lec6.words_often(beatles, 2) == []
        
