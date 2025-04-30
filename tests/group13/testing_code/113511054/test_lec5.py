## EXAMPLE: returning a tuple
def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)

def test_quotient_and_remainder():
    (quot, rem) = quotient_and_remainder(5,3)
    assert quot == 1
    assert rem == 2
    (quot, rem) = quotient_and_remainder(20,7)
    assert quot == 2
    assert rem == 6

## EXAMPLE: iterating over tuples
def get_data(aTuple):
    nums = ()    # empty tuple
    words = ()
    for t in aTuple:
        # concatenating with a singleton tuple
        nums = nums + (t[0],)
        # only add words haven't added before
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

def test_get_data():
    test = ((1,"a"),(2, "b"),
            (1,"c"),(7,"b"))
    (a, b, c) = get_data(test)
    assert a == 1
    assert b == 7
    assert c == 3
    ##########################
    test = ((2014,"Katy"),
            (2014, "Harry"),
            (2012,"Jake"),
            (2010,"Taylor"),
            (2008,"Joe"))
    (a, b, c) = get_data(test)
    assert a == 2008
    assert b == 2014
    assert c == 5

## EXAMPLE: sum of elements in a list
def sum_elem_method1(L):
  total = 0
