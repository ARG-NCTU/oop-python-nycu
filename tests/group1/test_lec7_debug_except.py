import math
from add_path import add_path
add_path()
from lec7_debug_except import rev_list, primes_list, get_ratios, avg, get_stats

def test_rev_list():
    L = [1, 2, 3, 4]
    assert rev_list(L) == [4, 3, 2, 1]

    L2 = [1]
    assert rev_list(L2) == [1]

    L3 = []
    assert rev_list(L3) == []


def test_primes_list():
    assert primes_list(1) == []
    assert primes_list(2) == [2]
    assert primes_list(3) == [2, 3]
    assert primes_list(10) == [2, 3, 5, 7]


def test_get_ratios():
    L1 = [1, 4, 6]
    L2 = [1, 2, 0]

    r = get_ratios(L1, L2)
    assert r[0] == 1.0
    assert r[1] == 2.0
    assert math.isnan(r[2])


def test_avg():
    assert avg([10, 20, 30]) == 20
    try:
        avg([])
        assert False  # Should not reach
    except AssertionError:
        assert True


def test_get_stats():
    cls = [
        [['peter','parker'], [80, 70, 90]],
        [['deadpool'], []],
    ]
    s = get_stats(cls)

    assert s[0][2] == 80   # avg
    assert s[1][2] == 0.0  # no grades → handled


def test_primes_list_small_inputs():
    """Sanity checks for small inputs to primes_list."""
    assert primes_list(0) == []
    assert primes_list(-5) == []
