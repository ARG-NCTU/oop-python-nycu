import add_path
import mit_ocw_exercises.lec9_inheritance as inh
import pytest

def test_animal():
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

def test_person():
    p1 = inh.Person("Uhhuh", 18)
    p2 = inh.Person("Yeah", 19)
    print(p1.get_name())
    print(p1.get_age())
    print(p2.get_name())
    print(p2.get_age())
    assert p1.get_name() == "Uhhuh"
    assert p2.get_age() == 19
    p1.add_friend("friend1")
    print(p1.get_friends())
    p2.age_diff(p1)
    p2.speak()
    
