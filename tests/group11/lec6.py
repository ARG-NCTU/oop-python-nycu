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

# --- Test for fib_mem ---
@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (5, 8),
    (6, 13),
])
def test_fib_mem(n, expected):
    assert lec6.fib_mem(n) == expected

def test_fib_mem_relation():
    assert lec6.fib_mem(5) == lec6.fib_mem(4) + lec6.fib_mem(3)


# --- Test for fib_efficient ---
def test_fib_efficient():
    d = {1: 1, 2: 2}
    assert lec6.fib_efficient(3, d.copy()) == 3
    assert lec6.fib_efficient(6, d.copy()) == 21
    assert lec6.fib_efficient(1, d.copy()) == 1
    assert lec6.fib_efficient(2, d.copy()) == 2

