from lec11_complexity_part2 import binary_search, merge_sorted, union, difference
import pytest
import add_path
import random
def test_binary_search_found():
    L = list(range(100))
    e = 42
    assert binary_search(L, e) == True

def test_binary_search_not_found():
    L = list(range(100))
    e = 150
    assert binary_search(L, e) == False

def test_merge_sorted():
    L1 = [1, 3, 5]
    L2 = [2, 4, 6]
    assert merge_sorted(L1, L2) == [1, 2, 3, 4, 5, 6]

def test_union():
    L1 = [1, 2, 3]
    L2 = [3, 4, 5]
    assert union(L1, L2) == [1, 2, 3, 4, 5]

def test_difference():
    L1 = [1, 2, 3, 4]
    L2 = [3, 4, 5]
    assert difference(L1, L2) == [1, 2]

@pytest.mark.parametrize("n", [10, 50, 100])
def test_binary_search_random_sizes(n):
    random.seed(123)
    L = sorted(random.sample(range(0, 1000), n))
    e = random.choice(L)
    assert binary_search(L, e) == True

def test_difference_random_sizes():
    random.seed(123)
    L1 = sorted(random.sample(range(0, 1000), 50))
    L2 = sorted(random.sample(range(0, 1000), 30))
    result = difference(L1, L2)
    for item in result:
        assert item in L1 and item not in L2
    expected = [item for item in L1 if item not in L2]
    assert sorted(result) == sorted(expected)