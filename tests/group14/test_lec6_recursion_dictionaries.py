import add_path
import mit_ocw_exercises.lec6_recursion_dictionaries as lec6
import pytest

def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(2) == 2
    assert lec6.fib(3) == 3
    assert lec6.fib(4) == 5
    
def test_is_palindrome():
    assert lec6.is_palindrome('eve') == True
    assert lec6.is_palindrome('apple') == False

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
    assert lec6.lyrics_to_frequencies(she_loves_you) == {'she': 20, 'loves': 13, 'you': 36, 'yeah': 28, 'think': 2, "you've": 1, 'lost': 2, 'your': 1, 'love': 5, 'well': 1, 'i': 2, 'saw': 1, 'her': 4, 'yesterday-yi-yay': 1, "it's": 3, "she's": 1, 'thinking': 1, 'of': 1, 'and': 8, 'told': 1, 'me': 1, 'what': 1, 'to': 3, 'say-yi-yay': 1, 'says': 3, 'know': 11, 'that': 7, "can't": 3, 'be': 10, 'bad': 3, 'yes': 2, 'should': 7, 'glad': 7, 'said': 1, 'hurt': 2, 'so': 1, 'almost': 1, 'mind': 1, 'now': 1, 'knows': 1, "you're": 1, 'not': 1, 'the': 1, 'hurting': 1, 'kind': 1, 'oo': 2, 'with': 4, 'a': 4, 'like': 4, 'up': 1, 'only': 1, 'fair': 1, 'pride': 1, 'can': 1, 'too': 1, 'pologize': 1, 'Because': 1, 'Yes': 1}
    
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
    beatles = lec6.lyrics_to_frequencies( she_loves_you )
    assert lec6.most_common_words(beatles) == (['you'], 36)

def test_words_often():
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
    beatles = lec6.lyrics_to_frequencies( she_loves_you )
    assert lec6.words_often(beatles, 5) == [(['you'], 36), (['yeah'], 28), (['she'], 20), (['loves'], 13), (['know'], 11), (['be'], 10), (['and'], 8), (['that', 'should', 'glad'], 7), (['love'], 5)]
    
