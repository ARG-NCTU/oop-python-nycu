import lec7_debug_except as lec
import pytest

def rev_list_test():
    L1 = [1, 2, 3, 4, 5]
    lec.rev_list(L1)
    assert L1 == [5, 4, 3, 2, 1]
    print(L1)
rev_list_test()

def primes_list_test():
    assert lec.primes_list(5) == [2, 3, 5]
    assert lec.primes_list(14) == [2, 3, 5, 7, 11, 13]
    print (lec.primes_list(14))
primes_list_test()

