#####################################
# EXAMPLE:  testing for palindrome 回文
#####################################
        
def is_palindrome(s): 

    def to_chars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz': 
                ans = ans + c
        return ans

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1]) 

    return is_pal(to_chars(s))

print(is_palindrome('O-O'))
#
print(is_palindrome('Able was I, ere I saw Elba'))
#
print(is_palindrome('is this a palindromeddddd'))

#####################################
# EXAMPLE: using dictionaries
#          counting frequencies of words in song lyrics
#####################################

def word_frequencies(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


song_lyrics = ['hello', 'world', 'hello', 'python', 'hello', 'code',
               'python', 'is', 'fun', 'world', 'is', 'great',
               'hello', 'python', 'world', 'fun', 'code', 'great']

word_counts = word_frequencies(song_lyrics)


def most_frequent_words(freq_dict):
    max_count = max(freq_dict.values())
    common_words = [word for word, count in freq_dict.items() if count == max_count]
    return common_words, max_count


def frequent_words(freq_dict, min_occurrences):
    result = []
    while True:
        common_words, count = most_frequent_words(freq_dict)
        if count >= min_occurrences:
            result.append((common_words, count))
            for word in common_words:
                del freq_dict[word]
        else:
            break
    return result
print(word_counts)
print(frequent_words(word_counts, 3))

#####################################
# EXAMPLE: comparing fibonacci using memoization
#####################################


def fibonacci_recursive(n):
    """計算費波那契數列的第 n 項，使用基本遞迴"""
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memo(n, memo):
    """計算費波那契數列的第 n 項，使用記憶化 (Memoization)"""
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# 初始化記憶化字典
memo_dict = {0: 1, 1: 1}

# 設定計算數值
n_value = 34

# 測試函式
print("使用基本遞迴:", fibonacci_recursive(n_value))
print("使用記憶化遞迴:", fibonacci_memo(n_value, memo_dict))
