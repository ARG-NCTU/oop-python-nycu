import add_path
import mit_ocw_exercises.lec9_inheritance as inh
import pytest

def test_animal1():
    a = inh.Animal(10)
    print(a)
    print(a.get_age())
    a.set_name("Cutie")
    print(a)
    assert a.get_name() == "Cutie"
    assert a.get_age() == 10

def test_cat():
    c = inh.Cat(6)
    print(c)
    print(c.get_age())
    c.set_name("lulu")
    print(c)
    assert c.get_name() == "lulu"
    assert c.get_age() == 6
    c.set_age(3)
    assert c.get_age() == 3
