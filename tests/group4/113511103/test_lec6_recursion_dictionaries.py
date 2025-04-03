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

# Part 3: lyrics_to_frequencies
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

def test_lyrics_to_frequencies():
    lyrics = ["she", "loves", "you", "yeah", "yeah", "yeah"]
    result = lyrics_to_frequencies(lyrics)
    assert result["she"] == 1
    assert result["yeah"] == 3
    assert result["loves"] == 1

# Part 4: Towers of Hanoi (不 print，改回傳指令)
def towers(n, fr, to, spare, moves=None):
    if moves is None:
        moves = []
    if n == 1:
        moves.append((fr, to))
    else:
        towers(n-1, fr, spare, to, moves)
        towers(1, fr, to, spare, moves)
        towers(n-1, spare, to, fr, moves)
    return moves

def test_towers_3():
    moves = towers(3, 'A', 'C', 'B')
    assert moves == [('A','C'), ('A','B'), ('C','B'), ('A','C'), ('B','A'), ('B','C'), ('A','C')]
    assert len(moves) == 7  # 2^3 - 1

def test_fib_large():
    assert fib(10) == 89
    assert fib(15) == 987

def test_lyrics_empty():
    assert lyrics_to_frequencies([]) == {}

def test_towers_single():
    assert towers(1, 'X', 'Y', 'Z') == [('X', 'Y')]
