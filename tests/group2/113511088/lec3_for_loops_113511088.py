####################
# EXAMPLE: approximate cube root
####################


def approximate_cube_root(cube: float, epsilon: float = 0.1, increment: float = 0.01):
    """
    依照題目的 approximate cube root 演算法：
        guess 從 0 開始、每次加 increment
        while abs(guess**3 - cube) >= epsilon and guess <= cube:
            更新 guess 與 num_guesses

    回傳：(guess, num_guesses, success)
      - guess: 最後的猜測值
      - num_guesses: 一共嘗試了幾次
      - success: 是否在誤差 epsilon 以內
    （這個版本只考慮 cube >= 0，和原範例一致）
    """
    guess = 0.0
    num_guesses = 0

    while abs(guess ** 3 - cube) >= epsilon and guess <= cube:
        guess += increment
        num_guesses += 1

    success = abs(guess ** 3 - cube) < epsilon
    return guess, num_guesses, success


def print_approximate_cube_root(
    cube: float, epsilon: float = 0.1, increment: float = 0.01
) -> None:
    """
    完全模仿原來 script 的輸出格式：

        num_guesses = <num_guesses>
        <guess> is close to the cube root of <cube>    (成功)
    或是：
        num_guesses = <num_guesses>
        Failed on cube root of <cube> with these parameters.  (失敗)
    """
    guess, num_guesses, success = approximate_cube_root(cube, epsilon, increment)

    print("num_guesses =", num_guesses)
    if not success:
        print("Failed on cube root of", cube, "with these parameters.")
    else:
        print(guess, "is close to the cube root of", cube)
