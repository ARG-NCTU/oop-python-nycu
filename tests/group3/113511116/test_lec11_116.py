import add_path
import mit_ocw_exercises.lec11_complexity_part2 as lec11
import pytest

def test_bisect_search1 (capsys):
    testList = list(range(100))
    lec11.bisect_search1(testList, 76)
    captured = capsys.readouterr()  
    assert 'low: 0; high: 99' in captured.out


def test_bisect_search2 (capsys):
    testList = list(range(100))
    lec11.bisect_search2(testList, 76)
    captured = capsys.readouterr()  
    assert 'low: 0; high: 99' in captured.out

def test_genSubsets():
    testSet = [1,2,3]
    result = lec11.genSubsets(testSet)
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert sorted(result) == sorted(expected)