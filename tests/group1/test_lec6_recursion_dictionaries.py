import pytest
import time
from examples import Towers, fib, is_palindrome, lyrics_to_frequencies, most_common_words, words_often, fib_efficient

# 假設您的原始程式碼檔案名為 examples.py
# 如果不是，請將上方 'from examples import ...' 替換為正確的檔案名

# --- Helper function to capture print output for Towers of Hanoi ---
def get_towers_moves(n, fr, to, spare, capsys):
    """Executes Towers and captures print output."""
    Towers(n, fr, to, spare)
    captured = capsys.readouterr()
    return captured.out.strip().split('\n')

# --- 1. Towers of Hanoi Test ---
def test_towers_of_hanoi_moves(capsys):
    """Tests the sequence of moves for Towers of Hanoi."""
    # Test for 1 disk
    moves_1 = get_towers_moves(1, 'A', 'C', 'B', capsys)
    assert len(moves_1) == 1
    assert moves_1[0] == 'move from A to C'

    # Test for 2 disks
    moves_2 = get_towers_moves(2, 'A', 'C', 'B', capsys)
    assert len(moves_2) == 3 # $2^2 - 1 = 3$ moves
    assert moves_2 == [
        'move from A to B',
        'move from A to C',
        'move from B to C'
    ]
    
    # Test for 3 disks
    moves_3 = get_towers_moves(3, 'P1', 'P3', 'P2', capsys)
    assert len(moves_3) == 7 # $2^3 - 1 = 7$ moves
    # Check the first and last move
    assert moves_3[0] == 'move from P1 to P3'
    assert moves_3[-1] == 'move from P2 to P3'


# --- 2. Fibonacci Tests ---
def test_fib_standard():
    """Tests the standard recursive fib function."""
    # Given the definition F(0)=1, F(1)=1
    assert fib(0) == 1
    assert fib(1) == 1
    # F(2) = F(1) + F(0) = 1 + 1 = 2
    assert fib(2) == 2
    # F(5) = F(4) + F(3) = 5 + 3 = 8
    assert fib(5) == 8
    # F(10) = 89
    assert fib(10) == 89
    
    # Test for negative input (should ideally raise error, but based on docstring ">= 0")
    # We stick to valid inputs per docstring.
    
def test_fib_efficient_memoization():
    """Tests the memoization version of fib."""
    d = {1: 1, 2: 2} # Initial dictionary with base cases F(1)=1, F(2)=2
    
    # Using the standard definition F(1)=1, F(2)=2, F(n) = F(n-1) + F(n-2)
    # Note: The original 'fib' has F(0)=1, F(1)=1. The 'fib_efficient' seems to use F(1)=1, F(2)=2.
    # We must use the base cases provided in the original code for consistency.
    d_eff = {1: 1, 2: 2}
    
    assert fib_efficient(1, d_eff) == 1
    assert fib_efficient(2, d_eff) == 2
    
    # F(3) = F(2) + F(1) = 2 + 1 = 3
    assert fib_efficient(3, d_eff) == 3
    # F(5) = 5
    assert fib_efficient(5, d_eff) == 5
    # F(10) = 55
    assert fib_efficient(10, d_eff) == 55
    
    # Test if memoization is actually used (by checking if the dictionary is populated)
    # The dictionary should contain results up to 10
    assert len(d_eff) == 10
    assert d_eff[10] == 55
    

# --- 3. Palindrome Tests ---
def test_is_palindrome():
    """Tests the recursive palindrome checker."""
    # Palindromes
    assert is_palindrome('eve') == True
    assert is_palindrome('Able was I, ere I saw Elba') == True # Should handle spaces, case, and punctuation
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    
    # Non-palindromes
    assert is_palindrome('Is this a palindrome') == False
    assert is_palindrome('test') == False
    assert is_palindrome('hello world') == False

# --- 4. Dictionary / Word Frequency Tests ---
def test_lyrics_to_frequencies():
    """Tests the function that creates the frequency dictionary."""
    test_lyrics = ['she', 'loves', 'you', 'yeah', 'yeah', 'she', 'you', 'love']
    freqs = lyrics_to_frequencies(test_lyrics)
    
    assert freqs['she'] == 2
    assert freqs['loves'] == 1
    assert freqs['you'] == 2
    assert freqs['yeah'] == 2
    assert freqs['love'] == 1
    assert len(freqs) == 5 # 5 unique words

def test_most_common_words():
    """Tests finding the single most common word(s)."""
    freqs = {'a': 5, 'b': 10, 'c': 5, 'd': 10}
    words, count = most_common_words(freqs)
    
    assert count == 10
    assert sorted(words) == ['b', 'd'] # Should return all words with max count

def test_words_often():
    """Tests finding multiple words above a minimum frequency."""
    freqs = {'cat': 5, 'dog': 12, 'mouse': 3, 'bird': 12, 'fish': 8}
    
    # Check words >= 10 times
    result_high = words_often(freqs.copy(), 10) # Use .copy() to protect original dict
    assert result_high == [(['dog', 'bird'], 12)]
    
    # Check words >= 5 times
    result_medium = words_often(freqs.copy(), 5)
    # The original implementation of words_often groups words by count and removes them, 
    # so we expect the highest counts first.
    assert result_medium == [(['dog', 'bird'], 12), (['fish'], 8), (['cat'], 5)]
    
    # Check no words
    result_none = words_often(freqs.copy(), 20)
    assert result_none == []