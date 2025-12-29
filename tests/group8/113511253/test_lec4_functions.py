import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lec4_functions

def test_eval_quadratic():
    # x^2 + 2x + 1 at x=2 => 4 + 4 + 1 = 9
    assert lec4_functions.eval_quadratic(1, 2, 1, 2) == 9

def test_clip():
    assert lec4_functions.clip(0, 5, 10) == 5
    assert lec4_functions.clip(0, -5, 10) == 0
    assert lec4_functions.clip(0, 15, 10) == 10
