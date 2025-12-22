import add_path
import mit_ocw_exercises.lec10_complexity_part1 as lec10
import pytest
import time
import random

# =========================
# Fixtures
# =========================
@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def sample_list_dup():
    return [1, 2, 3, 2, 3]

@pytest.fixture
def int_list_factory():
    def _int_list(n):
        return list(range(n))
    return _int_list

@pytest.fixture
def int_list_factory_shuffled():
    def _int_list(n):
        data = list(range(n))
        random.shuffle(data)
        return data
    return _int_list

@pytest.fixture(params=[1000, 10000, 100000])
def num_elements(request):
    return request.param

# =========================
# Linear search tests
# =========================
def test_linear_search_basic(sample_list):
    assert lec10.linear_search(sample_list, 3) is True
    assert lec10.linear_search(sample_list, 6) is False
    assert lec10.linear_search([], 3) is False

@pytest.mark.slow
def test_linear_search_large_sorted(int_list_factory, num_elements):
    lst = int_list_factory(num_elements)
    start = time.time()
    assert lec10.linear_search(lst, 4 * num_elements // 10) is True
    end = time.time()
    print(f"Time for linear_search sorted {num_elements}: {end-start:.2e} s")

@pytest.mark.slow
def test_linear_search_large_shuffled(int_list_factory_shuffled, num_elements):
    lst = int_list_factory_shuffled(num_elements)
    start = time.time()
    assert lec10.linear_search(lst, 4 * num_elements // 10) is True
    end = time.time()
    print(f"Time for linear_search shuffled {num_elements}: {end-start:.2e} s")

# =========================
# Intersection tests
# =========================
def test_intersect_basic(sample_list_dup):
    assert lec10.intersect(sample_list_dup, [2, 3, 4]) == [2, 3]
    assert lec10.intersect(sample_list_dup, [4, 5, 6]) == []
    assert lec10.intersect([], [1, 2, 3]) == []

# =========================
# Subset tests
# =========================
def test_isSubset_basic():
    assert lec10.isSubset([2, 3, 4], [1, 2, 3, 4, 5]) is True
    assert lec10.isSubset([2, 7], [1, 2, 3, 4, 5]) is False

# =========================
# Search (assumes sorted) tests
# =========================
def test_search_basic():
    lst = [1, 3, 4, 5, 9, 18, 27]
    assert lec10.search(lst, 27) is True
    assert lec10.search(lst, 6) is False

# =========================
# Membership test with built-in containers
# =========================
@pytest.mark.slow
def test_membership_containers(int_list_factory, int_list_factory_shuffled, num_elements):
    sorted_list = int_list_factory(num_elements)
    shuffled_list = int_list_factory_shuffled(num_elements)
    s = set(sorted_list)
    d = {x: None for x in sorted_list}

    start = time.time()
    assert 4 * num_elements // 10 in sorted_list
    end = time.time()
    print(f"In sorted list {num_elements}: {end-start:.2e} s")

    start = time.time()
    assert 4 * num_elements // 10 in shuffled_list
    end = time.time()
    print(f"In shuffled list {num_elements}: {end-start:.2e} s")

    start = time.time()
    assert 4 * num_elements // 10 in s
    end = time.time()
    print(f"In set {num_elements}: {end-start:.2e} s")

    start = time.time()
    assert 4 * num_elements // 10 in d
    end = time.time()
    print(f"In dict {num_elements}: {end-start:.2e} s")
