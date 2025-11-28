import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lec3_strings_algos

def test_is_palindrome_real():
    assert lec3_strings_algos.is_palindrome("Racecar")
    assert not lec3_strings_algos.is_palindrome("hello")

def test_cheer_word_logic():
    res = lec3_strings_algos.cheer_word("A", 1)
    assert len(res) == 3  # 1 char + 1 question + 1 answer
    assert res[-1] == "A !!!"
