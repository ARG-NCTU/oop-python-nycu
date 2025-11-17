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
    # 不回傳任何東西 → Python 會自動回傳 None


def is_even(i: int) -> bool:
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    remainder = i % 2
    return remainder == 0


def print_even_or_not_upto(limit: int) -> None:
    """
    模仿原本的程式：

        print("All numbers between 0 and 20: even or not")
        for i in range(20):
            ...

    只是把 20 換成 limit 當參數。
    """
    print(f"All numbers between 0 and {limit}: even or not")
    for i in range(limit):
        if is_even(i):
            print(i, "even")
        else:
            print(i, "odd")


# 如果直接執行這個檔案，做一個 demo
if __name__ == "__main__":
    is_even_with_return(3)
    print(is_even_with_return(3))

    is_even_without_return(3)
    print(is_even_without_return(3))

    print_even_or_not_upto(20)
