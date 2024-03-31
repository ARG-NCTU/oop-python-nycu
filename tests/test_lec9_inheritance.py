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
    
    
def test_16_animal():
    b = inh.Animal(5)
    print(b)
    print(b.get_age())
    b.set_name("Mona")
    print(b)
    assert b.get_name() == "Mona"
    assert b.get_age() == 5
    
def test_cat():
    c = inh.Cat(5)
    print(c)
    print(c.get_age())
    c.set_name("Mona")
    print(c)
    assert c.get_name() == "Mona"
    assert c.get_age() == 5

def test_16_person():
    p1 = inh.Person("John", 30)
    p2 = inh.Person("jill", 25)
    assert p1.get_name() == "John"
    assert p1.get_age() == 30
    assert p2.get_name() == "jill"
    assert p2.get_age() == 25

def test_16_student():
    s1 = inh.Student("alice", 20, "CS")
    s2 = inh.Student("beth", 18)
    assert s1.get_name() == "alice"
    assert s1.get_age() == 20
    assert s2.get_name() == "beth"
    assert s2.get_age() == 18

def test_16_rabbit():
    r1 = inh.Rabbit(3)
    r2 = inh.Rabbit(4)
    r3 = inh.Rabbit(5)
    r4 = r1 + r2
    r5 = r3+r4
    r6 = r4+r3
    assert r1.get_age() == 3
    assert r2.get_age() == 4
    assert r3.get_age() == 5
    assert r1.get_rid() == '007'
    assert r2.get_rid() == '008'
    assert r3.get_rid() == '009'
    assert r4.get_rid() == '010'
    assert r5.get_rid() == '011'
    assert r6.get_rid() == '012'
    assert r1.get_parent1() == None
    assert r1.get_parent2() == None
    
    

    
