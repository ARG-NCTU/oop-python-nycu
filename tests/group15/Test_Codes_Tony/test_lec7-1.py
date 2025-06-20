import lec7_debug_except as lec
import pytest

def test_rev_list():
    L1 = [1, 2, 3, 4, 5]
    lec.rev_list(L1)
    assert L1 == [5, 4, 3, 2, 1]
    print(L1)

def test_primes_list():
    assert lec.primes_list(5) == [2, 3, 5]
    assert lec.primes_list(14) == [2, 3, 5, 7, 11, 13]
    print (lec.primes_list(14))

if __name__ == "__main__":
    pytest.main([__file__])
    # Alternatively, you can run pytest from the command line:
    # pytest test_lec7-1.py

