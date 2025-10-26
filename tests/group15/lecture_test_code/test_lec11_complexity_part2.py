import tests.group15.lecture_test_code.add_path
import pytest
import mit_ocw_exercises.lec11_complexity_part2 as l11

@pytest.mark.parametrize(
    "L,e,expect",
    [
        ([], 0, False),
        ([1], 1, True),
        ([1], 0, False),
        (list(range(0, 10)), 0, True),
        (list(range(0, 10)), 9, True),
        (list(range(0, 10)), 5, True),
        (list(range(0, 10)), -1, False),
        (list(range(0, 10)), 10, False),
        ([1, 1, 2, 2, 3, 3], 2, True),
    ],
)
def test_bisect_search1_basic(L, e, expect, capsys):
    assert l11.bisect_search1(L, e) is expect
    _ = capsys.readouterr().out  # swallow prints

@pytest.mark.parametrize(
    "L,e,expect",
    [
        ([], 0, False),
        ([1], 1, True),
        ([1], 2, False),
        (list(range(0, 10)), 0, True),
        (list(range(0, 10)), 9, True),
        (list(range(0, 10)), 4, True),
        (list(range(0, 10)), -3, False),
        (list(range(0, 10)), 11, False),
        ([1, 1, 2, 2, 3, 3], 3, True),
    ],
)
def test_bisect_search2_basic(L, e, expect, capsys):
    assert l11.bisect_search2(L, e) is expect
    _ = capsys.readouterr().out  # swallow prints

def to_set_of_tuples(list_of_lists):
    return {tuple(x) for x in list_of_lists}

@pytest.mark.parametrize(
    "L,expected_set",
    [
        ([], {()}),
        ([1], {(), (1,)}),
        ([1, 2], {(), (1,), (2,), (1, 2)}),
        ([1, 2, 3], {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}),
    ],
)
def test_genSubsets_contents_and_size(L, expected_set):
    res = l11.genSubsets(L)
    got = to_set_of_tuples(res)
    assert got == expected_set
    assert len(res) == 2 ** len(L)

def test_genSubsets_order_example_small():
    res = l11.genSubsets([1, 2])
    assert res == [[], [1], [2], [1, 2]]

def test_bisect_search_edges_large():
    L = list(range(0, 100))
    assert l11.bisect_search1(L, 0) is True
    assert l11.bisect_search1(L, 99) is True
    assert l11.bisect_search2(L, 0) is True
    assert l11.bisect_search2(L, 99) is True
