import add_path
import mit_ocw_exercises.lec9_inheritance as lec9
import pytest

def test_Animal():
    a = lec9.Animal(7)
    assert a.get_age() == 7
    assert str(a) == "animal:None:7"
    a.set_name("buddy")
    assert str(a) == "animal:buddy:7"
    a.set_name()
    assert str(a) == "animal::7"

def test_Cat():
    c = lec9.Cat(5)
    assert c.get_age() == 5
    assert str(c) == "cat:None:5"
    c.set_name("whiskers")
    assert str(c) == "cat:whiskers:5"

def test_Person():
    p = lec9.Person("Alice", 30)
    assert p.get_age() == 30
    assert str(p) == "person:Alice:30"
    assert p.get_friends() == []
    p.add_friend("Bob")
    assert p.get_friends() == ["Bob"]
    p.add_friend("Bob") 
    assert p.get_friends() == ["Bob"]  

def test_Student():
    s = lec9.Student("Charlie", 20, "Math")
    assert s.get_age() == 20
    assert str(s) == "student:Charlie:20:Math"
    assert s.major == "Math"
    s.change_major("Physics")
    assert s.major == "Physics"
    s.add_friend("Dave")
    assert s.get_friends() == ["Dave"]
    
def test_Rabbit():
    r7 = lec9.Rabbit(3)
    assert r7.get_age() == 3
    assert str(r7) == "rabbit:007"
    r7.set_name("Thumper")
    assert r7.get_rid()  == "007"
    assert r7.get_parent1() == None
    assert r7.get_parent2() == None
    r8 = lec9.Rabbit(4)
    assert r8.get_rid()  == "008"
    r8.set_name("jack")
    r9 = r7+r8
    r10 = r7 + r8
    assert  r9.get_parent1().get_rid() == "007"
    assert  r9.get_parent2().get_rid() == "008"
    a = ( r9 == r10)
    assert  a  == True
    