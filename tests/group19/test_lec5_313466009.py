def is_even(n):
    return n % 2 == 0


def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def find_common_factors(a, b):
    return [x for x in get_divisors(a) if b % x == 0]


def get_multiplication_table(m, up_to=10):
    return [[i, i * m] for i in range(1, up_to + 1)]


def make_adder(a):
    def adder(b):
        return a + b
    return adder


def apply_func(f, value):
    return f(value)

# test start here
def test_is_even():
    assert is_even(2)
    assert not is_even(3)
    assert is_even(0)

def test_get_divisors():
    assert get_divisors(1) == [1]
    assert get_divisors(6) == [1, 2, 3, 6]

def test_find_common_factors():
    assert find_common_factors(12, 18) == [1, 2, 3, 6]
    assert find_common_factors(7, 13) == [1]

def test_get_multiplication_table():
    assert get_multiplication_table(2, 3) == [[1, 2], [2, 4], [3, 6]]
    assert get_multiplication_table(5, 1) == [[1, 5]]

def test_make_adder():
    add5 = make_adder(5)
    assert add5(2) == 7
    assert make_adder(10)(3) == 13

def test_apply_func():
    assert apply_func(lambda x: x * 2, 4) == 8
    assert apply_func(is_even, 4)

def test_all():
    test_is_even()
    test_get_divisors()
    test_find_common_factors()
    test_get_multiplication_table()
    test_make_adder()
    test_apply_func()