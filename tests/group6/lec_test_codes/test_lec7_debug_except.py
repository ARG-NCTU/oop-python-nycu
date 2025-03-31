import add_path
import pytest
import mit_ocw_exercises.lec7_debug_except as lec7

def test_reverse_list():
  L = [1,2,3,4];
  U = [4,3,2,1];
  lec7.rev_list(L);
  assert U[:] == L[:]
  
def test_primes_list():
  A = [2];  
  assert lec7.primes_list(2) == A;

def test_get_ratios():
  assert (abs(2 - lec7.get_ratios(2,1)) < 1e-9);
