def is_palindrome(s):
    """
    Returns True if s is a palindrome, False otherwise.
    """
    # 忽略大小寫
    s = s.lower()

    # 移除非字母數字，只保留 a-z0-9（更符合 palindrome 題目的習慣）
    s = ''.join(c for c in s if c.isalnum())

    return s == s[::-1]


def main():
    """
    讓使用者在 Terminal 輸入字串進行判斷
    """
    word = input("Enter a word to check palindrome: ")

    if is_palindrome(word):
        print(f"'{word}' is a palindrome!")
    else:
        print(f"'{word}' is NOT a palindrome.")


# 讓 python 腳本直接執行時才跑 main()
if __name__ == "__main__":
    main()
