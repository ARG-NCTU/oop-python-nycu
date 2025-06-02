def towers_of_hanoi(n, fr, to, spare):
    moves = []
    def move(n, fr, to, spare):
        if n == 1:
            moves.append(f"move from {fr} to {to}")
        else:
            move(n-1, fr, spare, to)
            move(1, fr, to, spare)
            move(n-1, spare, to, fr)
    move(n, fr, to, spare)
    return moves

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def is_palindrome(s):
    def to_chars(s):
        return ''.join(c.lower() for c in s if c.isalpha())

    def is_pal(s):
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))

def lyrics_to_frequencies(lyrics):
    freqs = {}
    for word in lyrics:
        freqs[word] = freqs.get(word, 0) + 1
    return freqs

def most_common_words(freqs):
    best = max(freqs.values())
    words = [k for k in freqs if freqs[k] == best]
    return (words, best)

def words_often(freqs, min_times):
    result = []
    freqs = freqs.copy()
    while True:
        words, count = most_common_words(freqs)
        if count >= min_times:
            result.append((words, count))
            for w in words:
                del freqs[w]
        else:
            break
    return result

def fib_mem(n):
    if n == 0 or n == 1:
        return 1
    return fib_mem(n - 1) + fib_mem(n - 2)


def fib_efficient(n, d=None):
    if d is None:
        d = {0: 1, 1: 1}
    if n in d:
        return d[n]
    d[n] = fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
    return d[n]

