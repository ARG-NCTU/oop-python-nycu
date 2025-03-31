from functions import is_even_with_return, is_even_without_return, is_even, bisection_cuberoot_approx

def test_is_even_with_return():
    assert is_even_with_return(3) == False
    assert is_even_with_return(4) == True
    assert is_even_with_return(0) == True
    assert is_even_with_return(1) == False
    assert is_even_with_return(103) == False

