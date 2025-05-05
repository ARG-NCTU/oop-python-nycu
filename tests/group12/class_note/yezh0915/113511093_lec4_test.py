import pytest
from src.mit_ocw_exercises.lec4_functions import (
    is_even_with_return,
    bisection_cuberoot_approx,
    f,
    g
)

def test_is_even_with_return():
    assert is_even_with_return(2) == True
    assert is_even_with_return(3) == False
    assert is_even_with_return(0) == True

if __name__ == "__main__":
    pytest.main()
