import add_path
import pytest
import mit_ocw_exercises.lec9_inheritance as lec9
import random

def test_animal():
    a = lec9.Animal(4)
    assert a.get_age() == 4
    a.set_name("fluffy")
    assert str(a) == "animal:fluffy:4"
    a.set_name()
    assert str(a) == "animal::4"
    
def test_cat():
    c = lec9.Cat(5)
    c.set_name("fluffy")
    assert str(c) == "cat:fluffy:5"
    c.speak()
    assert c.get_age() == 5
    
def test_person():
    p1 = lec9.Person("jack", 30)
    p2 = lec9.Person("jill", 25)
    print(p1.get_name())
    print(p1.get_age())
    print(p2.get_name())
    print(p2.get_age())
    print(p1)
    p1.speak()
    p1.age_diff(p2)



