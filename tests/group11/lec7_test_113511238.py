import pytest

@pytest.mark.parametrize("a, b, expected", [
    (10, 3, (3, 1)),
    (8, 4, (2, 0)),
    (0, 5, (0, 0)),
    (17, 5, (3, 2)),
    (22, 7, (3, 1))
])
def test_quotient_and_remainder_basic(a, b, expected):
    assert lec5.quotient_and_remainder(a, b) == expected
