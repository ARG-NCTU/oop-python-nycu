import lec4_functions as lec

def is_even_with_return_test():
    assert lec.is_even_with_return(13) == False
    assert lec.is_even_with_return(24) == True
    print("test successful!!")

def bisection_cuberoot_approx_test():
    assert lec.bisection_cuberoot_approx(27, 0.01) == 3.000091552734375
    assert lec.bisection_cuberoot_approx(1, 0.01) == 0.998046875
    print("test successful!!")

is_even_with_return_test()
bisection_cuberoot_approx_test()
