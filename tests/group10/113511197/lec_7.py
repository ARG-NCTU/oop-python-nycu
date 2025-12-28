import pytest
import math
import lec7_debug_except as lec
def test_rev_list():
    L1 = [1, 2, 3, 4]
    lec.rev_list(L1)
    assert L1 == [4, 3, 2, 1]
    L2 = [1, 2, 3, 4, 5]
    lec.rev_list(L2)
    assert L2 == [5, 4, 3, 2, 1]
    L3 = []
    lec.rev_list(L3)
    assert L3 == []
    L4 = [10]
    lec.rev_list(L4)
    assert L4 == [10]

def test_primes_list():
    # 基本情況
    assert lec.primes_list(15) == [2, 3, 5, 7, 11, 13]
    
    # 邊界情況
    assert lec.primes_list(2) == [2]
    assert lec.primes_list(1) == []
    assert lec.primes_list(0) == []
    assert lec.primes_list(-10) == []

def test_get_ratios():
    ratios = lec.get_ratios([1, 4, 6], [2, 0, 3])
    assert ratios[0] == 0.5
    assert math.isnan(ratios[1])
    assert ratios[2] == 2.0
    with pytest.raises(ValueError, match='different lengths'):
        lec.get_ratios([1, 2], [1])

    with pytest.raises(ValueError, match='bad argument type'):
        lec.get_ratios([1, 'a'], [2, 3])

def test_avg():
    assert lec.avg([80, 90, 100]) == 90.0
    assert lec.avg([]) == 0.0
    assert lec.avg([10.5, 20.5]) == 15.5

def test_get_stats():
    test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]],
                   [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
                   [['deadpool'], []]]

    stats = lec.get_stats(test_grades)
    assert stats[0][0] == ['peter', 'parker']
    assert stats[0][2] == pytest.approx(78.33333333333333)
    assert stats[1][2] == pytest.approx(84.66666666666667)
    

