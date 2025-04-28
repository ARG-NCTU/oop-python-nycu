#####################################
# EXAMPLE:  Towers of Hanoi
#####################################
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare): # P1 -> P2
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to) # P1 -> P3
        Towers(1, fr, to, spare)   # P1 -> P2
        Towers(n-1, spare, to, fr) # P3 -> P2

Towers(4, 'P1', 'P2', 'P3') # From P1 -> P2, P3 spare

#####################################
# EXAMPLE:  fibonacci
#####################################

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def test_fib():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 3
    assert fib(4) == 5
    assert fib(5) == 8
    assert fib(6) == 13
    assert fib(7) == 21
    assert fib(8) == 34
    assert fib(9) == 55

#####################################
# EXAMPLE:  testing for palindrome 回文
#####################################

def is_palindrome(s):
    # 把字串全部變小寫＋去掉非字母的字元
    def to_chars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    # 判斷是否為回文
    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1]) #

    return is_pal(to_chars(s))

def test_is_palindrome():
    assert is_palindrome('eve') == True
    assert is_palindrome('Able was I, ere I saw Elba') == True
    assert is_palindrome('Is this a palindrome') == False

#####################################
# EXAMPLE: using dictionaries
#          counting frequencies of words in song lyrics
#####################################

def lyrics_to_frequencies(lyrics):
    # Like: {'she': 20, 'loves': 13, 'you': 36, 'yeah': 28, ...}
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah',
'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]

def test_lyrics_to_frequencies():
    beatles = lyrics_to_frequencies(she_loves_you)
    assert beatles['she'] == 20
    assert beatles['loves'] == 13
    assert beatles['you'] == 36

def most_common_words(freqs):
    best = max(freqs.values())
    words = []
    # 逐一檢查所有跟best數量一樣多的word
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

def test_most_common_words():
    beatles = lyrics_to_frequencies(she_loves_you)
    # e.g. beatles[0] == ['you', 'she'...]
    #      beatles[1] == 36
    assert most_common_words(beatles) == (['you'], 36)

def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes: # 若字典中的某個word數量超過minTimes
            result.append(temp) # 把這個word加入result
            for w in temp[0]:   # 把這個word從字典中刪除
                del(freqs[w])
        else:
            done = True
    return result

def test_words_often():
    beatles = lyrics_to_frequencies(she_loves_you)
    result = words_often(beatles, 5)
    assert result[0] == (['you'], 36)
    assert result[1] == (['yeah'], 28)

#####################################
# EXAMPLE: comparing fibonacci using memoization
#####################################
def fib_mem(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)

def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans

def test_fib():
    d = {1:1, 2:2} # Key:Value = 1:1, 2:2
    argToUse = 34
    assert fib(argToUse) == 9227465
    assert fib_efficient(argToUse, d) == 9227465