import pytest
import lec6_recursion_dictionaries as lec6
import math

def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(10) == 89

def test_pal():
    assert lec6.is_palindrome("a") == True
    assert lec6.is_palindrome("ab") == False
    assert lec6.is_palindrome("aba") == True
    assert lec6.is_palindrome("Madam in Eden, I'm Adam") == True
    
def test_freq():
    she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
    'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

    'you', 'think', "you've", 'lost', 'your', 'love',
    'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
    "it's", 'you', "she's", 'thinking', 'of',
    'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

    'she', 'says', 'she', 'loves', 'you',
    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
    'yes', 'she', 'loves', 'you',
    'and', 'you', 'know', 'you', 'should', 'be', 'glad',

    'she', 'said', 'you', 'hurt', 'her', 'so',
    'she', 'almost', 'lost', 'her', 'mind',
    'and', 'now', 'she', 'says', 'she', 'knows',
    "you're", 'not', 'the', 'hurting', 'kind',

    'she', 'says', 'she', 'loves', 'you',
    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
    'yes', 'she', 'loves', 'you',
    'and', 'you', 'know', 'you', 'should', 'be', 'glad',

    'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',

    'you', 'know', "it's", 'up', 'to', 'you',
    'i', 'think', "it's", 'only', 'fair',
    'pride', 'can', 'hurt', 'you', 'too',
    'pologize', 'to', 'her',

    'Because', 'she', 'loves', 'you',
    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
    'Yes', 'she', 'loves', 'you',
    'and', 'you', 'know', 'you', 'should', 'be', 'glad',

    'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    'yeah', 'yeah', 'yeah',
    'yeah', 'yeah', 'yeah', 'yeah'
    ]

    beatles = lec6.lyrics_to_frequencies(she_loves_you)

    assert lec6.words_often(beatles, 5) == [(['you'], 36), (['yeah'], 28), (['she'], 20), (['loves'], 13), (['know'], 11), (['be'], 10), (['and'], 8), (['that', 'should', 'glad'], 7), (['love'], 5)]
##
