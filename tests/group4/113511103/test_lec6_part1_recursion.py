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

