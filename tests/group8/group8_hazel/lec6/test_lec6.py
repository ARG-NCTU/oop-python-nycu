import pytest
import lec6

def test_fib():
    """assumes x an int >= 0
       returns Fibonacci of x"""
    assert lec6.fib(1)==1
    assert lec6.fib(2)==2
    assert lec6.fib(3)==3
    assert lec6.fib(4)==5

def test_is_palindrome():
    assert lec6.is_palindrome("HazelisaCat")==False
    assert lec6.is_palindrome("HazellezaH")==True

def test_lyrics_to_frequencies():
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
    assert lec6.lyrics_to_frequencies(she_loves_you)==beatles
   
def test_most_common_words():
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

    assert lec6.most_common_words(lec6.lyrics_to_frequencies(she_loves_you)) == (['you'], 36)
    assert lec6.is_palindrome('iamhazellezahmai') == True