import sys
import os
import pytest

# 【關鍵修正】強制把當前資料夾加入 Python 搜尋路徑
# 這樣 import 絕對不會找不到檔案
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 現在可以直接 import 檔名，不用管資料夾結構
import lec3_strings_algos

def test_is_palindrome():
    assert lec3_strings_algos.is_palindrome("Racecar")
    assert not lec3_strings_algos.is_palindrome("python")

def test_cheer_word():
    result = lec3_strings_algos.cheer_word("MIT", 2)
    # 驗證結構
    assert len(result) == 6
    assert "Give me" in result[0]
    assert result[-1] == "MIT !!!"

def test_perfect_cube():
    assert lec3_strings_algos.perfect_cube(27) == 3
