import add_path  # if your repo requires this to set up sys.path
import mit_ocw_exercises.lec5_tuples_lists as lec5
import pytest

# --- Test for quotient_and_remainder ---
@pytest.mark.parametrize("a, b, expected", [
    (10, 3, (3, 1)),
    (8, 4, (2, 0)),
    (0, 5, (0, 0)),
    (17, 5, (3, 2)),
    (22, 7, (3, 1)),
])
def test_quotient_and_remainder_basic(a, b, expected):
    assert lec5.quotient_and_remainder(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (-9, 2, (-5, 1)),
    (9, -2, (-5, -1)),
])
def test_quotient_and_remainder_negative(a, b, expected):
    assert lec5.quotient_and_remainder(a, b) == expected

def test_quotient_and_remainder_zero_division():
    with pytest.raises(ZeroDivisionError):
        lec5.quotient_and_remainder(5, 0)

# --- Test for get_data ---
@pytest.mark.parametrize("data, expected", [
    (((5, "apple"), (3, "banana"), (9, "apple"), (7, "cherry")), (3, 9, 3)),
    (((100, "x"), (200, "y"), (300, "x"), (50, "z")), (50, 300, 3)),
    (((1, "a"), (2, "b"), (1, "a"), (7, "b")), (1, 7, 2)),
    (((10, "mango"),), (10, 10, 1)),
    (((1, "x"), (2, "x"), (3, "x")), (1, 3, 1)),
])
def test_get_data(data, expected):
    assert lec5.get_data(data) == expected
