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
    Does not return anything
    """
    print("without return")
    remainder = i % 2
    # 沒有 return → 自動回傳 None


def is_even(i: int) -> bool:
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    remainder = i % 2
    return remainder == 0


def print_even_or_not_upto(limit: int = 20) -> None:
    """
    模仿原始程式：

        print("All numbers between 0 and 20: even or not")
        for i in range(20):
            ...

    只是把 20 改成參數 limit。
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
    Input: x, an integer (or float)
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
    對應原本：

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


def f_return():
    """
    對應原始：

        def f():
            def x(a, b):
                return a+b
            return x
        val = f()(3,4)
        print(val)
    """

    def x(a, b):
        return a + b

    return x


def run_returning_function_example() -> int:
    """
    小 wrapper：模仿
        val = f()(3,4)
        print(val)
    """
    val = f_return()(3, 4)
    print(val)
    return val


#########################
# EXAMPLE: shows accessing variables outside scope
#########################


def scope_example_f():
    """
    原始：

        def f(y):
            x = 1
            x += 1
            print(x)
        x = 5
        f(x)
        print(x)

    期望輸出：
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
    原始：

        def g(y):
            print(x)
            print(x+1)
        x = 5
        g(x)
        print(x)

    期望輸出：
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
    原始：

        def h(y):
            pass
            # x += 1
        x = 5
        h(x)
        print(x)

    我們只保留「不動到 x」的效果，輸出：
        5
    """

    def h_inner(y):
        pass

    x = 5
    h_inner(x)
    print(x)


#########################
# EXAMPLE: harder scope example from slides
#########################


def harder_scope_example():
    """
    原始：

        def g(x):
            def h():
                x = 'abc'
            x = x + 1
            print('in g(x): x =', x)
            h()
            return x

        x = 3
        z = g(x)

    在這裡回傳 (x, z)，方便測試：
        x 應該還是 3
        z 應該是 4
    """

    def g_inner(x):
        def h():
            x_local = "abc"
            return x_local

        x = x + 1
        print("in g(x): x =", x)
        h()
        return x

    x = 3
    z = g_inner(x)
    return x, z


#########################
# EXAMPLE: complicated scope, test yourself!
#########################


def simple_scope_f(x: int) -> int:
    """
    對應第一段的 f(x):

        def f(x):
           x = x + 1
           print('in f(x): x =', x)
           return x
    """
    x = x + 1
    print("in f(x): x =", x)
    return x


def run_simple_scope_example():
    """
    對應：

        x = 3
        z = f(x)
        print('in main program scope: z =', z)
        print('in main program scope: x =', x)
    """
    x = 3
    z = simple_scope_f(x)
    print("in main program scope: z =", z)
    print("in main program scope: x =", x)
    return x, z


def nested_scope_g(x: int) -> int:
    """
    對應第二段的 g(x)/h(x)：
        def g(x):
            def h(x):
                x = x+1
                print("in h(x): x = ", x)
            x = x + 1
            print('in g(x): x = ', x)
            h(x)
            return x
    """

    def h(x_inner):
        x_inner = x_inner + 1
        print("in h(x): x = ", x_inner)

    x = x + 1
    print("in g(x): x = ", x)
    h(x)
    return x


def run_nested_scope_example():
    """
    對應：

        x = 3
        z = g(x)
        print('in main program scope: x = ', x)
        print('in main program scope: z = ', z)
    """
    x = 3
    z = nested_scope_g(x)
    print("in main program scope: x = ", x)
    print("in main program scope: z = ", z)
    return x, z


if __name__ == "__main__":
    # 可選：直接跑整份檔案時的小 demo
    print_even_or_not_upto(20)
    print_bisection_cuberoot_series()
    func_a()
    print(func_a())
    print(5 + func_b(2))
    print(func_c(func_a))
    run_returning_function_example()
    scope_example_f()
    scope_example_g()
    scope_example_h()
    print(harder_scope_example())
    run_simple_scope_example()
    run_nested_scope_example()
