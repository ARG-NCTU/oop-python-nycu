import pytest

def most_common_words(freqs):
    values = freqs.values()
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

def test_most_common_words():
    freqs = {'the': 5, 'and': 3, 'to': 5, 'of': 2}
    result = most_common_words(freqs)
    assert result == (['the', 'to'], 5)

    freqs = {'hello': 1, 'world': 1}
    result = most_common_words(freqs)
    assert result == (['hello', 'world'], 1)

    freqs = {'a': 0, 'b': 0}
    result = most_common_words(freqs)
    assert result == (['a', 'b'], 0)