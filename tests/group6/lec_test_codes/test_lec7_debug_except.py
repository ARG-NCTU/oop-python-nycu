import add_path
import pytest
import mit_ocw_exercises.lec7_debug_except as lec7

def test_reverse_list():
  L = [1,2,3,4]
  U = [4,3,2,1]
  lec7.rev_list(L)
  assert L[:] == U[:]
  assert U[:] == L[:]

  
def test_primes_list():
  A = [2];  B = [2,3]; C = [2,3,5]; D = [2,3,5,7]
  assert lec7.primes_list(1) == A
  assert lec7.primes_list(2) == A
  assert lec7.primes_list(3) == B
  assert lec7.primes_list(4) == B


def test_get_ratios():
  assert lec7.get_ratios([2],[1]) == [2]
  assert lec7.get_ratios([2],[3]) <= [0.67]
  assert lec7.get_ratios([2,3],[1,2]) == [2,1.5]
  assert lec7.get_ratios([2,3],[1,2]) == [2,1.5]
  assert lec7.get_ratios([2,3,4],[1,2,3]) == [2,1.5,1.3333333333333333]

  
  
