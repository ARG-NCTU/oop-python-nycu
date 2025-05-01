# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:52:34 2016

@author: WELG
"""

#####################################
# EXAMPLE:  Towers of Hanoi
#####################################
#three rods:from, destination, spare
#goal: move n disks from fr to des using spare
def printMove(fr, des):
    print('move from ' + str(fr) + ' to ' + str(des))

#moving 'n' disks from 'fr' to 'des' using 'spare'
def Towers(n, fr, des, spare):
    if n == 1:
        printMove(fr, des)
    else:
        Towers(n-1, fr, spare, des) # move n-1 disks from fr to spare
        Towers(1, fr, des, spare) # move 1 disk from fr to des
        Towers(n-1, spare, des, fr) # move n-1 disks from spare to des

#print(Towers(4, 'P1', 'P2', 'P3'))

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
        
#####################################
# EXAMPLE:  testing for palindrome 回文
#####################################
#function inside a function  (cool!)    
def is_palindrome(s): 

    #moves to lower case and remove non-alphabetic characters
    def to_chars(s):
        s = s.lower() # convert to lower case (小寫)
        ans = '' #a empty string
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz': 
                ans = ans + c
        return ans

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])
            #s[1:-1] is the string s without the first and last character (recursion)
            #s[0] is the first character of s
            #s[-1] is the last character of s !

    return is_pal(to_chars(s))

#print(is_palindrome('eve'))
#
#print(is_palindrome('Able was I, ere I saw Elba'))
#
#print(is_palindrome('Is this a palindrome'))

#####################################
# EXAMPLE: using dictionaries
#          counting frequencies of words in song lyrics
#####################################
#dictionary: a data structure that stores a collection of key-value pairs
#key: a unique index, can be a string, number, or tuple, immutable
#value: the data associated with the key, can be any data type, mutable or immutable
#framework: {key1: value1, key2: value2, ...}
#dictionary is mutable, can be changed after creation
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1 
            #increment the count of the word (value) by 1
        else:
            myDict[word] = 1 
            #create a new entry in the dictionary with the word as key and 1 as value
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


def most_common_words(freqs):
    values = freqs.values() #values() returns a 'list' of all the values in the dictionary
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

#find words in the 'freqs' (dictionary) that appear at least 'minTimes' times 
def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs) #temp is a tuple (words, best), words is a list of words, best is a integer
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])  #delete the word from the dictionary so that it won't be counted again
        else:
            done = True
    return result #result be a list of tuples
    
#print(words_often(beatles, 5))

#####################################
# EXAMPLE: comparing fibonacci using memoization
#####################################
#memoization: a technique used to speed up recursive algorithms by 
#storing the results of expensive function calls and reusing them when the same inputs occur again

def fib_mem(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib_mem(n-1) + fib_mem(n-2)
# mistakes recorrected: change fib_mem instead of fib1

def fib_efficient(n, d):
    if n in d:
        return d[n] #check if n is in the dictionary d, if so, return the value of d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans
#this function will store f(1) to f(n) once it ended
#aimed to reduce redundant calculations    
d = {1:1, 2:2} #dictionary to store the results of fib_efficient, view as a cache, stored f(1) and f(2)

argToUse = 34
#print("")
#print('using fib')
#print(fib(argToUse))
#print("")
#print('using fib_efficient')
#print(fib_efficient(argToUse, d))