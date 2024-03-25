import add_path
import mit_ocw_exercises.lec9_inheritance as inh
import pytest

def test_animal():
    a = inh.Animal(4)
    print(a)
    print(a.get_age())
    a.set_name("fluffy")
    print(a)
    assert a.get_name() == "fluffy"
    assert a.get_age() == 4

def test_10_animal():
    a = inh.Animal(5)
    assert a.get_age() == 5

def test_100_animal():
    a = inh.Animal(8)
    a.set_name("daniel") 
    assert a.get_name() == "daniel"
    assert a.get_age() == 8 
