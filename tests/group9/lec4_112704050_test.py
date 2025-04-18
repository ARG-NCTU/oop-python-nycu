import pytest
from lec4_112704050 import even_odd

def test_even_odd_1():
    result = even_odd(2)
    assert result == True
    result = even_odd(3)
    assert result == False


from lec4_112704050 import bisection_cuberoot_approx

def test_bisection_cuberoot_approx():
    result = bisection_cuberoot_approx(27,0.01)
    assert 2.99 <= result <= 3.01
    result = bisection_cuberoot_approx(20,0.01)
    assert 20**(1/3)-0.01 <= 20**(1/3) <= 20**(1/3)+0.01
    result = bisection_cuberoot_approx(-27,0.01)
    assert -3.01 <= result <= -2.99
    result = bisection_cuberoot_approx(-20,0.01)
    assert -20**(1/3)-0.01 <= result <= -20**(1/3)+0.01


from lec4_112704050 import just_return

def test_bisection_cuberoot_approx_add():
    num_input = just_return(1)(10,5)
    assert num_input == 15
    num_input = just_return(1)(-10,-5)
    assert num_input == -15
    num_input = just_return(1)(0,0)
    assert num_input == 0
    num_input = just_return(1)(-1,10)
    assert num_input == 9

def test_bisection_cuberoot_approx_minus():
    num_input = just_return(2)(10,5)
    assert num_input == 5
    num_input = just_return(2)(-10,-5)
    assert num_input == -5
    num_input = just_return(2)(0,0)
    assert num_input == 0
    num_input = just_return(0.5)(-10,0)
    assert num_input == -10
    num_input = just_return(0.5)(-1,10)
    assert num_input == -11
import numpy as np
from lec4_112704050 import generate_score, pass_or_not

def test_generate_score_deterministic():
    seed = 42
    total = generate_score(seed)

    # 若你想保證輸出值固定，可印出並寫死
    assert isinstance(total, (int,np.integer))
    assert 0 <= total <= 1000

def test_generate_score_repeatable():
    seed = 1234
    total1 = generate_score(seed)
    total2 = generate_score(seed)
    assert total1 == total2  # 相同 seed，結果要一樣

def test_generate_score_randomness():
    # 不同 seed，應該大多情況下結果不同
    total1 = generate_score(1)
    total2 = generate_score(2)
    assert total1 != total2  # 偶爾一樣無妨，但通常不會一樣

def test_pass_or_not_pass():
    result = pass_or_not(999)
    assert result == 1
    result = pass_or_not(601)
    assert result == 1
    result = pass_or_not(599)
    assert result == 1
    result = pass_or_not(0)
    assert result == 1
    result = pass_or_not(-100)
    assert result == 1

import numpy as np
from lec4_112704050 import return_book

def test_return_book_fixed_seed_10_returned():
    result = return_book(0.8,10)
    assert result == 1 
    result = return_book(0.78,10)
    assert result == 1 
    result = return_book(0.85,10)
    assert result == 1 
    result = return_book(0.9,10)
    assert result == 1 

def test_return_book_fixed_seed_10_nonreturned():
    result = return_book(0.7,10)
    assert result == 0
    result = return_book(0.76,10)
    assert result == 0 
    result = return_book(0.15,10)
    assert result == 0
    result = return_book(0.1,10)
    assert result == 0    

def test_return_book_fixed_seed_0_returned():
    result = return_book(0.56,0)
    assert result == 1 
    result = return_book(0.78,0)
    assert result == 1 
    result = return_book(0.85,0)
    assert result == 1 
    result = return_book(0.9,0)
    assert result == 1 

def test_return_book_fixed_seed_0_nonreturned():
    result = return_book(0.5,0)
    assert result == 0
    result = return_book(0.53,0)
    assert result == 0 
    result = return_book(0.15,0)
    assert result == 0
    result = return_book(0.1,0)
    assert result == 0    



    