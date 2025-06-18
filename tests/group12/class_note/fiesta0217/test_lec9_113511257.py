import add_path
import pytest
import mit_ocw_exercises.lec9_inheritance as lec9

def test_animal_init_and_str():
    a = lec9.Animal(4)
    assert a.age == 4
    assert a.name is None
    assert str(a) == "animal:None:4"
    a.set_name("fluffy")
    assert a.get_name() == "fluffy"
    a.set_age(8)
    assert a.get_age() == 8
    a.set_name()
    assert a.get_name() == ""

def test_cat_inheritance():
    c = lec9.Cat(5)
    c.set_name("fluffy")
    assert c.get_age() == 5
    assert c.get_name() == "fluffy"
    assert str(c) == "cat:fluffy:5"

def test_person_inheritance_and_friends():
    p1 = lec9.Person("jack", 30)
    p2 = lec9.Person("jill", 25)
    assert p1.get_name() == "jack"
    assert p1.get_age() == 30
    assert p2.get_name() == "jill"
    assert p2.get_age() == 25
    p1.add_friend("jill")
    assert "jill" in p1.get_friends()
    p1.add_friend("alice")
    assert "alice" in p1.get_friends()
    # 不能重複
    p1.add_friend("jill")
    assert p1.get_friends().count("jill") == 1
    assert str(p1) == "person:jack:30"

def test_student_inheritance():
    s1 = lec9.Student("alice", 20, "CS")
    s2 = lec9.Student("beth", 18)
    assert s1.get_name() == "alice"
    assert s1.get_age() == 20
    assert s1.major == "CS"
    assert s2.major is None
    s2.change_major("Math")
    assert s2.major == "Math"
    assert str(s1).startswith("student:alice:20:CS")
'''
def test_rabbit_tag_and_add():
    lec9.Rabbit.tag = 1  # reset class var for repeatable test
    r1 = lec9.Rabbit(3)
    r2 = lec9.Rabbit(4)
    r3 = lec9.Rabbit(5)
    assert r1.get_rid() == "001"
    assert r2.get_rid() == "002"
    assert r3.get_rid() == "003"
    r4 = r1 + r2
    assert isinstance(r4, lec9.Rabbit)
    assert r4.age == 0
    assert r4.get_parent1() == r1
    assert r4.get_parent2() == r2
    # test equality
    r5 = r3 + r4
    r6 = r4 + r3
    assert (r5 == r6) is True
    assert (r4 == r6) is False
    assert r4.get_parent1() is r1  # 用 is 更直觀地比較
'''