# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:52:34 2016

@author: WELG
"""

#####################################
# EXAMPLE:  Towers of Hanoi
#####################################

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to) 
        Towers(1, fr, to, spare) 
        Towers(n-1, spare, to, fr) 

Towers(4, 'P1', 'P2', 'P3')

#####################################
# EXAMPLE:  fibonacci
#####################################

def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

for i in range(5):
    print(fib(i))
#####################################
# EXAMPLE:  testing for palindrome 回文
#####################################
        
def is_palindrome(s): 

    def to_chars(s):            #turn the sentence into only char
        s = s.lower()           #turn all captial latter into lower case
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz': 
                ans = ans + c
        return ans

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])        #s[-1] is the last char of s, s[1:-1] is the string without the first and last char

    return is_pal(to_chars(s))                              

print(is_palindrome('eve'))
#
print(is_palindrome('Able was I, ere I saw Elba'))
#
print(is_palindrome('Is this a palindrome'))

#####################################
# EXAMPLE: using dictionaries
#          counting frequencies of words in song lyrics
#####################################

def lyrics_to_frequencies(lyrics):
    myDict = {}                 # create an empty dictionary
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1   #words is key, myDict[word] is the value
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

beatles = lyrics_to_frequencies(she_loves_you)

#construct a tuple of the list of keys and the maximum value
def most_common_words(freqs):       #freqs is a dictionary
    if freqs == {}:                 #if freqs is empty, max(freqs.values()) will give an error
        return ([], 0)              #return a tuple of empty list and 0
    else:
        values = freqs.values()         #values is a list of all values in freqs
        best = max(values)              #best is the maximum value in values
        words = []                      #words is a list of keys with same value
        for k in freqs:                 #for k the key in freqs
            if freqs[k] == best:        #freqs[k] is the value of key k, best is the maximum value of freqs
                words.append(k)
        return (words, best)            #return a tuple of the list of keys with the values = maximum value

#construct a list of tuples of the list of keys and the maximum value
def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs) #temp is a tuple of the list of keys and the maximum value
        if temp[1] > minTimes:          #temp[1] is the second element of the tuple
            result.append(temp)         #append the available tuple to result
            for w in temp[0]:           #temp[0] is a list of keys
                del(freqs[w])           #delete the key w from freqs and also delete the value
        else:
            done = True
    return result
    
print(words_often(beatles, 0))

#####################################
# EXAMPLE: comparing fibonacci using memoization
#####################################


def fib_mem(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib_mem(n-1) + fib_mem(n-2)


def fib_efficient(n, d):        #use hash table to store the values of fib(n)
    if n in d:      #if n is a key in d, return d[n]
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans
          
d = {0:1, 1:1}

#the first fib will recalculate one terms many time, second one reduce these redundant works

argToUse = 34
print("")
print('using fib_mem')
print(fib_mem(argToUse))
print("")
print('using fib_efficient')
print(fib_efficient(argToUse, d))
