import pytest
import math
from lec4_module import roll_die, run_sim, same_date, birthday_prob


def test_roll_die():
    # Test that the function returns an int between 1 and 6
    for i in range(100):
        result = roll_die()
        assert isinstance(result, int)
        assert result >= 1 and result <= 6
        assert result != 8
