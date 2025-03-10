
import lec7


# please write a test for fib function
def test_rev_list():
    assert lec7.rev_list([1,2,3,4]) == [4,3,2,1]
    assert lec7.rev_list([1,2,3]) == [3,2,1]
    assert lec7.rev_list([1,2]) == [2,1]
    assert lec7.rev_list([1]) == [1]
    assert lec7.rev_list([]) == []
    assert lec7.rev_list([-1,-2,-3]) == [-3,-2,-1]
    assert lec7.rev_list([-1,-2,0]) == [-2,-1,0]

def test_primes_list():
    assert lec7.primes_list(2) == [2]
    assert lec7.primes_list(3) == [2,3]
    assert lec7.primes_list(4) == [2,3]
    assert lec7.primes_list(5) == [2,3,5]
    assert lec7.primes_list(6) == [2,3,5]


def test_get_ratios():
    assert lec7.get_ratios([1,2,3],[1,2,3]) == [1.0, 1.0, 1.0]
    assert lec7.get_ratios([1,2,3],[1,2,4]) == [1.0, 1.0, 0.75]
    assert lec7.get_ratios([1,2,3],[1,2,0]) == [1.0, 1.0, float('nan')]
    assert lec7.get_ratios([1,2,3],[1,0,3]) == [1.0, float('nan'), 1.0]


def test_get_stats(capfd):
    test_grades = [
        [['peter', 'parker'], [80.0, 70.0, 85.0]], 
        [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
        [['captain', 'america'], [80.0, 70.0, 96.0]],
        [['deadpool'], []]
    ]
    expected_output = [
        [['peter', 'parker'], [80.0, 70.0, 85.0], 78.33333333333333],
        [['bruce', 'wayne'], [100.0, 80.0, 74.0], 84.66666666666667],
        [['captain', 'america'], [80.0, 70.0, 96.0], 82.0],
        [['deadpool'], [], 0.0]
    ]
    result = lec7.get_stats(test_grades)
    out, err = capfd.readouterr()
    assert result == expected_output
    assert 'warning: no grades data' in out