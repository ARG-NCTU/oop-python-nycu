# test_dua_lib.py
import pytest
import dua_lib

def test_fib_base_and_recursive():
    # fib(0) 和 fib(1) 都應回傳 1
    assert dua_lib.fib(0) == 1
    assert dua_lib.fib(1) == 1
    # 一般遞迴結果
    assert dua_lib.fib(6) == 13  # 1,1,2,3,5,8,13

def test_fib_efficient_memoization():
    # fib_efficient 只在 d 裡找不到時才計算
    d = {1: 1, 2: 2}
    # 基本值
    assert dua_lib.fib_efficient(1, d) == 1
    assert dua_lib.fib_efficient(2, d) == 2
    # 較大值
    assert dua_lib.fib_efficient(10, d) == 89

@pytest.mark.parametrize("s, expected", [
    ("eve", True),
    ("Able was I, ere I saw Elba", True),
    ("hello", False),
])
def test_is_palindrome(s, expected):
    assert dua_lib.is_palindrome(s) is expected

def test_lyrics_to_frequencies_and_most_common_words():
    # 簡單測試資料
    sample = ["a", "b", "a", "c", "b", "a"]
    freqs = dua_lib.lyrics_to_frequencies(sample)
    # 總次數應等於 list 長度
    assert sum(freqs.values()) == len(sample)
    # 最常出現的字是 'a'，共 3 次
    words, count = dua_lib.most_common_words(freqs)
    assert words == ["a"]
    assert count == 3

def test_words_often():
    sample = ["x", "y", "x", "z", "y", "x", "y"]
    freqs = dua_lib.lyrics_to_frequencies(sample)  # {'x':3,'y':3,'z':1}
    groups = dua_lib.words_often(freqs, 2)
    # 先是 ['x','y'] 各 3 次，再是 ['z'] 1 次，但因 minTimes=2，z 不會被包含
    assert groups == [ (["x","y"], 3) ]

def test_Towers_print_moves(capsys):
    # Towers(2) 應印出兩步：P1→Pspare，P1→P2，Pspare→P2
    dua_lib.Towers(2, "P1", "P2", "PS")
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == [
        "move from P1 to PS",
        "move from P1 to P2",
        "move from PS to P2",
    ]

