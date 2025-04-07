def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primes_below(n):
    return [x for x in range(2, n) if is_prime(x)]

# ===================== 測試區 =====================

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_is_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("A man a plan a canal Panama")
    assert not is_palindrome("hello")

def test_char_frequency():
    assert char_frequency("aabcc") == {'a': 2, 'b': 1, 'c': 2}
    assert char_frequency("") == {}
    assert char_frequency("xyz") == {'x':1, 'y':1, 'z':1}

def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(13)
    assert not is_prime(1)
    assert not is_prime(0)
    assert not is_prime(9)

def test_primes_below():
    assert primes_below(10) == [2, 3, 5, 7]
    assert primes_below(2) == []
    assert primes_below(20) == [2, 3, 5, 7, 11, 13, 17, 19]
