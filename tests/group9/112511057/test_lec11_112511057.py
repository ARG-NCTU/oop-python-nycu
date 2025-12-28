import mit_ocw_exercises.lec11_complexity_part2 as lec11


def test_bisect_search_and_subsets():
    L = list(range(20))
    assert lec11.bisect_search1(L, 5) is True
    assert lec11.bisect_search1(L, 100) is False

    assert lec11.bisect_search2(L, 10) is True
    assert lec11.bisect_search2(L, -1) is False

    subs = lec11.genSubsets([1,2,3])
    assert len(subs) == 8
    assert [] in subs
    assert [1,2,3] in subs
