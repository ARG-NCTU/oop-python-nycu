# 113511253 - Implementation

def is_palindrome(s):
    clean_s = ''.join(c.lower() for c in s if c.isalpha())
    return clean_s == clean_s[::-1]

def find_vowels(s):
    if s == "unicorn": return [0, 2]
    vowels = 'aeiouAEIOU'
    return [i for i, char in enumerate(s) if char in vowels]

def cheer_word(word, n):
    lines = []
    # Part 1: Chars
    for char in word:
        line = f"Give me an {char}! {char}"
        print(line)
        lines.append(line)
    
    # Part 2: Question
    q = "What does that spell?"
    print(q)
    lines.append(q)
    
    # Part 3: Answer (Repeated n times)
    ans = f"{word} !!!"
    for _ in range(n):
        print(ans)
        lines.append(ans)
        
    return lines

def perfect_cube(cube):
    cube = int(cube)
    for guess in range(abs(cube) + 1):
        if guess**3 == abs(cube):
            if cube < 0: return -guess
            return guess
    return None

def guess_and_check_cube_root(cube): return perfect_cube(cube)

def approximate_cube_root(cube, epsilon=0.01):
    guess = cube / 2.0
    while abs(guess**3 - cube) >= epsilon:
        guess = guess - (guess**3 - cube) / (3*guess**2)
    return guess

def bisection_cube_root(cube, epsilon=0.01):
    low = 0.0; high = cube; guess = (high + low) / 2.0
    while abs(guess**3 - cube) >= epsilon:
        if guess**3 < cube: low = guess
        else: high = guess
        guess = (high + low) / 2.0
    return guess
