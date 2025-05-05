import pytest
from src.mit_ocw_exercises.lec5_tuples_lists import (
    quotient_and_remainder,
    get_data,
    sum_elem_method1,
    sum_elem_method2,
    remove_dups,
    remove_dups_new,
)

def test_quotient_and_remainder():
    assert quotient_and_remainder(5, 3) == (1, 2)
    assert quotient_and_remainder(10, 2) == (5, 0)
    assert quotient_and_remainder(0, 5) == (0, 0)

