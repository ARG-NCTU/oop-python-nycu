from lec7 import rev_list, primes_list, get_ratios, get_stats

test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]], 
              [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
              [['captain', 'america'], [80.0, 70.0, 96.0]]]

def test_rev_list():
    L1 = [1, 'c', 3, 'a']
    rev_list(L1)
    assert L1 == ['a', 3, 'c', 1]
    l2 = [1, 2, 3, 4]
    rev_list(l2)
    assert l2 == [4, 3, 2, 1]

def test_primes_list():
    assert primes_list(2) == [2]
    assert primes_list(3) == [2, 3]
    assert primes_list(51) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def test_get_ratios():
    assert get_ratios([1, 2, 3], [2, 3, 4]) == [0.5, 2/3, 0.75]

def test_get_stats():
    assert get_stats(test_grades) == [[['peter', 'parker'], [80.0, 70.0, 85.0], 235/3],
                                      [['bruce', 'wayne'], [100.0, 80.0, 74.0], 254/3],
                                      [['captain', 'america'], [80.0, 70.0, 96.0], 246/3]]