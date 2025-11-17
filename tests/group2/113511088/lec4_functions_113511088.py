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

    輸出應該是：
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

    輸出應該是：
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
            # x += 1  # 如果沒 global x 會出錯
        x = 5
        h(x)
        print(x)

    這裡我們只保留「不動到 x」的效果，輸出：
        5
    """
    def h_inner(y):
        pass  # 不動 x

    x = 5
    h_inner(x)
    print(x)
