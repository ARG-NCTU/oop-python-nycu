import pytest
from lec6_112704050 import tower

def test_tower_moves():
    result = tower(2, "A", "C", "B")
    expected = [
        ("A", "B"),
        ("A", "C"),
        ("B", "C")
    ]
    assert result == expected

def test_tower_move_count():
    for n in range(1, 6):
        result = tower(n, "P1", "P2", "P3")
        expected_moves = 2 ** n - 1
        assert len(result) == expected_moves

from lec6_112704050 import fib2

def test_fib2_base_cases():
    assert fib2(0) == 0
    assert fib2(1) == 1

def test_fib2_recursive_cases():
    assert fib2(2) == 1
    assert fib2(3) == 2
    assert fib2(4) == 3
    assert fib2(5) == 5
    assert fib2(10) == 55
    assert fib2(15) == 610
    assert fib2(19) == 4181
