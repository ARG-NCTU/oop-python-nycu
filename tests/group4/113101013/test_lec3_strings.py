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

# ===================== test =====================


def test_is_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("A man a plan a canal Panama")
    assert is_palindrome("No lemon, no melon")  # 有逗號與空白
    assert is_palindrome("Was it a car or a cat I saw")  
    assert is_palindrome("")  # 空字串應該是 palindrome
    assert is_palindrome(" ")  # 單空白字串
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
    
def test_is_palindrome_additional():
    # 含標點符號與大小寫混合的字串，測試能否正確判斷
    assert not is_palindrome("Madam, I'm Adam")  # 加逗號與撇號
    assert not is_palindrome("Eva, can I see bees in a cave?")  # 含逗號與問號
    # 含數字與字母的回文
    assert is_palindrome("12321")
    assert not is_palindrome("12345")
    # 空白與標點混合
    assert is_palindrome("A Santa at NASA")
    assert is_palindrome("232 32")  # 數字與空白
    assert not is_palindrome("Hello, World!")  # 含標點符號的非回文

def test_all():
    test_is_palindrome()
    test_char_frequency()
    test_is_prime()
    test_primes_below()
    test_is_palindrome_additional()


