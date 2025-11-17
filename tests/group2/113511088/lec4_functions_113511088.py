#########################
# EXAMPLE: harder scope example from slides
#########################


def g(x):
    """
    原始範例：

        def g(x):
            def h():
                x = 'abc'
            x = x + 1
            print('in g(x): x =', x)
            h()
            return x
    """
    def h():
        # 這個 x 其實是 h 裡面的「區域變數」
        # 不會改到 g 外面的 x
        x_local = "abc"
        return x_local

    x = x + 1
    print("in g(x): x =", x)
    h()
    return x


def harder_scope_example():
    """
    模擬原本 script：

        x = 3
        z = g(x)

    回傳 (x, z)，方便在 pytest 裡檢查。
    """
    x = 3
    z = g(x)
    return x, z


if __name__ == "__main__":
    # 小 demo：直接執行這個檔案時會看到行為
    x_out, z_out = harder_scope_example()
    print("outside x:", x_out)
    print("z:", z_out)
