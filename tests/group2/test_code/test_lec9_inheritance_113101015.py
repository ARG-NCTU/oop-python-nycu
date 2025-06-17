import pytest
import lec9_inheritance as lec9
import math

def test_animal():
    a = lec9.Animal(6)
    assert a.get_name() == None
    a.set_age(7)
    assert a.get_age() == 7

def test_cat():
    c = lec9.Cat(9)
    assert c.get_age() == 9
    c.set_age(7)
    assert c.get_age() == 7#change its age using class inheritance

