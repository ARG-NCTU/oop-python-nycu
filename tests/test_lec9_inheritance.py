import add_path
import mit_ocw_exercises.lec9_inheritance as inh
import pytest

def test12_animal():
    a = inh.Animal(4)
    print(a)
    print(a.get_age())
    a.set_name("fluffy")
    print(a)
    assert a.get_name() == "fluffy"
    assert a.get_age() == 4
    a.set_age(5)
    assert a.get_age() == 5
    
def test12_cat():
    c = inh.Cat(5)
    print(c)
    print(c.get_age())
    c.set_name("fluffy")
    print(c)
    assert c.get_name() == "fluffy"
    assert c.get_age() == 5
    c.set_age(6)
    assert c.get_age() == 6


