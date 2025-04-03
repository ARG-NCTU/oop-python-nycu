# === Commit 1: 定義 Fibonacci 遞迴函式 ===
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
