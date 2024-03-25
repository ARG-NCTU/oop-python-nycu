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

def test_1_animal():
    a = inh.Animal(4)
    print(a)
    print(a.get_age())  
    a.set_name("fluffy")
    print(a)
    assert a.get_name() == "fluffy"
    assert a.get_age() == 4
    b = inh.Animal(5)
    assert b.get_age() == 5
    b.set_name("tiger")
    assert b.get_name() == "tiger"
    c = inh.Animal(6)
    assert c.get_age() == 6
    c.set_name("lion")
    assert c.get_name() == "lion"
    d = inh.Animal(7)
    assert d.get_age() == 7
    d.set_name("elephant")
    assert d.get_name() == "elephant"
    e = inh.Animal(8)
    assert e.get_age() == 8
    e.set_name("giraffe")
    assert e.get_name() == "giraffe"

def test_person():
    a = inh.Animal(19)
    print(a)
    print(a.get_age())
    a.set_name("PPPP")
    print(a)
    assert a.get_name() == "PPPP"

def test_1_animal():
    b= inh.Animal(7)
    print(b)
    b.set_name("What is this?")
    assert b.get_name() == "What is this?"
    assert b.get_age() == 7

def test_1_animal():
    b = inh.Animal(7)
    b.set_name("luffy")
    assert b.get_age() == 7
    assert b.get_name() == "luffy"

def test_13_animal():
    a = inh.Animal(19)
    print(a)
    print(a.get_age())
    a.set_name("Yuyu")
    print(a)
    assert a.get_name() == "Yuyu"
    assert a.get_age() == 19
    
def test_person():
    a = inh.Animal(19)
    print(a)
    print(a.get_age())
    a.set_name("PPPP")
    print(a)
    assert a.get_name() == "PPPP"
    assert a.get_age() == 19

