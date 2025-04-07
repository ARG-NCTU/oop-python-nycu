def test_primes_list():
    assert primes_list(2) == [2], "Test case 1 failed"
    assert primes_list(10) == [2, 3, 5, 7], "Test case 2 failed"
    assert primes_list(15) == [2, 3, 5, 7, 11, 13], "Test case 3 failed"
    assert primes_list(1) == [], "Test case 4 failed"
    
    print("primes_list passed all test cases.")

test_primes_list()

