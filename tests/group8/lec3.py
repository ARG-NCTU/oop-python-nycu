import sys, os
###############
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import add_path 
from src.mit_ocw_exercises.lec3_strings_algos import is_palindrome
def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("Racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("ab") == False
    assert is_palindrome("Able was I ere I saw Elba") == True
