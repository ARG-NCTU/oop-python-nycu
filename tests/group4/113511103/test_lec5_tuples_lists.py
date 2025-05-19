# tests/group4/113511103/test_lec5_tuples_lists.py

# 從 lec5 改寫來的兩個函式，去除 print，改為純 function

def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

# ========== 測試區段 ==========

def test_quotient_and_remainder():
    assert quotient_and_remainder(5, 3) == (1, 2)
    assert quotient_and_remainder(10, 2) == (5, 0)
    assert quotient_and_remainder(0, 1) == (0, 0)
    assert quotient_and_remainder(13, 5) == (2, 3)

def test_get_data_basic():
    data = ((1,"a"), (2,"b"), (1,"a"), (7,"b"))
    result = get_data(data)
    assert result == (1, 7, 2)

def test_get_data_taylor():
    data = ((2014,"Katy"), (2014,"Harry"), (2012,"Jake"),
            (2010,"Taylor"), (2008,"Joe"))
    assert get_data(data) == (2008, 2014, 5)

def test_get_data_edge():
    data = ((99,"z"),)
    assert get_data(data) == (99, 99, 1)

    data = ((-5,"x"), (5,"x"), (-5,"x"))
    assert get_data(data) == (-5, 5, 1)
