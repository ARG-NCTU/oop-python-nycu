import add_path
import pytest
from mit_ocw_exercises.lec9_inheritance import Animal, Cat, Person, Student, Rabbit

# class animal test
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

# cat test
# def test_cat_speak(capsys):

def test_cat_str():
    c = Cat(4)
    c.set_name("a")
    assert str(c) == "cat:a:4"

# person
def test_person_init():
    p = Person("a", 18)
    assert p.get_name() == "a"
    assert p.get_age() == 18
    assert p.get_friends() == []

def test_person_add_friend():
    p = Person("Bob", 30)
    p.add_friend("C")
    assert "C" in p.get_friends()

# def test_person_speak(capsys):


# def test_person_age_diff(capsys):


def test_person_str():
    p = Person("e", 278)
    assert str(p) == "person:e:278"

    
# student

# rabbit
