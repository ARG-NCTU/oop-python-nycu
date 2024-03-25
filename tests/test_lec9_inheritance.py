import add_path
import mit_ocw_exercises.lec9_inheritance as inh
import pytest

def test_animal_5A():
    a = inh.Animal(4)
    print(a)
    print(a.get_age())
    a.set_name("fluffy")
    print(a)
    assert a.get_name() == "fluffy"
    assert a.get_age() == 4
    a.set_name('outgoing')
    assert a.get_name() == 'outgoing'
    a.set_age(5)
    assert a.get_age() == 5
    assert a.__str__() == "animal:outgoing:5"



