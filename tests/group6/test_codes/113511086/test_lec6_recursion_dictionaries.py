import add_path
import mit_ocw_exercises.lec6_recursion_dictionaries as lec6
import pytest

# =========================
# Tests for fib
# =========================
@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
    (6, 13),
    (7, 21),
    (8, 34),
    (9, 55),
    (10, 89)
])
def test_fib(n, expected):
    assert lec6.fib(n) == expected


# =========================
# Tests for is_palindrome
# =========================
@pytest.mark.parametrize("s,expected", [
    ("eve", True),
    ("Able was I, ere I saw Elba", True),
    ("Is this a palindrome", False),
    ("eillie", True),
    ("cookieliileikooc", True),
    ("owo", True),
    ("ALPHAahpla", True),
    (",\\-=*", True),  # only non-alpha chars => empty string => True
    ("cAwAc", True)
])
def test_is_palindrome(s, expected):
    assert lec6.is_palindrome(s) == expected


# =========================
# Tests for lyrics_to_frequencies
# =========================
def test_lyrics_to_frequencies_basic():
    words = ['wuo', 'due', 'ni', 'i', 'i', 'i', 'bu', 'wan']
    expected = {'wuo': 1, 'due': 1, 'ni': 1, 'i': 3, 'bu': 1, 'wan': 1}
    assert lec6.lyrics_to_frequencies(words) == expected


# =========================
# Tests for most_common_words
# =========================
def test_most_common_words_basic():
    freqs = {'wuo': 1, 'due': 1, 'ni': 1, 'i': 3, 'bu': 1, 'wan': 1}
    assert lec6.most_common_words(freqs) == (['i'], 3)


def test_most_common_words_beatles():
    she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
                     'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                     'she', 'loves', 'you', 'yeah', 'yeah', 'yeah']
    freqs = lec6.lyrics_to_frequencies(she_loves_you)
    assert lec6.most_common_words(freqs) == (['you', 'yeah'], 6)


# =========================
# Tests for words_often
# =========================
def test_words_often_basic():
    freqs = lec6.lyrics_to_frequencies(['wuo', 'due', 'ni', 'i', 'i', 'i', 'bu', 'wan'])
    # words appearing at least 3 times
    assert lec6.words_often(freqs.copy(), 3) == [(['i'], 3)]
    # words appearing at least 2 times
    assert lec6.words_often(freqs.copy(), 2) == [(['i'], 3)]
    # words appearing at least 4 times => none
    assert lec6.words_often(freqs.copy(), 4) == []


# =========================
# Large-scale lyrics test
# =========================
def test_words_often_large():
    she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                     'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                     'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                     'you', 'think', "you've", 'lost', 'your', 'love']
    freqs = lec6.lyrics_to_frequencies(she_loves_you)
    result = lec6.words_often(freqs.copy(), 3)
    # "you" and "yeah" appear 6 times each
    assert (['you', 'yeah'] in [group[0] for group in result])


