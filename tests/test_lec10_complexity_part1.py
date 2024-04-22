import add_path
import mit_ocw_exercises.lec10_complexity_part1 as lec10
import pytest
import time
import random

# create a fixture for the empty list
@pytest.fixture
def empty_list():
    return []

# create a fixture for the list of integers
@pytest.fixture
def sample_data():
    data = [1, 2, 3, 4, 5]
    return data

def test_linear_search():
    assert lec10.linear_search([1, 2, 3, 4, 5], 3) == True 
    assert lec10.linear_search([1, 2, 3, 4, 5], 6) == False
    assert lec10.linear_search([], 3) == False

def test_linear_search_int_list(sample_data):
    assert lec10.linear_search(sample_data, 3) == True 
    assert lec10.linear_search(sample_data, 6) == False





# test linear search with empty list
def test_linear_search_empty_list(empty_list):
    assert lec10.linear_search(empty_list, 3) == False

# create a list of integers, with parameter n for number of elements
def int_list(n):
    return list(range(n))

def test_linear_search_int_list():
    assert lec10.linear_search(int_list(10), 4) == True
    assert lec10.linear_search(int_list(10000), 4) == True
    #assert lec10.linear_search(int_list(100000000), 4) == True

# create a fixture factory that takes a parameter n for number of elements
@pytest.fixture
def int_list_factory():
    def _int_list(n):
        return list(range(n))
    return _int_list


def test_linear_search_int_list_factory(int_list_factory):
    assert lec10.linear_search(int_list_factory(10), 4) == True
    assert lec10.linear_search(int_list_factory(10000), 4) == True
    assert lec10.linear_search(int_list_factory(100000000), 4) == True

# create a fixture for num_elements with parameters 10, 10000, 1000000
@pytest.fixture(params=[10, 10000, 10000000])
def num_elements(request):
    return request.param

def test_linear_search_int_list_factory_enum(int_list_factory, num_elements):
    assert lec10.linear_search(int_list_factory(num_elements), 4) == True


@pytest.fixture
def sample1():
    data = [1,2,3,2,3]
    return data

# test intersection
def test_intersect(sample1):
    assert lec10.intersect(sample1, [2, 3, 4]) == [2, 3]
    assert lec10.intersect(sample1, [4, 5, 6]) == []
    assert lec10.intersect([], [4, 5, 6]) == []

# check elements in a list via python built-in function
def test_intersect_in(sample1):
    assert 2 in sample1
    assert 4 not in sample1

@pytest.fixture
def test_set():
    data = [1,2,3,4,5]
    return data

# test subset
def test_subset(test_set):
    assert lec10.isSubset([2,3,4],test_set) == True
    assert lec10.isSubset([2,7],test_set) == False

@pytest.fixture
def test_list():
    data = [1,3,4,5,9,18,27]
    return data

#test search
def test_search(test_list):
    assert lec10.search(test_list,27) == True
    assert lec10.search(test_list,6) == False



# test intersection
def test_intersect():
    assert lec10.intersect([1, 2, 3, 2, 3], [2, 3, 4]) == [2, 3]
    assert lec10.intersect([1, 2, 3], [4, 5, 6]) == []
    assert lec10.intersect([], [4, 5, 6]) == []

# check elements in a list via python built-in function
def test_intersect_in():
    assert 2 in [1, 2, 3]
    assert 4 not in [1, 2, 3]
    


# create a fixture factory that takes a parameter n for number of elements, and shuffles the list
@pytest.fixture
def int_list_factory_shuffled():
    def _int_list(n):
        data = list(range(n))
        random.shuffle(data)
        return data
    return _int_list

# create a fixture for num_elements with parameters 1000, 10000, 100000, 1000000, 10000000
@pytest.fixture(params=[1000, 10000, 100000, 1000000, 10000000])
def num_elements(request):
    return request.param

# run the test with the following command to show the time taken for each test
# pytest test_lec10_complexity_part1.py -s

# test linear search with both shuffled and sorted list and calculate time
def test_linear_search_int_list_factory_shuffled(int_list_factory_shuffled, num_elements):
    # Create list spends some time therefore we create it before the timer
    shuffled_list = int_list_factory_shuffled(num_elements)
    start = time.time()
    assert lec10.linear_search(shuffled_list, 4 * num_elements // 10) == True
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for linear search with {num_elements: 10d} elements shuffled list: {end-start:.2e}')

def test_linear_search_int_list_factory_sorted(int_list_factory, num_elements):
    # Create list spends some time therefore we create it before the timer
    sorted_list = int_list_factory(num_elements)
    start = time.time()
    assert lec10.linear_search(sorted_list, 4 * num_elements // 10) == True
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for linear search with {num_elements: 10d} elements sorted list: {end-start:.2e}')

# test built-in 'in' operator for shuffled list and calculate time
def test_in_operator_int_list_factory_shuffled(int_list_factory_shuffled, num_elements):
    # Create list spends some time therefore we create it before the timer
    shuffled_list = int_list_factory_shuffled(num_elements)
    start = time.time()
    assert 4 * num_elements // 10 in shuffled_list
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for \'in\' operator with {num_elements: 10d} elements shuffled list: {end-start:.2e}')

# test built-in 'in' operator for list and calculate time
def test_in_operator_int_list_factory(int_list_factory, num_elements):
    # Create list spends some time therefore we create it before the timer
    sorted_list = int_list_factory(num_elements)
    start = time.time()
    assert 4 * num_elements // 10 in sorted_list
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for \'in\' operator with {num_elements: 10d} elements sorted list: {end-start:.2e}')


