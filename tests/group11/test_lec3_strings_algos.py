import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lec3_strings_algos import is_palindrome

def test_is_palindrome():
    """測試回文偵測"""
    # 基本回文
    assert is_palindrome('aba') is True
    assert is_palindrome('noon') is True
    
    # 忽略大小寫 (原始碼中有 s.lower())
    assert is_palindrome('Noon') is True
    assert is_palindrome('AbA') is True
    
    # 非回文
    assert is_palindrome('abc') is False
    assert is_palindrome('hello') is False
    
    # 空字串 (通常視為回文)
    assert is_palindrome('') is True
    
    # 單一字元
    assert is_palindrome('a') is True
