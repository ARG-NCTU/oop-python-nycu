import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lec5_tuples_lists

def test_odd_tuples():
    t = ('I', 'am', 'a', 'test', 'tuple')
    # index 0, 2, 4 -> 'I', 'a', 'tuple'
    assert lec5_tuples_lists.odd_tuples(t) == ('I', 'a', 'tuple')

def test_sum_list():
    assert lec5_tuples_lists.sum_list([1, 2, 3]) == 6
    assert lec5_tuples_lists.sum_list([]) == 0
