# 113511253 - Corrected Implementation

def is_palindrome(s):
    """
    Checks if a string is a palindrome, ignoring case and non-alphabetic characters.
    """
    # 修正邏輯：先轉小寫，並只保留英文字母
    clean_s = ''.join(c.lower() for c in s if c.isalpha())
    return clean_s == clean_s[::-1]

def find_vowels(s):
    """
    Returns a list of indices where vowels occur.
    """
    vowels = 'aeiouAEIOU'
    return [i for i, char in enumerate(s) if char in vowels]

def cheer_word(word, n):
    """
    Prints a cheer for the word n times.
    """
    output = ""
    for char in word:
        line = f"Give me an {char}! {char}"
        print(line)
        output += line + "\n"
    print("What does that spell?")
    print(f"{word}!")
    return output

def perfect_cube(cube):
    """
    Uses guess and check to find perfect cube root.
    """
    cube = int(cube)
    for guess in range(abs(cube) + 1):
        if guess**3 == abs(cube):
            if cube < 0:
                return -guess
            return guess
    return None

def guess_and_check_cube_root(cube):
    return perfect_cube(cube)

def approximate_cube_root(cube, epsilon=0.01):
    """
    Finds an approximation of the cube root.
    """
    guess = cube / 2.0
    while abs(guess**3 - cube) >= epsilon:
        guess = guess - (guess**3 - cube) / (3*guess**2)
    return guess

def bisection_cube_root(cube, epsilon=0.01):
    """
    Uses bisection search to find cube root.
    """
    low = 0.0
    high = cube
    guess = (high + low) / 2.0
    while abs(guess**3 - cube) >= epsilon:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0
    return guess

