import pytest
from lec6_112704050 import tower

def test_tower_moves():
    result = tower(2, "A", "C", "B")
    expected = [
        ("A", "B"),
        ("A", "C"),
        ("B", "C")
    ]
    assert result == expected

def test_tower_move_count():
    for n in range(1, 6):
        result = tower(n, "P1", "P2", "P3")
        expected_moves = 2 ** n - 1
        assert len(result) == expected_moves

from lec6_112704050 import fib2

def test_fib2_base_cases():
    assert fib2(0) == 0
    assert fib2(1) == 1

def test_fib2_recursive_cases():
    assert fib2(2) == 1
    assert fib2(3) == 2
    assert fib2(4) == 3
    assert fib2(5) == 5
    assert fib2(10) == 55
    assert fib2(15) == 610
    assert fib2(19) == 4181

from lec6_112704050 import palindrome_check

def test_palindrome_check():
    assert palindrome_check("aba") == True
    assert palindrome_check("abc") == False
    assert palindrome_check("ab ba") == True
    assert palindrome_check("abb a") == True
    assert palindrome_check("ab,b a") == True
    assert palindrome_check("abccccba") == True
    assert palindrome_check("ab,b, ./'a") == True
    assert palindrome_check("ab    b a") == True
    assert palindrome_check("abx,lcswwa") == False
    assert palindrome_check("aa") == True
    assert palindrome_check("a123321a") == True
    assert palindrome_check("09iw990wi") == True
    assert palindrome_check("-=1-2-=-=-=qwwq") == True

from lec6_112704050 import news_to_frequencies, find_the_most_common_words


def test_news_to_frequencies_removal():
    sample_news = ["hello", "world", "hello", "news", "data", "test",
    "test", "test", "data" , "data", "data", "data", "data", "world", "world", "world"]

    result = news_to_frequencies(sample_news)
    # 應該刪除出現小於等於 5 次的單字，這裡"news"只出現1次應被移除
    assert "news" not in result
    assert "hello" not in result
    assert "world" not in result
    assert "test" not in result
    assert result == {"data": 6}

    sample_news2 = [
    "apple", "banana", "cherry", "apple", "banana", "apple", "banana",
    "apple", "banana", "apple", "banana",  # apple, banana 各出現 5次以上
    "date", "elderberry", "fig",
    "grape", "apple", "banana", "fig",
    "cherry", "cherry", "date", "grape", "fig", "apple", "banana",
    ]
    result = news_to_frequencies(sample_news2)
    assert "cherry" not in result
    assert "date" not in result
    assert "elderberry" not in result
    assert "fig" not in result
    assert "grape" not in result
    assert "fig" not in result
    assert result == {"apple": 7 , "banana": 7}

    sample_news3 = ["apple", "banana", "cherry", "apple", "banana", "apple", "banana",]
    result = news_to_frequencies(sample_news3)
    assert "cherry" not in result
    assert "apple" not in result
    assert "banana" not in result
    assert result == {}

def test_find_the_most_common_words():
    freq = {"a": 3, "b": 5, "c": 5, "d": 1 , "e": 2 , "f": 1} 
    max_words, min_words = find_the_most_common_words(freq)
    assert max_words , min_words == [{"b", "c"} , {"d" , "f"}]
    freq = {"a": 4, "b": 4, "c": 1, "d": 1 , "e": 2 , "f": 1} 
    max_words, min_words = find_the_most_common_words(freq)
    assert max_words , min_words == [{"a", "b"} , {"c" ,"d" , "f"}]
    freq = {"a": 4, "b": 4, "c": 4, "d": 4 , "e": 4 , "f": 4} 
    max_words, min_words = find_the_most_common_words(freq)
    assert max_words , min_words == [{"a", "b", "c", "d", "e", "f"} , {"a", "b", "c", "d", "e", "f"}]