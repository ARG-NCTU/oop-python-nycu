import add_path
import pytest
from mit_ocw_exercises.lec9_inheritance import Animal, Cat, Person, Student, Rabbit

def test_animal_init():
    a = Animal(1)
    assert a.get_age() == 1
    assert a.get_name() is None
  
def test_animal_set_name():
    a = Animal(5)
    a.set_name("5")
    assert a.get_name() == "5"

def test_animal_set_age():
    a = Animal(100)
    a.set_age(4)
    assert a.get_age() == 4

def test_animal_str():
    a = Animal(1)
    a.set_name("test")
    assert str(a) == "animal:test:1"
