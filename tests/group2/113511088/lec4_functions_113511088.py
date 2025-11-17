#########################
# EXAMPLE: combinations of print and return
#########################


def is_even_with_return(i: int) -> bool:
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print("with return")
    remainder = i % 2
    return remainder == 0


def is_even_without_return(i: int) -> None:
    """ 
    Input: i, a positive int
    Does not return anything (回傳 None)
    """
    print("without return")
    remainder = i % 2
    # 沒有 return → Python 會自動回傳 None


# Simple is_even function definition
def is_even(i: int) -> bool:
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    remainder = i % 2
    return remainder == 0


def print_even_or_not_upto(limit: int) -> None:
    """
    模仿原本程式：
      print("All numbers between 0 and 20: even or not")
      for i in range(20):
          ...
    只是把 20 換成參數 limit。
    """
    print(f"All numbers between 0 and {limit}: even or not")
    for i in range(limit):
        if is_even(i):
            print(i, "even")
        else:
            print(i, "odd")


#########################
# EXAMPLE: applying functions to repeat same task many times
#########################


def bisection_cuberoot_approx(x: float, epsilon: float) -> float:
    """
    Input: x, a positive number
    Uses bisection to approximate the cube root of x to within epsilon
    Returns: a float approximating the cube root of x
    """
    low = 0.0
    high = x
    guess = (high + low) / 2.0
    while abs(guess ** 3 - x) >= epsilon:
        if guess ** 3 < x:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0
    return guess


def print_bisection_cuberoot_series(
    start: int = 1, stop: int = 10000, factor: int = 10, epsilon: float = 0.01
) -> None:
    """
    模仿原本程式：

        x = 1
        while x <= 10000:
            approx = bisection_cuberoot_approx(x, 0.01)
            print(approx, "is close to cube root of", x)
            x *= 10

    只是把參數抽出來方便測試。
    """
    x = start
    while x <= stop:
        approx = bisection_cuberoot_approx(x, epsilon)
        print(approx, "is close to cube root of", x)
        x *= factor


# 直接執行這個檔案時的小 demo（交作業不一定要用到）
if __name__ == "__main__":
    # 原本的示範呼叫
    is_even_with_return(3)
    print(is_even_with_return(3))

    is_even_without_return(3)
    print(is_even_without_return(3))

    print_even_or_not_upto(20)

    print_bisection_cuberoot_series()
