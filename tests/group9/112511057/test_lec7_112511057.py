import math
import pytest
import mit_ocw_exercises.lec7_debug_except as lec7


def test_rev_list_basic():
    L = [1, 2, 3, 4]
    lec7.rev_list(L)
    assert L == [4, 3, 2, 1]


def test_rev_list_edge_cases():
    L = []
    lec7.rev_list(L)
    assert L == []

    L2 = [1]
    lec7.rev_list(L2)
    assert L2 == [1]


def test_primes_list_known():
    assert lec7.primes_list(2) == [2]
    assert lec7.primes_list(15) == [2, 3, 5, 7, 11, 13]


def test_get_ratios_normal_and_zero():
    res = lec7.get_ratios([1, 4], [2, 0])
    assert math.isclose(res[0], 0.5)
    assert math.isnan(res[1])


def test_get_ratios_bad_args():
    with pytest.raises(ValueError):
        lec7.get_ratios([1, 2, 3], [1, 2])


def test_avg_nonempty_and_empty():
    assert lec7.avg([10.0, 20.0]) == pytest.approx(15.0)
    with pytest.raises(AssertionError):
        lec7.avg([])


def test_get_stats_basic():
    class_list = [[['alice'], [80.0, 90.0]], [['bob'], [100.0]]]
    stats = lec7.get_stats(class_list)
    assert len(stats) == 2
    assert stats[0][0] == ['alice']
    assert stats[0][1] == [80.0, 90.0]
    assert stats[0][2] == pytest.approx(85.0)
