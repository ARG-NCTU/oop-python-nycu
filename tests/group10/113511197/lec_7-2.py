def primes_list(n):
    primes = [2]
    for j in range(3,n+1):
        is_div = False
        # go through each elem of primes list
        for p in primes:
            if j%p == 0:
                is_div = True
        if not is_div:
            p