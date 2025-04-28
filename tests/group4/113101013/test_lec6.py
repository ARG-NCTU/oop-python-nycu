# === 定義 test_fib: Fibonacci 遞迴函式 ===
def test_fib(x):
    """
    計算 Fibonacci 數列第 x 項
    """
    if x == 0 or x == 1:
        return 1
    else:
        return test_fib(x-1) + test_fib(x-2)


# === 測試 test_fib 小範圍 ===
def test_test_fib_small():
    assert test_fib(0) == 1
    assert test_fib(1) == 1
    assert test_fib(2) == 2
    assert test_fib(3) == 3
    assert test_fib(4) == 5
    assert test_fib(5) == 8


# === 定義 test_is_palindrome 函式（含 to_chars）===
def test_is_palindrome(s):
    """
    判斷字串是否為回文，忽略大小寫與非字母符號
    """
    def to_chars(s):
        s = s.lower()
        return ''.join(c for c in s if c.isalpha())

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))


# === 測試 test_is_palindrome 不同情境 ===
def test_test_is_palindrome_cases():
    # 標準回文測試
    assert test_is_palindrome("racecar")
    assert test_is_palindrome("A man a plan a canal Panama")
    assert test_is_palindrome("No lemon, no melon")

    # 非回文
    assert not test_is_palindrome("banana")
    assert not test_is_palindrome("xyz")

    # 邊界條件
    assert test_is_palindrome("")
    assert test_is_palindrome("x")

    # 含標點與大小寫
    assert test_is_palindrome("Was it a car or a cat I saw?")
