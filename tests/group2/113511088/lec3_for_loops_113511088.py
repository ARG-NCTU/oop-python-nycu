####################
# EXAMPLE: perfect cube
####################

def find_perfect_cube_root(cube: int):
    """
    用 for 迴圈從 0 ~ |cube| 找立方根。
    如果 cube 是 perfect cube，回傳整數立方根；
    否則回傳 None。
    支援負數：例如 cube = -27 -> 回傳 -3。
    """
    limit = abs(cube)
    for guess in range(limit + 1):
        if guess ** 3 == limit:
            # 處理負數
            return guess if cube >= 0 else -guess
    return None


def print_cube_root(cube: int) -> None:
    """
    模仿原本的範例輸出格式：
      如果是 perfect cube:
          Cube root of <cube> is <guess>
      否則：
          <cube> is not a perfect cube
    """
    root = find_perfect_cube_root(cube)
    if root is not None:
        print("Cube root of", cube, "is", root)
    else:
        print(f"{cube} is not a perfect cube")
