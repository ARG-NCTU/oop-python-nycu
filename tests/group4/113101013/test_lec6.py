# === Lecture code (自包含) ===

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

def is_palindrome(s):
    def to_chars(s):
        s = s.lower()
        return ''.join([c for c in s if c.isalpha()])
    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])
    return is_pal(to_chars(s))

# === Tests ===

def test_fib_small():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 3
    assert fib(4) == 5
    assert fib(5) == 8

def test_is_palindrome_cases():
    # 一般情境
    assert is_palindrome("racecar")
    assert is_palindrome("A man a plan a canal Panama")
    assert not is_palindrome("banana")

    # 邊界與極簡測試
    assert is_palindrome("")
    assert is_palindrome("x")
    assert not is_palindrome("xyz")

    # 特殊標點與大小寫
    assert is_palindrome("Was it a car or a cat I saw?")
    assert is_palindrome("No lemon, no melon")
