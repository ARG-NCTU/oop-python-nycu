def is_palindrome(s):
    """
    Returns True if s is a palindrome, False otherwise.
    """
    s = s.lower()          # 忽略大小寫
    s = ''.join(c for c in s if c.isalnum())  # 只保留字母和數字
    return s == s[::-1]
