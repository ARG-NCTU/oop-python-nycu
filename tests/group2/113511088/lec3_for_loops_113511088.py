####################
# EXAMPLE: for loops over strings
####################

def print_i_or_u_by_index(s: str) -> None:
    """用 index 走訪字串，遇到 i 或 u 就印一句話。"""
    for index in range(len(s)):
        if s[index] == "i" or s[index] == "u":
            print("There is an i or u")


def print_i_or_u_by_char(s: str) -> None:
    """直接用字元走訪字串，遇到 i 或 u 就印一句話。"""
    for char in s:
        if char == "i" or char == "u":
            print("There is an i or u")


####################
# EXAMPLE: while loops and strings
# CHALLENGE: rewrite while loop with a for loop
####################

AN_LETTERS = "aefhilmnorsxAEFHILMNORSX"


def cheer_word(word: str, times: int, an_letters: str = AN_LETTERS) -> None:
    """
    不用 input，而是用參數：
      先對 word 每個字母喊口號，
      再重複印出 times 次 "<word> !!!"
    """
    for char in word:
        if char in an_letters:
            print("Give me an " + char + "! " + char)
        else:
            print("Give me a  " + char + "! " + char)

    print("What does that spell?")
    for _ in range(times):
        print(word, "!!!")


####################
# EXAMPLE: perfect cube
####################

def perfect_cube_root(cube: int):
    """
    最單純的枚舉法：
      從 0 ~ cube 嘗試，找到整數立方剛好等於 cube 就回傳，
      找不到就回傳 None。
    只處理 cube >= 0。
    """
    if cube < 0:
        return None

    for guess in range(cube + 1):
        if guess ** 3 == cube:
            return guess
    return None


####################
# EXAMPLE: guess and check cube root
####################

def guess_and_check_cube_root(cube: int):
    """
    依照原本的 guess-and-check 程式：
      for guess in range(abs(cube)+1):
          if guess**3 >= abs(cube): break
      判斷是否為 perfect cube。
    回傳：
      - 整數立方根（可為負數），如果是 perfect cube
      - None，否則
    """
    abs_cube = abs(cube)
    for guess in range(abs_cube + 1):
        if guess ** 3 >= abs_cube:
            break

    if guess ** 3 != abs_cube:
        return None

    if cube < 0:
        guess = -guess
    return guess


####################
# EXAMPLE: approximate cube root
####################

def approximate_cube_root(
    cube: float,
    epsilon: float = 0.1,
    increment: float = 0.01,
):
    """
    近似立方根：
      guess 從 0 開始，每次加 increment，
      直到 |guess**3 - cube| < epsilon 或 guess > cube。
    回傳 (guess, num_guesses, success)：
      - guess: 最後猜測值
      - num_guesses: 嘗試次數
      - success: 是否在誤差 epsilon 內
    只考慮 cube >= 0（跟原始範例一致）。
    """
    guess = 0.0
    num_guesses = 0

    while abs(guess ** 3 - cube) >= epsilon and guess <= cube:
        guess += increment
        num_guesses += 1

    success = abs(guess ** 3 - cube) < epsilon
    return guess, num_guesses, success


def print_approximate_cube_root(
    cube: float,
    epsilon: float = 0.1,
    increment: float = 0.01,
) -> None:
    """輸出版本，模仿原本 script 的 print 格式。"""
    guess, num_guesses, success = approximate_cube_root(cube, epsilon, increment)
    print("num_guesses =", num_guesses)
    if not success:
        print("Failed on cube root of", cube, "with these parameters.")
    else:
        print(guess, "is close to the cube root of", cube)


####################
# EXAMPLE: bisection cube root (only positive cubes!)
####################

def bisection_cube_root(cube: float, epsilon: float = 0.01):
    """
    使用二分搜尋法找 cube 的立方根：
      low = 0, high = cube
      重複把區間砍半，直到 |guess**3 - cube| < epsilon。
    限制：只處理 cube > 0。
    回傳 (guess, num_guesses)
    """
    if cube <= 0:
        raise ValueError("bisection_cube_root only supports cube > 0.")

    low = 0.0
    high = cube
    guess = (high + low) / 2.0
    num_guesses = 0

    while abs(guess ** 3 - cube) >= epsilon:
        if guess ** 3 < cube:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0
        num_guesses += 1

    return guess, num_guesses


def print_bisection_cube_root(cube: float, epsilon: float = 0.01) -> None:
    """輸出版本，模仿原本 script 的 print 格式。"""
    guess, num_guesses = bisection_cube_root(cube, epsilon)
    print("num_guesses =", num_guesses)
    print(guess, "is close to the cube root of", cube)


####################
# EXTRA: palindrome
####################

def is_palindrome(s: str) -> bool:
    """
    Returns True if s is a palindrome, False otherwise.
    忽略大小寫（全部轉成小寫後再比較）。
    """
    s = s.lower()
    return s == s[::-1]


# 如果你想單獨執行這個檔案做簡單測試，可以用 main 區塊：
if __name__ == "__main__":
    # 小小 demo，交作業時可以留著或註解掉
    print(is_palindrome("Level"))     # True
    print(is_palindrome("Python"))    # False
