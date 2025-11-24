def primes_list(n):
    primes = [2]
    for j in range(3,n+1):
        is_div = False
        # go through each elem of primes list
        for p in primes:
            if j%p == 0:
                is_div = True
        if not is_div:
            primes.append(j)
    return primes

print(primes_list(2))               
print(primes_list(15))              


def test_primes_list():
    assert primes_list(2) == [2]
    assert primes_list(3) == [2, 3]
    assert primes_list(10) == [2, 3, 5, 7]
    assert primes_list(20) == [2, 3, 5, 7, 11, 13, 17, 19]
