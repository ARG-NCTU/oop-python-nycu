import add_path
import mit_ocw_exercises.lec5_tuples_lists as lec5
import pytest


# =========================
# Tests for quotient_and_remainder
# =========================
def test_quotient_and_remainder_basic():
    # Basic cases
    assert lec5.quotient_and_remainder(20, 6) == (3, 2)
    assert lec5.quotient_and_remainder(20, 7) == (2, 6)
    assert lec5.quotient_and_remainder(20, 8) == (2, 4)
    assert lec5.quotient_and_remainder(20, 9) == (2, 2)
    assert lec5.quotient_and_remainder(20, 10) == (2, 0)
    assert lec5.quotient_and_remainder(20, 11) == (1, 9)

def test_quotient_and_remainder_edge_cases():
    # Division by 1
    assert lec5.quotient_and_remainder(15, 1) == (15, 0)
    # Dividend smaller than divisor
    assert lec5.quotient_and_remainder(3, 10) == (0, 3)
    # Dividend equal to divisor
    assert lec5.quotient_and_remainder(7, 7) == (1, 0)
    # Large numbers
    assert lec5.quotient_and_remainder(1000000, 999) == (1001, 1)

def test_quotient_and_remainder_zero_division():
    # Ensure ZeroDivisionError is raised
    with pytest.raises(ZeroDivisionError):
        lec5.quotient_and_remainder(20, 0)

def test_quotient_and_remainder_additional_cases():
    assert lec5.quotient_and_remainder(24, 6) == (4, 0)
    assert lec5.quotient_and_remainder(25, 7) == (3, 4)
    assert lec5.quotient_and_remainder(12, 8) == (1, 4)
    assert lec5.quotient_and_remainder(30, 9) == (3, 3)
    assert lec5.quotient_and_remainder(19, 10) == (1, 9)
    assert lec5.quotient_and_remainder(23, 13) == (1, 10)


# =========================
# Tests for sum_elem_method1
# =========================
def test_sum_elem_method1_basic():
    assert lec5.sum_elem_method1([1, 2, 3, 4]) == 10
    assert lec5.sum_elem_method1([-1, -2, -3, -4]) == -10
    assert lec5.sum_elem_method1([13, 34, 0, 88, 88, 0, 9]) == 232
    assert lec5.sum_elem_method1([5]) == 5
    assert lec5.sum_elem_method1([]) == 0

def test_sum_elem_method1_additional():
    # Mixed positive and negative
    assert lec5.sum_elem_method1([10, -5, 3, -2]) == 6
    # Large numbers
    assert lec5.sum_elem_method1([1000000, 2000000, -500000]) == 2500000


# =========================
# Tests for sum_elem_method2
# =========================
def test_sum_elem_method2_basic():
    assert lec5.sum_elem_method2([1, 2, 3, 4]) == 10
    assert lec5.sum_elem_method2([-1, -2, -3, -4]) == -10
    assert lec5.sum_elem_method2([13, 34, 0, 88, 88, 0, 9]) == 232
    assert lec5.sum_elem_method2([5]) == 5
    assert lec5.sum_elem_method2([]) == 0

def test_sum_elem_method2_additional():
    # Mixed positive and negative
    assert lec5.sum_elem_method2([10, -5, 3, -2]) == 6
    # Large numbers
    assert lec5.sum_elem_method2([1000000, 2000000, -500000]) == 2500000
