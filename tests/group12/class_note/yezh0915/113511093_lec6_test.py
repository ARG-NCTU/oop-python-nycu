import pytest
from src.mit_ocw_exercises import lec6_recursion_dictionaries as lec6

def test_towers_of_hanoi(capsys):
    lec6.Towers(2, 'A', 'B', 'C')
    captured = capsys.readouterr().out
    assert "move from A to C" in captured
    assert "move from A to B" in captured
    assert "move from C to B" in captured

