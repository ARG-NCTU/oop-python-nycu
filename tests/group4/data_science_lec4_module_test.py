import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import add_path
import numpy as np
from src.mit_ocw_data_science.lec4.lec4_module import roll_die, birthday_prob

def test_roll_die():
    for _ in range(100):
        result = roll_die()
        assert result in [1, 2, 3, 4, 5, 6]

def test_birthday_prob():
    prob_23_2 = birthday_prob(23, 2, 1000)
    assert 0.0 <= prob_23_2 <= 1.0 

    prob_50_3 = birthday_prob(50, 3, 1000)
    assert 0.0 <= prob_50_3 <= 1.0  
