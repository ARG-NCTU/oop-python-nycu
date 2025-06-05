

def is_palindrome(s):
    """
    Returns True if s is a palindrome, False otherwise
    """
    s = s.lower()  # 忽略大小寫
    return s == s[::-1]