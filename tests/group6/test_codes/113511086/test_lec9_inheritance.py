import add_path
import mit_ocw_exercises.lec9_inheritance as inh
import pytest

# =========================
# Animal Tests
# =========================
def test_animal_basic():
    a = inh.Animal(4)
    assert a.get_age() == 4
    assert a.get_name() is None
    a.set_name("Fluffy")
    assert a.get_name() == "Fluffy"
    a.set_age(5)
    assert a.get_age() == 5
    assert str(a) == "animal:Fluffy:5"

def test_animal_multiple_instances():
    names = ["Tiger", "Lion", "Elephant"]
    ages = [5, 6, 7]
    animals = [inh.Animal(age) for age in ages]
    for i, animal in enumerate(animals):
        animal.set_name(names[i])
        assert animal.get_name() == names[i]
        assert animal.get_age() == ages[i]

# =========================
# Cat Tests
# =========================
def test_cat_inheritance_and_methods():
    c = inh.Cat(5)
    assert c.get_age() == 5
    assert c.get_name() is None
    c.set_name("Mona")
    assert c.get_name() == "Mona"
    assert str(c) == "cat:Mona:5"
    c.speak()  # should print "meow"

# =========================
# Person Tests
# =========================
def test_person_basic():
    p = inh.Person("John", 25)
    assert p.get_name() == "John"
    assert p.get_age() == 25
    p.set_name("Jane")
    p.set_age(26)
    assert p.get_name() == "Jane"
    assert p.get_age() == 26

def test_person_friends_and_speak():
    p = inh.Person("Alice", 20)
    p.add_friend("Bob")
    p.add_friend("Charlie")
    p.add_friend("Bob")  # duplicate should not be added
    friends = p.get_friends()
    assert friends == ["Bob", "Charlie"]
    p.speak()  # should print "hello"

def test_person_age_diff(capsys):
    p1 = inh.Person("Alice", 20)
    p2 = inh.Person("Bob", 25)
    p1.age_diff(p2)
    captured = capsys.readouterr()
    assert "5 year difference" in captured.out

# =========================
# Student Tests
# =========================
def test_student_inheritance_and_major():
    s = inh.Student("Ella", 22, "Nano")
    assert s.get_name() == "Ella"
    assert s.get_age() == 22
    assert s.major == "Nano"
    s.change_major("ECE")
    assert s.major == "ECE"
    s.set_name("Johnson")
    assert s.get_name() == "Johnson"
    s.speak()  # should print "I am a student"

# =========================
# Rabbit Tests
# =========================
def test_rabbit_basic_and_rid():
    r1 = inh.Rabbit(3)
    r2 = inh.Rabbit(4)
    r3 = inh.Rabbit(5)
    assert r1.get_age() == 3
    assert r1.get_parent1() is None
    assert r1.get_parent2() is None
    assert r1.get_rid() == "027"  # class variable increments
    assert r2.get_rid() == "028"
    assert r3.get_rid() == "029"

def test_rabbit_breeding_and_eq():
    r1 = inh.Rabbit(2)
    r2 = inh.Rabbit(3)
    r3 = r1 + r2
    r4 = r2 + r1
    # r3 and r4 should have parents r1 and r2 in any order
    assert r3 == r4
    assert r3.get_parent1() == r1
    assert r3.get_parent2() == r2

def test_rabbit_str_and_name():
    r = inh.Rabbit(1)
    r.set_name("Bunny")
    assert r.get_name() == "Bunny"
    assert str(r) == "rabbit:Bunny:1"
