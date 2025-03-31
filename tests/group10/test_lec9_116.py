import add_path
import pytest
import mit_ocw_exercises.lec9_inheritance.py as lec9
import math

def test_animal():
    a = lec9.Animal(4)
    assert a.__str__() == "animal:None:4"
    assert a.get_age() == 4
    a.set_name("fluffy")
    assert a.__str__() == "animal:fluffy:4"
    assert a.set_name() == None
    
    