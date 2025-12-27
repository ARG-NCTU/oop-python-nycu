# -*- coding: utf-8 -*-
"""
Modified on Thu Dec 25 2025
Original Author: WELG
"""

import time
import sys

# NOTE: Commented out local dependency to ensure script runs standalone.
# from add_path import add_path
# add_path()

# Increase recursion limit for deep recursive calls (e.g., inefficient fib)
sys.setrecursionlimit(2000)

# ==============================================================================
# 1. Towers of Hanoi 🗼
# ==============================================================================

def print_move(source: str, target: str):
    """Output the move in English."""
    print(f'move from {source} to {target}')

def towers_of_hanoi(n: int, source: str, target: str, spare: str):
    """
    Recursively solves the Towers of Hanoi problem.
    """
    if n == 1:
        print_move(source, target)
    else:
        # 1. Move n-1 disks from source to spare
        towers_of_hanoi(n - 1, source, spare, target)
        # 2. Move the largest disk (n) from source to target
        towers_of_hanoi(1, source, target, spare)
        # 3. Move n-1 disks from spare to target
        towers_of_hanoi(n - 1, spare, target, source)

# ==============================================================================
# 2. Fibonacci Sequence (Recursion vs. Memoization) ⏱️
# ==============================================================================

def fib_recursive(x: int) -> int:
    """
    Inefficient recursive Fibonacci.
    Assumes F(0)=1, F(1)=1.
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib_recursive(x - 1) + fib_recursive(x - 2)

def fib_efficient(n: int, memo: dict) -> int:
    """
    Efficient recursive Fibonacci using memoization.
    """
    if n in memo:
        return memo[n]
    else:
        ans = fib_efficient(n - 1, memo) + fib_efficient(n - 2, memo)
        memo[n] = ans
        return ans

# ==============================================================================
# 3. Palindrome Check 🔄
# ==============================================================================

def is_palindrome(s: str) -> bool:
    """
    Checks if a string s is a palindrome, ignoring non-letters and case.
    """
    def to_chars(text):
        # Keep only lowercase alphabetic characters
        text = text.lower()
        return ''.join(c for c in text if c.isalpha())

    def is_pal(text):
        if len(text) <= 1:
            return True
        else:
            return text[0] == text[-1] and is_pal(text[1:-1])

    return is_pal(to_chars(s))

# ==============================================================================
# 4. Word Frequency Analysis 📊
# ==============================================================================

def lyrics_to_frequencies(lyrics: list) -> dict:
    """Returns a dictionary of word frequencies from a list of words."""
    freq_dict = {}
    for word in lyrics:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict

def most_common_words(freqs: dict):
    """Finds the word(s) with the highest frequency."""
    if not freqs:
        return ([], 0)
    best_count = max(freqs.values())
    words = [k for k, v in freqs.items() if v == best_count]
    return (words, best_count)

def words_often(freqs: dict, min_times: int) -> list:
    """
    Finds all words appearing at least min_times.
    Returns a list of tuples: ([words], count)
    """
    result = []
    # Work on a copy to avoid modifying the original dictionary
    freqs_copy = freqs.copy()
    
    while freqs_copy:
        words, count = most_common_words(freqs_copy)
        if count >= min_times:
            result.append((words, count))
            # Remove these words to find the next most common
            for w in words:
                del freqs_copy[w]
        else:
            # If the most common remaining word is below threshold, we are done
            break
            
    return result

# ==============================================================================
# Main Execution
# ==============================================================================

def main():
    print("=" * 60)
    print(f"{'💻 PROGRAM EXAMPLES OUTPUT 📈':^60}")
    print("=" * 60)

    # --- 1. Towers of Hanoi ---
    print("\n## 1. Towers of Hanoi (4 disks, P1 to P2)")
    print("-" * 40)
    towers_of_hanoi(4, 'P1', 'P2', 'P3')

    # --- 2. Palindrome Check ---
    print("\n## 2. Palindrome Check")
    print("-" * 40)
    test_strings = [
        "eve",
        "Able was I, ere I saw Elba",
        "Is this a palindrome"
    ]
    for s in test_strings:
        print(f"'{s}' is palindrome? -> {is_palindrome(s)}")

    # --- 3. Word Frequency ---
    print("\n## 3. Word Frequency Analysis (Beatles 'She Loves You')")
    print("-" * 40)
    
    she_loves_you = [
        'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
        'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
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

    beatles_freqs = lyrics_to_frequencies(she_loves_you)
    print(f"Total words: {len(she_loves_you)}")
    print(f"Unique words: {len(beatles_freqs)}")

    min_count = 5
    print(f"\nWords appearing >= {min_count} times:")
    results = words_often(beatles_freqs, min_count)
    for words, count in results:
        print(f"  Count {count:2d}: {', '.join(words)}")

    # --- 4. Fibonacci Efficiency ---
    print("\n## 4. Comparing Fibonacci Efficiency")
    print("-" * 40)
    
    # We compare the calculation of F(34)
    # Recursion tree grows exponentially (O(2^n)), leading to redundant calculations.
    # Memoization stores results (O(n)), calculating each state only once.
    

    target_n = 34
    print(f"Calculating F({target_n})...")

    # Inefficient Recursion
    print(f"\n[Standard Recursion]")
    start_time = time.perf_counter()
    try:
        val_rec = fib_recursive(target_n)
        end_time = time.perf_counter()
        print(f"  Result: {val_rec}")
        print(f"  Time  : {end_time - start_time:.6f} seconds")
    except RecursionError:
        print("  Error : Recursion depth exceeded.")

    # Efficient Memoization
    # Initialize base cases: F(0)=1, F(1)=1 to match the recursive version
    print(f"\n[Memoization]")
    memo_dict = {0: 1, 1: 1}
    start_time = time.perf_counter()
    val_memo = fib_efficient(target_n, memo_dict)
    end_time = time.perf_counter()
    print(f"  Result: {val_memo}")
    print(f"  Time  : {end_time - start_time:.6f} seconds")

    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()