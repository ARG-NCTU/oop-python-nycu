def primes_list(n):
    """
    input: n an integer > 1
    returns: list of all the primes up to and including n
    """
    # initialize primes list with the first prime
    primes = [2]
    
    # go through each number from 3 up to and including n
    for j in range(3, n + 1):
        is_div = False
        # check against already found primes
        for p in primes:
            if j % p == 0:
                is_div = True
                break # optimization: stop checking if a divisor is found
        if not is_div:
            primes.append(j)
    return primes

# --- Pytest Functions ---
def test_primes_list():
    assert primes_list(2) == [2]
    assert primes_list(3) == [2, 3]
    assert primes_list(10) == [2, 3, 5, 7]
    assert primes_list(20) == [2, 3, 5, 7, 11, 13, 17, 19]