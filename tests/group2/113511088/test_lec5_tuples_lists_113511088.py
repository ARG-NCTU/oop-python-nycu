import pytest

from lec5_tuples_lists_113511088 import quotient_and_remainder


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
