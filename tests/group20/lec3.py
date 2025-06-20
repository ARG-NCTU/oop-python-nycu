def is_palindrome(s):
    """
    Check if a string is a palindrome, ignoring case.
    Args:
        s (str): Input string.
    Returns:
        bool: True if palindrome, False otherwise.
    """
    s = s.lower()
    return s == s[::-1]

def check_vowels(s):
    """
    Check each character in the string for 'i' or 'u'.
    Args:
        s (str): Input string.
    Returns:
        list: List of messages indicating presence of 'i' or 'u'.
    """
    messages = []
    for idx, char in enumerate(s):
        if char.lower() in ['i', 'u']:
            messages.append(f"Position {idx}: Found '{char}' (i or u)")
        else:
            messages.append(f"Position {idx}: No i or u")
    return messages

def cheer_word(word, enthusiasm):
    """
    Generate cheer messages for each character in the word.
    Args:
        word (str): Input word to cheer for.
        enthusiasm (int): Number of times to repeat the final cheer.
    Returns:
        list: List of cheer messages.
    """
    valid_letters = "aefhilmnorsxAEFHILMNORSX"
    messages = []
    for char in word:
        if char in valid_letters:
            messages.append(f"Give me an {char}! {char}")
        else:
            messages.append(f"Give me a {char}! {char}")
    messages.append("What does that spell?")
    for _ in range(max(0, enthusiasm)):
        messages.append(f"{word}!!!")
    return messages

def find_perfect_cube(number):
    """
    Find if a number is a perfect cube.
    Args:
        number (int): Input number.
    Returns:
        dict: {'found': bool, 'root': int or None, 'iterations': int}
    """
    iterations = 0
    for guess in range(number + 1):
        iterations += 1
        if guess ** 3 == number:
            return {"found": True, "root": guess, "iterations": iterations}
    return {"found": False, "root": None, "iterations": iterations}

def guess_cube_root(number):
    """
    Find the cube root of a number using guess and check.
    Args:
        number (int): Input number (positive or negative).
    Returns:
        dict: {'is_perfect': bool, 'root': int or None}
    """
    abs_num = abs(number)
    for guess in range(abs_num + 1):
        if guess ** 3 >= abs_num:
            break
    if guess ** 3 != abs_num:
        return {"is_perfect": False, "root": None}
    if number < 0:
        guess = -guess
    return {"is_perfect": True, "root": guess}

def approximate_cube_root(number, epsilon=0.1, increment=0.01):
    """
    Approximate the cube root using incremental search.
    Args:
        number (float): Input number.
        epsilon (float): Tolerance for approximation.
        increment (float): Step size for guessing.
    Returns:
        dict: {'success': bool, 'guess': float, 'iterations': int}
    """
    guess = 0.0
    iterations = 0
    while abs(guess ** 3 - number) >= epsilon and guess <= abs(number):
        guess += increment
        iterations += 1
    return {
        "success": abs(guess ** 3 - number) < epsilon,
        "guess": guess,
        "iterations": iterations
    }

def bisection_cube_root(number, epsilon=0.01):
    """
    Approximate the cube root using bisection search (positive numbers only).
    Args:
        number (float): Positive input number.
        epsilon (float): Tolerance for approximation.
    Returns:
        dict: {'success': bool, 'guess': float, 'iterations': int}
    """
    if number <= 0:
        return {"success": False, "guess": None, "iterations": 0}
    low = 0
    high = max(1, number)
    guess = (low + high) / 2.0
    iterations = 0
    while abs(guess ** 3 - number) >= epsilon and iterations < 10000:
        if guess ** 3 < number:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        iterations += 1
    return {
        "success": abs(guess ** 3 - number) < epsilon,
        "guess": guess,
        "iterations": iterations
    }
