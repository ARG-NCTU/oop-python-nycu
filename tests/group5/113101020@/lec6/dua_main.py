# -*- coding: utf-8 -*-
"""
main.py：測試 dua_lib.py 中的函式範例執行檔
"""

import dua_lib

if __name__ == '__main__':
    # 1. 測試 Towers of Hanoi
    print("===== Towers of Hanoi (n=3) =====")
    dua_lib.Towers(3, 'P1', 'P2', 'P3')
    print()

    # 2. 測試遞迴 Fibonacci
    x = 6
    print(f"fib({x}) = {dua_lib.fib(x)}")
    print()

    # 3. 測試迴文判斷
    test_strings = ['eve', 'Able was I, ere I saw Elba', 'hello']
    print("===== Palindrome 測試 =====")
    for s in test_strings:
        print(f"is_palindrome({s!r}) → {dua_lib.is_palindrome(s)}")
    print()

    # 4. 詞頻統計與最常見單字
    freqs = dua_lib.lyrics_to_frequencies(dua_lib.she_loves_you)
    common, count = dua_lib.most_common_words(freqs)
    print("===== 最常出現的單字 =====")
    print(f"單字：{common}，次數：{count}")
    print()

    # 5. 找出至少出現 5 次的單字群
    freqs = dua_lib.lyrics_to_frequencies(dua_lib.she_loves_you)
    groups = dua_lib.words_often(freqs, 5)
    print("===== 依序找出 ≥5 次出現的單字群 =====")
    for words, times in groups:
        print(f"  單字：{words}，次數：{times}")
    print()

    # 6. 測試帶備忘錄的高效 Fibonacci
    d = {1: 1, 2: 2}
    n = 34
    print("===== 高效 Fibonacci (memoization) =====")
    print(f"fib_efficient({n}) = {dua_lib.fib_efficient(n, d)}")

