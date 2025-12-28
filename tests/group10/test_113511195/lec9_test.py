import add_path
import lec9_inheritance as lec9
import pytest

def test_animal_init_defaults():
    a = lec9.Animal(4)
    assert lec9.Animal.get_age(a) == 4
    assert lec9.Animal.get_name(a) == None

def test_animal_set_age():
    a = lec9.Animal(4)
    lec9.Animal.set_age(a, 10)
    assert lec9.Animal.get_age(a) == 10
    
def test_animal_set_name_explicit():
    a = lec9.Animal(4)
    lec9.Animal.set_name(a, "fluffy")
    assert lec9.Animal.get_name(a) == "fluffy"
    assert str(a) == "animal:fluffy:4"

def test_animal_set_name_default_empty_string():
    a = lec9.Animal(4)
    lec9.Animal.set_name(a)  # default newname=""
    assert lec9.Animal.get_name(a) == ""
    assert str(a) == "animal::4"

def test_animal_str_when_name_none():
    a = lec9.Animal(4)
    assert str(a) == "animal:None:4"

def test_cat_inherits_animal_getters_setters_and_str():
    c = lec9.Cat(5)
    lec9.Animal.set_name(c, "fluffy")
    assert lec9.Animal.get_age(c) == 5
    assert lec9.Animal.get_name(c) == "fluffy"
    # Cat overrides __str__
    assert str(c) == "cat:fluffy:5"

def test_cat_speak_prints_meow(capsys):
    c = lec9.Cat(5)
    lec9.Cat.speak(c)
    out = capsys.readouterr().out.strip()
    assert out == "meow"

def test_person_init_sets_name_age_and_friends():
    p = lec9.Person("jack", 30)
    assert lec9.Animal.get_name(p) == "jack"
    assert lec9.Animal.get_age(p) == 30
    assert lec9.Person.get_friends(p) == []
    assert str(p) == "person:jack:30"

def test_person_speak_prints_hello(capsys):
    p = lec9.Person("jack", 30)
    lec9.Person.speak(p)
    out = capsys.readouterr().out.strip()
    assert out == "hello"

def test_person_add_friend_unique_only():
    p = lec9.Person("jack", 30)
    lec9.Person.add_friend(p, "jill")
    lec9.Person.add_friend(p, "jill")  # duplicate should not be added
    lec9.Person.add_friend(p, "bob")
    assert lec9.Person.get_friends(p) == ["jill", "bob"]


def test_person_age_diff_prints_absolute_difference(capsys):
    p1 = lec9.Person("jack", 30)
    p2 = lec9.Person("jill", 25)
    lec9.Person.age_diff(p1, p2)
    out = capsys.readouterr().out.strip()
    assert out == "5 year difference"

def test_person_age_diff_symmetric_value(capsys):
    p1 = lec9.Person("jack", 30)
    p2 = lec9.Person("jill", 25)
    lec9.Person.age_diff(p2, p1)
    out = capsys.readouterr().out.strip()
    assert out == "5 year difference"

def test_student_init_major_default_none_and_str():
    s = lec9.Student("beth", 18)
    assert lec9.Animal.get_name(s) == "beth"
    assert lec9.Animal.get_age(s) == 18
    assert s.major is None
    assert str(s) == "student:beth:18:None"

def test_student_init_major_provided_and_str():
    s = lec9.Student("alice", 20, "CS")
    assert s.major == "CS"
    assert str(s) == "student:alice:20:CS"

def test_student_change_major():
    s = lec9.Student("alice", 20, "CS")
    lec9.Student.change_major(s, "Math")
    assert s.major == "Math"
    assert str(s) == "student:alice:20:Math"

@pytest.mark.parametrize(
    "r, expected",
    [
        (0.00, "i have homework"),
        (0.24, "i have homework"),
        (0.25, "i need sleep"),
        (0.49, "i need sleep"),
        (0.50, "i should eat"),
        (0.74, "i should eat"),
        (0.75, "i am watching tv"),
        (0.99, "i am watching tv"),
    ],
)
def test_student_speak_deterministic(monkeypatch, capsys, r, expected):
    s = lec9.Student("alice", 20, "CS")
    monkeypatch.setattr(lec9.random, "random", lambda: r)
    lec9.Student.speak(s)
    out = capsys.readouterr().out.strip()
    assert out == expected

@pytest.fixture
def reset_rabbit_tag():
    """
    Ensure Rabbit.tag is reset for deterministic rid numbering across tests.
    """
    old = lec9.Rabbit.tag
    lec9.Rabbit.tag = 1
    yield
    lec9.Rabbit.tag = old

def test_rabbit_init_rid_and_parents_none(reset_rabbit_tag):
    r1 = lec9.Rabbit(3)
    r2 = lec9.Rabbit(4)
    r3 = lec9.Rabbit(5)

    assert lec9.Rabbit.get_rid(r1) == "001"
    assert lec9.Rabbit.get_rid(r2) == "002"
    assert lec9.Rabbit.get_rid(r3) == "003"

    assert lec9.Rabbit.get_parent1(r1) is None
    assert lec9.Rabbit.get_parent2(r1) is None

    assert str(r1) == "rabbit:001"
    assert str(r2) == "rabbit:002"
    assert str(r3) == "rabbit:003"

def test_rabbit_add_creates_child_with_parents(reset_rabbit_tag):
    r1 = lec9.Rabbit(3)
    r2 = lec9.Rabbit(4)

    r4 = r1 + r2  # uses __add__

    # rid sequence: r1=001 r2=002 r4=003
    assert lec9.Rabbit.get_rid(r4) == "003"
    assert lec9.Rabbit.get_parent1(r4) is r1
    assert lec9.Rabbit.get_parent2(r4) is r2
    assert str(r4) == "rabbit:003"

def test_rabbit_eq_false_when_missing_parents(reset_rabbit_tag):
    r1 = lec9.Rabbit(3)
    r2 = lec9.Rabbit(4)
    assert (r1 == r2) is False

    r3 = lec9.Rabbit(5)
    r4 = r1 + r2
    # r3 has no parents, so equality should be False
    assert (r3 == r4) is False

def test_rabbit_eq_true_same_parents_order_independent(reset_rabbit_tag):
    r3 = lec9.Rabbit(5)
    r4 = lec9.Rabbit(6)

    r5 = r3 + r4
    r6 = r4 + r3

    assert (r5 == r6) is True
    assert (r6 == r5) is True


def test_rabbit_eq_false_different_parents(reset_rabbit_tag):
    r1 = lec9.Rabbit(3)
    r2 = lec9.Rabbit(4)
    r3 = lec9.Rabbit(5)

    child_a = r1 + r2
    child_b = r1 + r3
    assert (child_a == child_b) is False
