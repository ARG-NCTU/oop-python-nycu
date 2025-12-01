# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:52:34 2016
@author: WELG
"""
import time
import sys
from add_path import add_path
add_path()


# Increase recursion limit for potentially deep recursive calls
sys.setrecursionlimit(2000) 

# --- Function Definitions ---

#####################################
# EXAMPLE:  Towers of Hanoi
#####################################

def printMove(fr, to):
    # Output in English
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    """
    Recursively solves the Towers of Hanoi problem.
    """
    if n == 1:
        printMove(fr, to)
    else:
        # 1. Move n-1 disks from fr to spare
        Towers(n-1, fr, spare, to)
        # 2. Move the largest disk (n) from fr to to
        Towers(1, fr, to, spare)
        # 3. Move n-1 disks from spare to to
        Towers(n-1, spare, to, fr)

#####################################
# EXAMPLE:  fibonacci (Inefficient recursion)
#####################################

def fib(x):
    """assumes x an int >= 0; returns Fibonacci of x (F(0)=1, F(1)=1)"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
        
#####################################
# EXAMPLE:  testing for palindrome
#####################################
        
def is_palindrome(s): 
    """Checks if a string s is a palindrome, ignoring non-letters and case."""
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

#####################################
# EXAMPLE: using dictionaries - counting frequencies of words
#####################################

def lyrics_to_frequencies(lyrics):
    """Returns a dictionary of word frequencies from a list of words."""
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

beatles = lyrics_to_frequencies(she_loves_you)


def most_common_words(freqs):
    """Finds the word(s) with the highest frequency."""
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)
    
def words_often(freqs, minTimes):
    """Finds all words appearing at least minTimes."""
    result = []
    freqs_copy = freqs.copy() 
    
    done = False
    while not done and freqs_copy: 
        temp = most_common_words(freqs_copy)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs_copy[w])  
        else:
            done = True
    return result

#####################################
# EXAMPLE: comparing fibonacci using memoization
#####################################

def fib_efficient(n, d):
    """Efficient recursive Fibonacci using memoization (dictionary d)."""
    if n in d:
        return d[n] 
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans
        
# --- Program Execution and English Output ---

print("="*50)
print("           💻 PROGRAM EXAMPLES OUTPUT 📈")
print("="*50)

## 1. Towers of Hanoi 🗼
print("## 1. Towers of Hanoi (4 disks, P1 to P2)")
Towers(4, 'P1', 'P2', 'P3')
print("\n" + "-"*50)

## 2. Palindrome Check 🔄
print("## 2. Palindrome Check (is_palindrome)")
print(f"'{'eve'}' is a palindrome: {is_palindrome('eve')}")
print(f"'{'Able was I, ere I saw Elba'}' is a palindrome: {is_palindrome('Able was I, ere I saw Elba')}")
print(f"'{'Is this a palindrome'}' is a palindrome: {is_palindrome('Is this a palindrome')}")
print("\n" + "-"*50)

## 3. Dictionary: Word Frequency Analysis 📊
print("## 3. Dictionary: Word Frequency Analysis (Beatles 'She Loves You')")
print(f"Total words (including duplicates): {len(she_loves_you)}")
print(f"Total unique words: {len(beatles)}")

min_times = 5
print(f"\nWords appearing >= {min_times} times:")
result = words_often(beatles.copy(), min_times) 
for words, count in result:
    print(f"  Count {count}: {', '.join(words)}")

print("\n" + "-"*50)

## 4. Comparing Fibonacci Efficiency (Recursion vs. Memoization) ⏱️
argToUse = 34
print(f"## 4. Comparing Fibonacci Efficiency (Calculating F({argToUse}))")

# --- Inefficient Recursion ---
print("\nUsing fib (Standard Recursion):")
start_time = time.time()
try:
    result_fib = fib(argToUse)
    end_time = time.time()
    print(f"F({argToUse}) = {result_fib}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
except RecursionError:
    print("RecursionError: Recursion depth exceeded.")

# --- Efficient Recursion (Memoization) ---
d = {1:1, 2:2} 
print("\nUsing fib_efficient (Memoization):")
start_time = time.time()
result_efficient = fib_efficient(argToUse, d)
end_time = time.time()
print(f"F({argToUse}) = {result_efficient}")
print(f"Time taken: {end_time - start_time:.6f} seconds")
print("="*50)