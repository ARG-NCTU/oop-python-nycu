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
      for i in range(20): ...
    只是把 20 換成參數 limit。
    """
    print(f"All numbers between 0 and {limit}: even or not")
    for n in range(limit):
        if is_even(n):
            print(n, "even")
        else:
            print(n, "odd")


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
    模仿原本的程式：

        x = 1
        while x <= 10000:
            approx = bisection_cuberoot_approx(x, 0.01)
            print(approx, "is close to cube root of", x)
            x *= 10
    """
    x = start
    while x <= stop:
        approx = bisection_cuberoot_approx(x, epsilon)
        print(approx, "is close to cube root of", x)
        x *= factor


#########################
# EXAMPLE: functions as arguments
#########################


def func_a():
    print("inside func_a")


def func_b(y):
    print("inside func_b")
    return y


def func_c(z):
    print("inside func_c")
    return z()


#########################
# EXAMPLE: returning function objects
#########################


def f():
    """回傳一個把兩個參數相加的函式 x。"""

    def x(a, b):
        return a + b

    return x


#########################
# EXAMPLE: shows accessing variables outside scope
#########################


def scope_example_f():
    """
    對應原本：

        def f(y):
            x = 1
            x += 1
            print(x)
        x = 5
        f(x)
        print(x)

    輸出：
        2
        5
    """

    def f_inner(y):
        x = 1
        x += 1
        print(x)

    x = 5
    f_inner(x)
    print(x)


def scope_example_g():
    """
    對應原本：

        def g(y):
            print(x)
            print(x+1)
        x = 5
        g(x)
        print(x)

    輸出：
        5
        6
        5
    """

    def g_inner(y):
        print(x)
        print(x + 1)

    x = 5
    g_inner(x)
    print(x)


def scope_example_h():
    """
    對應原本：

        def h(y):
            pass
            # x += 1
        x = 5
        h(x)
        print(x)

    這裡只保留「不動到 x」的效果，輸出：
        5
    """

    def h_inner(y):
        pass  # 不動 x

    x = 5
    h_inner(x)
    print(x)


# 直接執行這個檔案時的小 demo（不是 pytest 必要的）
if __name__ == "__main__":
    is_even_with_return(3)
    print(is_even_with_return(3))

    is_even_without_return(3)
    print(is_even_without_return(3))

    print_even_or_not_upto(10)

    print_bisection_cuberoot_series()

    print(func_a())
    print(5 + func_b(2))
    print(func_c(func_a))

    val = f()(3, 4)
    print(val)

    scope_example_f()
    scope_example_g()
    scope_example_h()
