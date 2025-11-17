####################
# EXAMPLE: bisection cube root (only positive cubes!)
####################


def bisection_cube_root(cube: float, epsilon: float = 0.01):
    """
    用二分搜尋法找 cube 的立方根，模仿題目中的程式：

        low = 0
        high = cube
        guess = (high + low) / 2.0
        while abs(guess**3 - cube) >= epsilon:
            ...

    限制：
        - 僅處理 cube > 0，和原註解一致（only positive cubes）
        - cube < 1 時，原始版本 upper bound < 實際根，所以不保證正確

    回傳：(guess, num_guesses)
        guess       : 最後的猜測值
        num_guesses : while 迴圈跑了幾次
    """
    if cube <= 0:
        raise ValueError("bisection_cube_root only supports cube > 0.")

    low = 0.0
    high = cube
    guess = (high + low) / 2.0
    num_guesses = 0

    while abs(guess ** 3 - cube) >= epsilon:
        if guess ** 3 < cube:
            # look only in upper half search space
            low = guess
        else:
            # look only in lower half search space
            high = guess
        guess = (high + low) / 2.0
        num_guesses += 1

    return guess, num_guesses


def print_bisection_cube_root(cube: float, epsilon: float = 0.01) -> None:
    """
    完全照原本 script 的輸出格式：

        num_guesses = <num_guesses>
        <guess> is close to the cube root of <cube>
    """
    guess, num_guesses = bisection_cube_root(cube, epsilon)
    print("num_guesses =", num_guesses)
    print(guess, "is close to the cube root of", cube)
