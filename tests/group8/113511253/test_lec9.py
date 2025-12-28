import sys, os
import pytest
# 加入當前目錄到 sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lec9_inheritance import Animal, Cat, Person, Student, Rabbit

def test_animal_basic():
    a = Animal(4)
    assert a.get_age() == 4
    a.set_name("fluffy")
    assert str(a) == "animal:fluffy:4"

def test_student_inheritance():
    s = Student("alice", 20, "CS")
    assert isinstance(s, Person)
    assert isinstance(s, Animal)
    assert s.major == "CS"
    s.change_major("EE")
    assert s.major == "EE"

def test_rabbit_logic():
    Rabbit.tag = 1 
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r3 = r1 + r2
    assert r3.get_rid() == "003"
    assert r3.get_parent1() == r1