# create a fixture factory that takes a parameter n for number of elements, and returns a set   
@pytest.fixture
def int_set_factory(int_list_factory):
    def _int_set(n):
        return set(int_list_factory(n))
    return _int_set

# set uses a hashtable as its underlying data structure, so it has the O(1) membership checking
# test built-in 'set' container and calculate time
def test_in_operator_int_set_factory(int_set_factory, num_elements):
    # Create set spends some time therefore we create it before the timer
    target_set = int_set_factory(num_elements)
    start = time.time()
    assert 4 * num_elements // 10 in target_set
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for \'set\' container with {num_elements: 10d} elements: {end-start:.2e}')


# create a fixture factory that takes a parameter n for number of elements, and returns a dict   
@pytest.fixture
def int_dict_factory(int_list_factory):
    def _int_dict(n):
        return {x: None for x in int_list_factory(n)}
    return _int_dict

# dict also uses a hashtable as its underlying data structure, so it has the O(1) membership checking
# test built-in 'dict' container and calculate time
def test_in_operator_int_dict_factory(int_dict_factory, num_elements):
    # Create dict spends some time therefore we create it before the timer
    target_dict = int_dict_factory(num_elements)
    start = time.time()
    assert 4 * num_elements // 10 in target_dict
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for \'dict\' container with {num_elements: 10d} elements: {end-start:.2e}')


@pytest.fixture
def empty_7_list():
    return []

# create a fixture for the list of integers
@pytest.fixture
def sample_7_data():
    data = [2, 4, 6, 8, 10]
    return data

def test_7_linear_search():
    assert lec10.linear_search([2, 4, 6, 8, 10], 6) == True 
    assert lec10.linear_search([2, 4, 6, 8, 10], 5) == False
    assert lec10.linear_search([], 3) == False

def test_7_linear_search_int_list(sample_7_data):
    assert lec10.linear_search(sample_7_data, 6) == True 
    assert lec10.linear_search(sample_7_data, 5) == False





# test linear search with empty list
def test_7_linear_search_empty_list(empty_7_list):
    assert lec10.linear_search(empty_7_list, 3) == False

# create a list of integers, with parameter n for number of elements
def int_7_list(n):
    return list(range(n))

def test_7_linear_search_int_list():
    assert lec10.linear_search(int_7_list(40), 4) == True
    assert lec10.linear_search(int_7_list(8000), 4) == True
    #assert lec10.linear_search(int_list(100000000), 4) == True

# create a fixture factory that takes a parameter n for number of elements
@pytest.fixture
def int_7_list_factory():
    def _int_list(n):
        return list(range(n))
    return _int_list


def test_7_linear_search_int_list_factory(int_list_factory):
    assert lec10.linear_search(int_list_factory(10), 8) == True
    assert lec10.linear_search(int_list_factory(10000), 8) == True
    assert lec10.linear_search(int_list_factory(100000000), 8) == True

# create a fixture for num_elements with parameters 10, 10000, 1000000
@pytest.fixture(params=[6, 6666, 66666666])
def num_7_elements(request):
    return request.param

def test_7_linear_search_int_list_factory_enum(int_list_factory, num_elements):
    assert lec10.linear_search(int_list_factory(num_elements), 4) == True


@pytest.fixture
def sample1():
    data = [1, 3, 5, 7, 9]
    return data

# test intersection
def test_7_intersect(sample1):
    assert lec10.intersect(sample1, [2, 4, 6]) == []
    assert lec10.intersect(sample1, [5, 6, 7]) == [5, 7]
    assert lec10.intersect([], [2, 6, 10]) == []

# check elements in a list via python built-in function
def test_7_intersect_in(sample1):
    assert 5 in sample1
    assert 4 not in sample1

@pytest.fixture
def test_7_set():
    data = [1, 4, 7, 11, 15]
    return data

# test subset
def test_7_subset(test_7_set):
    assert lec10.isSubset([1, 4, 7],test_7_set) == True
    assert lec10.isSubset([2,7],test_7_set) == False

@pytest.fixture
def test_7_list():
    data = [1,3,4,5,9,18,27]
    return data

#test search
def test_7_search(test_7_list):
    assert lec10.search(test_7_list,18) == True
    assert lec10.search(test_7_list,7) == False



