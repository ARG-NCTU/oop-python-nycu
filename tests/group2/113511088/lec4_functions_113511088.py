#########################
# EXAMPLE: complicated scope, test yourself!
#########################


def f(x):
    x = x + 1
    print("in f(x): x =", x)
    return x


def run_f_example():
    """
    對應原本：

        x = 3
        z = f(x)
        print('in main program scope: z =', z)
        print('in main program scope: x =', x)
    """
    x = 3
    z = f(x)
    print("in main program scope: z =", z)
    print("in main program scope: x =", x)
    return x, z


def g(x):
    def h(x):
        x = x + 1
        print("in h(x): x = ", x)

    x = x + 1
    print("in g(x): x = ", x)
    h(x)
    return x


def run_g_example():
    """
    對應原本：

        x = 3
        z = g(x)
        print('in main program scope: x = ', x)
        print('in main program scope: z = ', z)
    """
    x = 3
    z = g(x)
    print("in main program scope: x = ", x)
    print("in main program scope: z = ", z)
    return x, z


if __name__ == "__main__":
    # 小 demo：直接執行這個檔案才會跑到這裡
    run_f_example()
    run_g_example()
