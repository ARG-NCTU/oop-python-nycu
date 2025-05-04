import pytest

# ========== 功能函式 ==========
def sum_elem_method1(L):
    total = 0
    for i in range(len(L)):
        total += L[i]
    return total

def sum_elem_method2(L):
    total = 0
    for i in L:
        total += i
    return total

def get_data(aTuple):
    """
    aTuple: tuple of tuples (int, string)
    Returns: (min integer, max integer, number of unique strings)
    """
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

# ========== 單元測試 ==========
@pytest.mark.parametrize("L, expected", [
    ([1, 2, 3, 4], 10),
    ([0, 0, 0], 0),
    ([-1, -2, -3], -6)
])
def test_sum_methods(L, expected):
    assert sum_elem_method1(L) == expected
    assert sum_elem_method2(L) == expected

@pytest.mark.parametrize("data, expected", [
    (((1, "a"), (2, "b"), (1, "a"), (7, "b")), (1, 7, 2)),
    (((2014, "phono wu"), (2014, "gibbs wu"), (2012, "porco wu")), (2012, 2014, 3)),
])
def test_get_data_function(data, expected):
    assert get_data(data) == expected

# ========== 主程式區 ==========
if __name__ == "__main__":
    print(sum_elem_method1([1, 2, 3, 4]))
    print(sum_elem_method2([1, 2, 3, 4]))

    test = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    (a, b, c) = get_data(test)
    print("最多的:", a, "最少的:", b, "總共幾個字母:", c)

    tswift = (
        (2014, "phono wu"),
        (2014, "gibbs wu"),
        (2012, "porco wu"),
        (2010, "gibbs wu"),
        (2008, "lagrange wu"),
        (2000, "alan wu")
    )
    (min_year, max_year, num_people) = get_data(tswift)
    print("From", min_year, "to", max_year,
          "Taylor Swift wrote songs about", num_people, "people!")
