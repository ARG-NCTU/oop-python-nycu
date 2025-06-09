import pytest
import lec9_inheritance as lec9
import math

def test_animal():
    a = lec9.Animal(6)
    assert a.get_name() == None
    a.set_age(7)
    assert a.get_age() == 7
    a.set_name('johnny')
    assert a.get_name() == 'johnny'
    a.set_name('johnny_walker')
    assert a.get_name() == 'johnny_walker'

def test_cat():
    c = lec9.Cat(9)
    assert c.get_age() == 9
    
def test_Rabbit():
    r7 = lec9.Rabbit(5)
    r8 = lec9.Rabbit(7)
    assert r7.rid == 7
    r9 = r7 + r8
    assert r9.get_rid() == '009'
    r10 = r8 + r7
    assert (r9 == r10) == True
    


