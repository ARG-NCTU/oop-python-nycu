def avg(grades):
    return sum(grades) / len(grades)

def get_stats(class_grades):
    result = []
    for name, grades in class_grades:
        result.append([name, grades, avg(grades)])
    return result

def primes_list(n):
    primes = []
    for num in range(2, n + 1):
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
    return primes

def rev_list(L):
    for i in range(len(L)//2):
        L[i], L[-i-1] = L[-i-1], L[i]

# Run Pytest

def test_avg():
    assert avg([1, 2, 3]) == 2.0
    assert avg([2, 4, 6, 8]) == 5.0

def test_get_stats():
    result = get_stats([['Alice', [90, 80, 85]], ['Bob', [70, 75, 80]]])
    expected = [['Alice', [90, 80, 85], 85.0], ['Bob', [70, 75, 80], 75.0]]
    assert result == expected

def test_primes_list():
    assert primes_list(1) == []
    assert primes_list(2) == [2]
    assert primes_list(5) == [2, 3, 5]
    assert primes_list(10) == [2, 3, 5, 7]

def test_rev_list():
    L = [1, 2, 3, 4]
    rev_list(L)
    assert L == [4, 3, 2, 1]