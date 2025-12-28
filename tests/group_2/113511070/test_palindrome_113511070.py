from palindrome_113511070 import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("aba") is True

def test_simple_not_palindrome():
    assert is_palindrome("abc") is False

def test_case_insensitive():
    assert is_palindrome("RaceCar") is True

def test_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True

def test_with_non_alnum():
    assert is_palindrome("No 'x' in Nixon") is True

def test_empty_string():
    assert is_palindrome("") is True

