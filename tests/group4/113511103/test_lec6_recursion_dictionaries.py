# Part 1: Fibonacci
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def test_fib_basic():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 3
    assert fib(5) == 8

# Part 2: is_palindrome
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

def test_is_palindrome():
    assert is_palindrome("Able was I, ere I saw Elba")
    assert is_palindrome("racecar")
    assert not is_palindrome("python")
    assert is_palindrome("a")
    assert is_palindrome("")
