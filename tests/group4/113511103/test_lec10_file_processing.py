# tests/group4/113511103/test_lec10_file_processing.py

def count_lines(text):
    return len(text.strip().splitlines())

def extract_words(text):
    words = []
    for line in text.splitlines():
        words.extend(line.strip().split())
    return words

def word_count(text):
    words = extract_words(text)
    return len(words)

# 測試區段

def test_count_lines():
    assert count_lines("a\nb\nc") == 3
    assert count_lines("\n\n") == 0
    assert count_lines("") == 0

def test_extract_words():
    assert extract_words("Hello world") == ["Hello", "world"]
    assert extract_words("a b\nc d") == ["a", "b", "c", "d"]

def test_word_count():
    assert word_count("one two three") == 3
    assert word_count("") == 0
    assert word_count("a\nb c") == 3
