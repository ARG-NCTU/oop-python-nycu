import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lec6_recursion

def test_factorial():
    assert lec6_recursion.factorial(5) == 120
    assert lec6_recursion.factorial(0) == 1

def test_fibonacci():
    # 0, 1, 1, 2, 3, 5, 8
    assert lec6_recursion.fibonacci(6) == 8
    assert lec6_recursion.fibonacci(0) == 0
