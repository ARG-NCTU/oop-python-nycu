####################
# EXAMPLE: guess and check cube root
####################


def guess_and_check_cube_root(cube: int):
    """
    模仿題目中的 guess-and-check 演算法：
      for guess in range(abs(cube)+1):
          if guess**3 >= abs(cube):
              break
      if guess**3 != abs(cube): -> not perfect cube
      else: 處理負號、回傳 guess

    回傳值：
      - 如果 cube 是 perfect cube，回傳整數立方根 (可為負數)
      - 否則回傳 None
    """
    abs_cube = abs(cube)
    for guess in range(abs_cube + 1):
        if guess ** 3 >= abs_cube:
            # 找到第一個立方 >= abs(cube)，就停止搜尋
            break

    if guess ** 3 != abs_cube:
        return None

    # 是 perfect cube，處理負數情況
    if cube < 0:
        guess = -guess
    return guess


def print_guess_and_check_result(cube: int) -> None:
    """
    完全照原本範例的輸出格式：

      如果不是 perfect cube：
          <cube> is not a perfect cube
      如果是：
          Cube root of <cube> is <guess>
    """
    root = guess_and_check_cube_root(cube)
    if root is None:
        print(f"{cube} is not a perfect cube")
    else:
        print("Cube root of " + str(cube) + " is " + str(root))
