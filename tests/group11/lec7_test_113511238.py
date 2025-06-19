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
