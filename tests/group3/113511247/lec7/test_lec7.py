import pytest
import math
from lec7_debug_except import rev_list, primes_list, get_ratios, get_stats

def test_rev_list():
    L = [1, 2, 3, 4]
    rev_list(L)
    assert L == [4, 3, 2, 1]

def test_primes_list():
    assert primes_list(2) == [2]
    assert primes_list(15) == [2, 3, 5, 7, 11, 13]

def test_get_ratios_success(capsys):
    ratios = get_ratios([1, 4], [2, 4])
    output = capsys.readouterr().out.splitlines()
    assert output == ["success", "executed no matter what!", "success", "executed no matter what!"]
    assert ratios == [0.5, 1.0]

def test_get_ratios_divzero(capsys):
    ratios = get_ratios([1, 4], [0, 4])
    output = capsys.readouterr().out.splitlines()
    assert output == ["executed no matter what!", "success", "executed no matter what!"]
    assert math.isnan(ratios[0])
    assert ratios[1] == 1.0

def test_get_ratios_bad_arg():
    with pytest.raises(ValueError, match="get_ratios called with bad arg"):
        get_ratios(["a"], [1])

def test_get_stats_valid():
    valid_list = [
        [['peter', 'parker'], [80.0, 70.0, 85.0]],
        [['bruce', 'wayne'], [100.0, 80.0, 74.0]]
    ]
    stats = get_stats(valid_list)
    avg1 = sum(valid_list[0][1]) / len(valid_list[0][1])
    avg2 = sum(valid_list[1][1]) / len(valid_list[1][1])
    assert len(stats) == 2
    assert stats[0][0] == ['peter', 'parker']
    assert stats[0][1] == [80.0, 70.0, 85.0]
    assert abs(stats[0][2] - avg1) < 1e-5
    assert stats[1][0] == ['bruce', 'wayne']
    assert stats[1][1] == [100.0, 80.0, 74.0]
    assert abs(stats[1][2] - avg2) < 1e-5

def test_get_stats_empty():
    invalid_list = [
        [['deadpool'], []]
    ]
    with pytest.raises(AssertionError):
        get_stats(invalid_list)
