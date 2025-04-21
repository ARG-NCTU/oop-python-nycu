import add_path
import mit_ocw_exercises.lec5_tuples_lists as lec5  
import pytest
def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(5,3) == (1,2)
    assert lec5.quotient_and_remainder(5,2) == (2,1)
    assert lec5.quotient_and_remainder(10,5) == (2,0)
    assert lec5.quotient_and_remainder(10,3) == (3,1)
    assert lec5.quotient_and_remainder(10,4) == (2,2)
    assert lec5.quotient_and_remainder(10,6) == (1,4)
    assert lec5.quotient_and_remainder(10,7) == (1,3)
    assert lec5.quotient_and_remainder(10,8) == (1,2)
    assert lec5.quotient_and_remainder(10,9) == (1,1)
    assert lec5.quotient_and_remainder(10,10) == (1,0)

        
def test_get_data():
    test = ((1,"a"),(2, "b"),
        (1,"a"),(7,"b"))
    assert lec5.get_data(test) == (1, 7, 2)
    tswift = ((2014,"Katy"),
          (2014, "Harry"),
          (2012,"Jake"), 
          (2010,"Taylor"), 
          (2008,"Joe"))   
    assert lec5.get_data(tswift) == (2008, 2014, 5)
    
def test_sum_elem_method1():
    assert lec5.sum_elem_method1([1,2,3,4]) == 10
    assert lec5.sum_elem_method1([0,0,0,0]) == 0
    assert lec5.sum_elem_method1([-1,-2,-3,-4]) == -10
    assert lec5.sum_elem_method1([1,-2,3,-4]) == -2
    assert lec5.sum_elem_method1([1]) == 1
    assert lec5.sum_elem_method1([]) == 0
    
def test_sum_elem_method2():
    assert lec5.sum_elem_method2([1,2,3,4]) == 10
    assert lec5.sum_elem_method2([0,0,0,0]) == 0
    assert lec5.sum_elem_method2([-1,-2,-3,-4]) == -10
    assert lec5.sum_elem_method2([1,-2,3,-4]) == -2
    assert lec5.sum_elem_method2([1]) == 1
    assert lec5.sum_elem_method2([]) == 0

    
    
    
