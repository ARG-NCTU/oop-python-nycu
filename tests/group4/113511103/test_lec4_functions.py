# tests/group4/113511103/test_lec4_functions.py

def is_even_with_return(i):
    return i % 2 == 0

def get_divisors(n):
    return [x for x in range(1, n+1) if n % x == 0]

def find_common_factors(n1, n2):
    return [x for x in get_divisors(n1) if n2 % x == 0]

def get_multiplication_table(m, up_to=10):
    return [[i, i*m] for i in range(1, up_to+1)]

# ===================== 測試區 =====================

def test_is_even_with_return():
    assert is_even_with_return(2) == True
    assert is_even_with_return(3) == False
    assert is_even_with_return(0) == True
    assert is_even_with_return(101) == False

def test_get_divisors():
    assert get_divisors(1) == [1]
    assert get_divisors(6) == [1, 2, 3, 6]
    assert get_divisors(13) == [1, 13]

def test_find_common_factors():
    assert find_common_factors(12, 18) == [1, 2, 3, 6]
    assert find_common_factors(7, 13) == [1]
    assert find_common_factors(20, 30) == [1, 2, 5, 10]

def test_get_multiplication_table():
    assert get_multiplication_table(2, 3) == [[1, 2], [2, 4], [3, 6]]
    assert get_multiplication_table(5, 1) == [[1, 5]]
