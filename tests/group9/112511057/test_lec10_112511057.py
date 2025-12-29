import mit_ocw_exercises.lec10_complexity_part1 as lec10


def test_searches_and_subset_and_intersect():
    L = [1,3,5,7,9]
    assert lec10.linear_search(L, 5) is True
    assert lec10.linear_search(L, 2) is False

    assert lec10.search(L, 3) is True
    assert lec10.search(L, 8) is False

    assert lec10.isSubset([1,3], [1,2,3,4]) is True
    assert lec10.isSubset([1,6], [1,2,3,4]) is False

    assert sorted(lec10.intersect([1,2,3], [2,3,4])) == [2,3]
