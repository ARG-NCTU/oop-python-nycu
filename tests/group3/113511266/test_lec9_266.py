import add_path
import mit_ocw_exercises.lec9_inheritance as lec9


def test_animal():
    a = lec9.Animal(4)
    assert a.get_age() == 4
    assert a.get_name() is None
    a.set_name("fluffy")
    assert a.get_name() == "fluffy"
    a.set_name()
    assert a.get_name() == ""

def test_cat():
    c = lec9.Cat(5)
    c.set_name("whiskers")
    assert str(c) == "cat:whiskers:5"
    assert c.get_age() == 5

def test_person():
    p1 = lec9.Person("alice", 30)
    p2 = lec9.Person("bob", 25)
    assert p1.get_name() == "alice"
    assert p1.get_age() == 30
    assert p2.get_name() == "bob"
    assert p2.get_age() == 25
    p1.add_friend("charlie")
    p1.add_friend("david")
    assert p1.get_friends() == ["charlie", "david"]
    p1.age_diff(p2)  # Should print "5 year difference"
    assert str(p1) == "person:alice:30"

def test_student():
    s = lec9.Student("eve", 20, "MIT")
    assert s.get_name() == "eve"
    assert s.get_age() == 20
    s.add_friend("frank")
    assert s.get_friends() == ["frank"]
    assert str(s) == "student:eve:20:MIT"


def test_Rabbit():
    # reset class counter to ensure test isolation when running whole group
    # set to 7 so that after creating r1 the tag becomes 8 (expected by test)
    lec9.Rabbit.tag = 7
    r1 = lec9.Rabbit(2, "r0")
    assert lec9.Rabbit.tag == 8
    r2 = lec9.Rabbit(3, "r1", "r3")
    assert lec9.Rabbit.tag == 9
    assert r1.get_rid() == "007"
    assert r1.get_parent1() == "r0"
    assert r2.get_parent2() == "r3"
    r1.set_age(5)
    assert r1.get_age() == 5
    r4 = r1 + r2
    assert isinstance(r4, lec9.Rabbit)
    assert r4.get_parent1() is r1
    assert str(r4) == "rabbit:009"
    r5 = r2 + r1
    assert (r4 == r5) is True
    r6 = lec9.Rabbit(1)
    assert (r4 == r6) is False
    assert str(r6) == "rabbit:011"
    assert lec9.Rabbit.tag == 12
    

