import pytest
from src.mit_ocw_exercises import lec6_recursion_dictionaries as lec6
import add_path  # if your repo requires this to set up sys.path

# --- Test for fib ---
@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (5, 8),
    (6, 13),
])
def test_fib(n, expected):
    assert lec6.fib(n) == expected