# test intersection
def test_7_intersect():
    assert lec10.intersect([1, 2, 3, 2, 3], [2, 3, 4]) == [2, 3]
    assert lec10.intersect([1, 2, 3], [4, 5, 6]) == []
    assert lec10.intersect([], [4, 5, 6]) == []

# check elements in a list via python built-in function
def test_7_intersect_in():
    assert 2 in [1, 2, 3]
    assert 4 not in [1, 2, 3]
    


# create a fixture factory that takes a parameter n for number of elements, and shuffles the list
@pytest.fixture
def int_list_factory_shuffled():
    def _int_list(n):
        data = list(range(n))
        random.shuffle(data)
        return data
    return _int_list

# create a fixture for num_elements with parameters 1000, 10000, 100000, 1000000, 10000000
@pytest.fixture(params=[1000, 10000, 100000, 1000000, 10000000])
def num_elements(request):
    return request.param

# run the test with the following command to show the time taken for each test
# pytest test_lec10_complexity_part1.py -s

# test linear search with both shuffled and sorted list and calculate time
def test_7_linear_search_int_list_factory_shuffled(int_list_factory_shuffled, num_elements):
    # Create list spends some time therefore we create it before the timer
    shuffled_list = int_list_factory_shuffled(num_elements)
    start = time.time()
    assert lec10.linear_search(shuffled_list, 4 * num_elements // 10) == True
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for linear search with {num_elements: 10d} elements shuffled list: {end-start:.2e}')

def test_7_linear_search_int_list_factory_sorted(int_list_factory, num_elements):
    # Create list spends some time therefore we create it before the timer
    sorted_list = int_list_factory(num_elements)
    start = time.time()
    assert lec10.linear_search(sorted_list, 4 * num_elements // 10) == True
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for linear search with {num_elements: 10d} elements sorted list: {end-start:.2e}')

# test built-in 'in' operator for shuffled list and calculate time
def test_7_in_operator_int_list_factory_shuffled(int_list_factory_shuffled, num_elements):
    # Create list spends some time therefore we create it before the timer
    shuffled_list = int_list_factory_shuffled(num_elements)
    start = time.time()
    assert 4 * num_elements // 10 in shuffled_list
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for \'in\' operator with {num_elements: 10d} elements shuffled list: {end-start:.2e}')

# test built-in 'in' operator for list and calculate time
def test_7_in_operator_int_list_factory(int_list_factory, num_elements):
    # Create list spends some time therefore we create it before the timer
    sorted_list = int_list_factory(num_elements)
    start = time.time()
    assert 4 * num_elements // 10 in sorted_list
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for \'in\' operator with {num_elements: 10d} elements sorted list: {end-start:.2e}')


# create a fixture factory that takes a parameter n for number of elements, and returns a set   
@pytest.fixture
def int_7_set_factory(int_list_factory):
    def _int_set(n):
        return set(int_list_factory(n))
    return _int_set

# set uses a hashtable as its underlying data structure, so it has the O(1) membership checking
# test built-in 'set' container and calculate time
def test_7_in_operator_int_set_factory(int_set_factory, num_elements):
    # Create set spends some time therefore we create it before the timer
    target_set = int_set_factory(num_elements)
    start = time.time()
    assert 4 * num_elements // 10 in target_set
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for \'set\' container with {num_elements: 10d} elements: {end-start:.2e}')


# create a fixture factory that takes a parameter n for number of elements, and returns a dict   
@pytest.fixture
def int_dict_factory(int_list_factory):
    def _int_dict(n):
        return {x: None for x in int_list_factory(n)}
    return _int_dict

# dict also uses a hashtable as its underlying data structure, so it has the O(1) membership checking
# test built-in 'dict' container and calculate time
def test_7_in_operator_int_dict_factory(int_dict_factory, num_elements):
    # Create dict spends some time therefore we create it before the timer
    target_dict = int_dict_factory(num_elements)
    start = time.time()
    assert 4 * num_elements // 10 in target_dict
    end = time.time()
    # print the result using exponential notation
    print(f'Time taken for \'dict\' container with {num_elements: 10d} elements: {end-start:.2e}')



def test_2_linear_search():
    assert lec10.linear_search([3, 1, 4, 1, 5, 9, 2, 6], 3) == True 
    assert lec10.linear_search([3, 1, 4, 1, 5, 9, 2, 6], 7) == False
    assert lec10.linear_search([], 3) == False

def test_2_search():
    assert lec10.search([1,3,4,5,9,18,27], 27) == True
    assert lec10.search([1,3,4,5,9,18,27], 6) == False

def test_2_isSubset():
    assert lec10.isSubset([2,3,4], [1,2,3,4,5]) == True
    assert lec10.isSubset([2,3,4], [1,5]) == False

def test_2_intersect():
    assert lec10.intersect([1, 2, 3, 2, 3], [2, 3, 4]) == [2, 3]
    assert lec10.intersect([1, 2, 3], [4, 5, 6]) == []
    assert lec10.intersect([], [4, 5, 6]) == []
    
