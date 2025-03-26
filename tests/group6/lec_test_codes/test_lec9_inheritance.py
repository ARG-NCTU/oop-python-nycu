import add_path
import pytest

import mit_ocw_exercises.lec9_inheritance as lec9

# class animal test
def test_animal_init():
    a = lec9.Animal(1)
    assert a.get_age() == 1
    assert a.get_name() is None
  
def test_animal_set_name():
    a = lec9.Animal(5)
    a.set_name("5")
    assert a.get_name() == "5"

def test_animal_set_age():
    a = lec9.Animal(100)
    a.set_age(4)
    assert a.get_age() == 4

def test_animal_str():
    a = lec9.Animal(1)
    a.set_name("test")
    assert str(a) == "animal:test:1"

# cat test
# def test_cat_speak(capsys):

def test_cat_str():
    c = lec9.Cat(4)
    c.set_name("a")
    assert str(c) == "cat:a:4"

# person
def test_person_init():
    p = lec9.Person("a", 18)
    assert p.get_name() == "a"
    assert p.get_age() == 18
    assert p.get_friends() == []

def test_person_add_friend():
    p = lec9.Person("Bob", 30)
    p.add_friend("C")
    assert "C" in p.get_friends()

# def test_person_speak(capsys):


# def test_person_age_diff(capsys):


def test_person_str():
    p = lec9.Person("e", 278)
    assert str(p) == "person:e:278"

    
# student
def test_student_init():
    s = lec9.Student("A", 200, "A")
    assert s.get_name() == "A"
    assert s.get_age() == 200
    assert s.major == "A"

def test_student_change_major():
    s = lec9.Student("qwer", 7, "A")
    s.change_major("B")
    assert s.major == "B"

# def test_student_speak(capsys):

def test_student_str():
    s = lec9.Student("qaq", 21, "C")
    assert str(s) == "student:qaq:21:C"
# rabbit

def test_rabbit_init(): 
    r = lec9.Rabbit(2)
    assert r.get_age() == 2
    assert r.get_name() is None 
