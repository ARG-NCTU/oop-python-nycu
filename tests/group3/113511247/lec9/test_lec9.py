import pytest
import random

from lecture9_inheritance import Animal, Cat, Person, Student, Rabbit

def test_animal():
    a = Animal(4)
    
    assert a.get_age() == 4
    assert a.get_name() is None

    
    a.set_name("fluffy")
    assert a.get_name() == "fluffy"
    assert str(a) == "animal:fluffy:4"

    
    a.set_name()
    assert a.get_name() == ""

def test_cat(capsys):
    c = Cat(5)
    c.set_name("fluffy")
    
    assert str(c) == "cat:fluffy:5"
    assert c.get_age() == 5

    
    c.speak()
    captured = capsys.readouterr().out.strip()
    assert captured == "meow"

def test_person(capsys):
    p1 = Person("jack", 30)
    p2 = Person("jill", 25)
   
    assert p1.get_name() == "jack"
    assert p1.get_age() == 30
    assert p2.get_name() == "jill"
    assert p2.get_age() == 25
    assert str(p1) == "person:jack:30"

    
    p1.speak()
    captured = capsys.readouterr().out.strip()
    assert captured == "hello"

    p1.add_friend("alice")
    assert "alice" in p1.get_friends()

    
    p1.age_diff(p2)
    captured = capsys.readouterr().out.strip()
    
    assert "5" in captured and "year difference" in captured

def test_student_speak(monkeypatch, capsys):
    s = Student("alice", 20, "CS")
    

    monkeypatch.setattr(random, "random", lambda: 0.1)
    s.speak()
    captured = capsys.readouterr().out.strip()
    assert captured == "i have homework"
    
  
    monkeypatch.setattr(random, "random", lambda: 0.3)
    s.speak()
    captured = capsys.readouterr().out.strip()
    assert captured == "i need sleep"
    
 
    monkeypatch.setattr(random, "random", lambda: 0.6)
    s.speak()
    captured = capsys.readouterr().out.strip()
    assert captured == "i should eat"
    

    monkeypatch.setattr(random, "random", lambda: 0.8)
    s.speak()
    captured = capsys.readouterr().out.strip()
    assert captured == "i am watching tv"

def test_student_str_and_change_major():
    s1 = Student("alice", 20, "CS")
    s2 = Student("beth", 18)
   
    assert str(s1) == "student:alice:20:CS"
    assert str(s2) == "student:beth:18:None"
    
   
    s2.change_major("Math")
    assert s2.major == "Math"
    assert str(s2) == "student:beth:18:Math"

def test_rabbit():
    
    Rabbit.tag = 1
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r3 = Rabbit(5)
    
    
    expected_rid = "001"  
    assert r1.get_rid() == expected_rid
    assert str(r1) == "rabbit:" + expected_rid
   
    assert r1.get_parent1() is None
    assert r1.get_parent2() is None

    
    r4 = r1 + r2
    assert r4.age == 0
    assert r4.get_parent1() == r1
    assert r4.get_parent2() == r2

    
    r5 = r3 + r4
    r6 = r4 + r3
    assert r5 == r6 

    assert r4 != r6
