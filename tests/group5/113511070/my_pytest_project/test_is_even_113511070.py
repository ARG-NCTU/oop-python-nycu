import pytest
from is_even_113511070 import is_even

@pytest.mark.parametrize("input_val, expected", [
    (0, True),
    (1, False),
    (2, True),
    (15, False),
    (100, True),
    (-1, False),
    (-2, True),
    (-101, False),
    (-100, True),
    (10**6, True),
    (10**6 + 1, False),
    (-10**6, True),
    (-10**6 + 1, False),
])
def test_is_even(input_val, expected):
    assert is_even(input_val) == expected
