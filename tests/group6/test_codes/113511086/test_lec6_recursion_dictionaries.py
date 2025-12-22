def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def is_palindrome(s):
    def to_chars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c.isalpha():
                ans += c
        return ans

    def is_pal(s):
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))


def lyrics_to_frequencies(lyrics):
    freqs = {}
    for word in lyrics:
        if word in freqs:
            freqs[word] += 1
        else:
            freqs[word] = 1
    return freqs


def most_common_words(freqs):
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


def words_often(freqs, min_times):
    result = []
    done = False

    while not done:
        words, count = most_common_words(freqs)
        if count >= min_times:
            result.append((words, count))
            for word in words:
                del freqs[word]
        else:
            done = True

    return result
