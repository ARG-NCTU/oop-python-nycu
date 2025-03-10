import add_path
import pytest
import mit_ocw_exercises.lec7_debug_except as lec7

def test_reverse_list():
  L = [1,2,3,4];
  U = [4,3,2,1];
  lec7.rev_list(L);
  assert U[:] == L[:]
  
