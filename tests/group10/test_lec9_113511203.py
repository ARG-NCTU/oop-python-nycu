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
