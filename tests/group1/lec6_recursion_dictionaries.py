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
    """Print a move instruction from one peg to another.
    
    Args:
        fr: Source peg identifier
        to: Destination peg identifier
    """
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    """Recursively solves the Towers of Hanoi problem.
    
    Args:
        n: Number of disks (int > 0)
        fr: Source peg identifier
        to: Destination peg identifier
        spare: Auxiliary peg identifier
    
    Raises:
        ValueError: If n is not a positive integer
    """
    if n <= 0:
        raise ValueError(f"Number of disks must be positive, got {n}")
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
# EXAMPLE:  fibonacci (Inefficient recursion)
#####################################

def fib(x):
    """Calculate Fibonacci number using naive recursion.
    
    WARNING: This is very inefficient for large x due to exponential time complexity.
    Use fib_efficient() with memoization for x >= 20.
    
    Args:
        x: Non-negative integer
    
    Returns:
        Fibonacci number at position x (F(0)=1, F(1)=1)
    
    Raises:
        ValueError: If x is negative
    """
    if x < 0:
        raise ValueError(f"Fibonacci index must be non-negative, got {x}")
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
        
#####################################
# EXAMPLE:  testing for palindrome
#####################################
        
def is_palindrome(s): 
    """Check if a string is a palindrome, ignoring non-letters and case.
    
    Args:
        s: String to check
    
    Returns:
        True if s is a palindrome (ignoring non-alphanumeric chars and case), False otherwise
    """
    def to_chars(s):
        """Convert string to lowercase letters only."""
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz': 
                ans = ans + c
        return ans

    def is_pal(s):
        """Recursively check if string s is a palindrome."""
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1]) 

    return is_pal(to_chars(s))

#####################################
# EXAMPLE: using dictionaries - counting frequencies of words
#####################################

def lyrics_to_frequencies(lyrics):
    """Convert a list of words into a frequency dictionary.
    
    Args:
        lyrics: List of words (strings)
    
    Returns:
        Dictionary mapping words to their frequencies
    
    Raises:
        ValueError: If lyrics is empty
    """
    if not lyrics:
        raise ValueError("lyrics list cannot be empty")
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
    """Find the word(s) appearing most frequently.
    
    Args:
        freqs: Dictionary mapping words to frequencies
    
    Returns:
        Tuple (list of words with max frequency, max frequency count)
    
    Raises:
        ValueError: If freqs dictionary is empty
    """
    if not freqs:
        raise ValueError("frequencies dictionary cannot be empty")
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)
    
def words_often(freqs, minTimes):
    """Find all words appearing at least minTimes in frequency dictionary.
    
    Args:
        freqs: Dictionary mapping words to frequencies
        minTimes: Minimum frequency threshold (int > 0)
    
    Returns:
        List of tuples (words, frequency) for words appearing >= minTimes
    
    Raises:
        ValueError: If minTimes is not positive
    """
    if minTimes <= 0:
        raise ValueError(f"minTimes must be positive, got {minTimes}")
    
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
    """Calculate Fibonacci number efficiently using memoization.
    
    This approach dramatically improves performance by caching results,
    reducing time complexity from O(2^n) to O(n).
    
    Args:
        n: Non-negative integer for Fibonacci calculation
        d: Dictionary for memoization (should contain {1: 1, 2: 2} as base cases)
    
    Returns:
        Fibonacci number at position n
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError(f"Fibonacci index must be non-negative, got {n}")
    if n in d:
        return d[n] 
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans


def compare_fib_performance(n, max_recursion_depth=2000):
    """Compare performance of naive vs memoized Fibonacci calculation.
    
    Args:
        n: Fibonacci index to calculate
        max_recursion_depth: Maximum recursion depth limit
    
    Returns:
        Dictionary with results from both approaches
    """
    results = {'input': n, 'naive_result': None, 'naive_time': None, 
               'efficient_result': None, 'efficient_time': None, 'speedup': None}
    
    # Try naive approach
    if n <= 25:  # Only for small values to avoid excessive computation
        print(f"\nUsing fib (Standard Recursion) for F({n}):")
        start_time = time.time()
        try:
            results['naive_result'] = fib(n)
            results['naive_time'] = time.time() - start_time
            print(f"F({n}) = {results['naive_result']}")
            print(f"Time taken: {results['naive_time']:.6f} seconds")
        except RecursionError:
            print("RecursionError: Recursion depth exceeded.")
            results['naive_time'] = float('inf')
    else:
        print(f"\nSkipping naive approach for F({n}) (would be too slow)")
    
    # Memoized approach
    d = {1: 1, 2: 2}
    print(f"\nUsing fib_efficient (Memoization) for F({n}):")
    start_time = time.time()
    results['efficient_result'] = fib_efficient(n, d)
    results['efficient_time'] = time.time() - start_time
    print(f"F({n}) = {results['efficient_result']}")
    print(f"Time taken: {results['efficient_time']:.6f} seconds")
    
    # Calculate speedup if both methods completed
    if results['naive_time'] and results['efficient_time']:
        results['speedup'] = results['naive_time'] / results['efficient_time']
        print(f"Speedup: {results['speedup']:.2f}x faster with memoization")
    
    return results
        


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

# Use the new comparison utility function
results = compare_fib_performance(argToUse)
print("="*50)