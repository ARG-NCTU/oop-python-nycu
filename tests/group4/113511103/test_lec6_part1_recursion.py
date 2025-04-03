# === Commit 1: 定義 Fibonacci 遞迴函式 ===
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

# === Commit 2: 測試 Fibonacci ===
def test_fib_small():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 3

# === Commit 3: 定義 is_palindrome 函式（含 to_chars）===
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
