import pytest
from src.mit_ocw_exercises import lec6_recursion_dictionaries as lec6

def test_towers_of_hanoi(capsys):
    lec6.Towers(2, 'A', 'B', 'C')
    captured = capsys.readouterr().out
    assert "move from A to C" in captured
    assert "move from A to B" in captured
    assert "move from C to B" in captured

def test_fib():
    assert lec6.fib(0) == 1
    assert lec6.fib(1) == 1
    assert lec6.fib(5) == 8
    assert lec6.fib(6) == 13



def test_fib_efficient():
    d = {1: 1, 2: 2}
    assert lec6.fib_efficient(5, d) == lec6.fib_efficient(4, d) + lec6.fib_efficient(3, d)
    # The memoization should work
    assert 5 in d
    assert 3 in d
