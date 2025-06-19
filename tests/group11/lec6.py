import pytest
from src.mit_ocw_exercises import lec6_recursion_dictionaries as lec6
import add_path  # if your repo requires this to set up sys.path

# --- Test for fib ---
@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (5, 8),
    (6, 13),
])
def test_fib(n, expected):
    assert lec6.fib(n) == expected

# --- Test for fib_mem ---
@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (5, 8),
    (6, 13),
])
def test_fib_mem(n, expected):
    assert lec6.fib_mem(n) == expected

def test_fib_mem_relation():
    assert lec6.fib_mem(5) == lec6.fib_mem(4) + lec6.fib_mem(3)


# --- Test for fib_efficient ---
def test_fib_efficient():
    d = {1: 1, 2: 2}
    assert lec6.fib_efficient(3, d.copy()) == 3
    assert lec6.fib_efficient(6, d.copy()) == 21
    assert lec6.fib_efficient(1, d.copy()) == 1
    assert lec6.fib_efficient(2, d.copy()) == 2

# --- Test for is_palindrome ---
@pytest.mark.parametrize("s, expected", [
    ('eve', True),
    ('Able was I, ere I saw Elba', True),
    ('Is this a palindrome', False),
    ('A man, a plan, a canal, Panama', True),
    ('', True),
    ('a', True),
])
def test_is_palindrome(s, expected):
    assert lec6.is_palindrome(s) is expected

# --- Test for lyrics_to_frequencies ---
def test_lyrics_to_frequencies():
    lyrics = ['hello', 'world', 'hello', 'python']
    result = lec6.lyrics_to_frequencies(lyrics)
    expected = {'hello': 2, 'world': 1, 'python': 1}
    assert result == expected

    lyrics = []
    assert lec6.lyrics_to_frequencies(lyrics) == {}

# --- Test for most_common_words ---
def test_most_common_words():
    freqs = {'a': 5, 'b': 2, 'c': 5}
    words, count = lec6.most_common_words(freqs)
    assert set(words) == {'a', 'c'}
    assert count == 5

    freqs = {'x': 1}
    words, count = lec6.most_common_words(freqs)
    assert words == ['x']
    assert count == 1

# --- Test for words_often ---
def test_words_often():
    freqs = {'a': 5, 'b': 2, 'c': 5, 'd': 1}
    result = lec6.words_often(deepcopy(freqs), 2)
    result_sorted = sorted((sorted(words), count) for words, count in result)
    expected_sorted = sorted((['a', 'c'], 5), (['b'], 2))
    assert result_sorted == expected_sorted

def test_words_often_none():
    freqs = {'a': 1}
    result = lec6.words_often(deepcopy(freqs), 2)
    assert result == [(['a'], 1)]
