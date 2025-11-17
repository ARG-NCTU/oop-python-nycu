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


#########################
# EXAMPLE: iterating over tuples
#########################


def get_data(aTuple):
    """
    aTuple: tuple of tuples (int, string)

    Extracts all integers from aTuple and sets
    them as elements in a new tuple.
    Extracts all unique strings from aTuple
    and sets them as elements in a new tuple.

    Returns a tuple of:
        (minimum integer, maximum integer, number of unique strings)
    """
    nums = ()      # empty tuple for ints
    words = ()     # empty tuple for unique strings

    for t in aTuple:
        # concatenating with a singleton tuple
        nums = nums + (t[0],)
        # only add words we haven't added before
        if t[1] not in words:
            words = words + (t[1],)

    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)


if __name__ == "__main__":
    # demo：直接執行這個檔案時才會跑到這裡

    # 1) quotient_and_remainder 小例子
    (quot, rem) = quotient_and_remainder(5, 3)
    print(quot)
    print(rem)

    # 2) get_data 的兩個例子
    test = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    (a, b, c) = get_data(test)
    print("a:", a, "b:", b, "c:", c)

    tswift = (
        (2014, "Katy"),
        (2014, "Harry"),
        (2012, "Jake"),
        (2010, "Taylor"),
        (2008, "Joe"),
    )
    (min_year, max_year, num_people) = get_data(tswift)
    print(
        "From",
        min_year,
        "to",
        max_year,
        "Taylor Swift wrote songs about",
        num_people,
        "people!",
    )
