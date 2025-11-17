import pytest

from lec5_tuples_lists_113511088 import (
    quotient_and_remainder,
    get_data,
)

# ----------------------
# tests for quotient_and_remainder
# ----------------------


def test_quotient_and_remainder_basic():
    # 5 // 3 = 1, 5 % 3 = 2
    q, r = quotient_and_remainder(5, 3)
    assert q == 1
    assert r == 2


def test_quotient_and_remainder_divisible():
    # 10 // 5 = 2, 10 % 5 = 0
    q, r = quotient_and_remainder(10, 5)
    assert q == 2
    assert r == 0


def test_quotient_and_remainder_type_and_length():
    result = quotient_and_remainder(7, 4)
    # 回傳型態要是 tuple，且長度為 2
    assert isinstance(result, tuple)
    assert len(result) == 2


# ----------------------
# tests for get_data
# ----------------------


def test_get_data_simple_example():
    test = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    a, b, c = get_data(test)

    # ints: 1,2,1,7 → min=1, max=7
    assert a == 1
    assert b == 7
    # unique strings: "a","b" → 2
    assert c == 2


def test_get_data_tswift_example():
    tswift = (
        (2014, "Katy"),
        (2014, "Harry"),
        (2012, "Jake"),
        (2010, "Taylor"),
        (2008, "Joe"),
    )
    min_year, max_year, num_people = get_data(tswift)

    assert min_year == 2008
    assert max_year == 2014
    # unique names: Katy, Harry, Jake, Taylor, Joe → 5
    assert num_people == 5


def test_get_data_works_with_single_element():
    data = ((42, "onlyone"),)
    mn, mx, count = get_data(data)

    assert mn == 42
    assert mx == 42
    assert count == 1
