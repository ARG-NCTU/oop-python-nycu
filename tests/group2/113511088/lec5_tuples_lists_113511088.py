#########################
# EXAMPLE: returning a tuple
#########################


def quotient_and_remainder(x, y):
    """
    Function that returns the quotient and remainder of two numbers.

    x: int
    y: int
    returns: tuple (quotient, remainder)
    """
    q = x // y
    r = x % y
    return (q, r)


if __name__ == "__main__":
    # 小 demo：直接跑這個檔案時才會執行
    (quot, rem) = quotient_and_remainder(5, 3)
    print(quot)
    print(rem)
