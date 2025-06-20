import lec4_functions as lec
import pytest

def test_is_even_with_return():
    assert lec.is_even_with_return(13) == False
    assert lec.is_even_with_return(24) == True
    print("test successful!!")

def test_bisection_cuberoot_approx():
    assert lec.bisection_cuberoot_approx(27, 0.01) == 3.000091552734375
    assert lec.bisection_cuberoot_approx(1, 0.01) == 0.998046875
    print("test successful!!")

if __name__ == "__main__":
    pytest.main([__file__])
    # Alternatively, you can run pytest from the command line:
    # pytest test_lec4-1.py
