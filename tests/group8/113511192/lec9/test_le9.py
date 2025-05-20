import add_path
import lec9 as inh
import pytest


def test_person():
    p1 = inh.Person("Alice", 30)
    p2 = inh.Person("Bob", 25)
    assert p1.get_name() == "Alice"
    assert p2.get_age() == 25

    p1.add_friend("Charlie")
    p1.add_friend("Dana")
    assert p1.get_friends() == ["Charlie", "Dana"]
    p1.add_friend("Charlie")  # Should not duplicate
    assert p1.get_friends() == ["Charlie", "Dana"]

def test_student_change_major_and_friends():
    s = inh.Student("Jane", 21, "Math")
    assert str(s) == "student:Jane:21:Math"
    s.change_major("Physics")
    assert str(s) == "student:Jane:21:Physics"

    s.add_friend("Tom")
    s.add_friend("Jerry")
    assert s.get_friends() == ["Tom", "Jerry"]
    s.add_friend("Tom")  # Should not duplicate
    assert s.get_friends() == ["Tom", "Jerry"]
    

def test_rabbit_creation_and_parents():
    RabbitClass = inh.Rabbit
    RabbitClass.tag = 1  # 重設計數器

    r1 = RabbitClass(2)
    r2 = RabbitClass(3)

    assert r1.get_parent1() is None
    assert r1.get_parent2() is None
    assert r1.get_rid() == "001"
    assert r2.get_rid() == "002"

    r3 = r1 + r2

    # 檢查 r3.parent1 和 r1 是同一物件
    assert r3.get_parent1() is r1
    # 檢查 r3.parent2 和 r2 是同一物件
    assert r3.get_parent2() is r2
    assert r3.get_rid() == "003"



def test_rabbit_equality():
    RabbitClass = inh.Rabbit
    RabbitClass.tag = 1  # Reset tag to test predictable rid values

    ra = RabbitClass(2)
    rb = RabbitClass(3)
    rc = ra + rb
    rd = ra + rb
    re = rb + ra

    assert rc == rd  # Same parents, same order
    assert rc == re  # Same parents, reversed order

    rf = rc + ra
    assert rc != rf  # Different parents

def test_rabbit_str_and_rid_formatting():
    RabbitClass = inh.Rabbit
    RabbitClass.tag = 1  # Reset tag

    r = RabbitClass(1)
    assert str(r) == "rabbit:001"
    for _ in range(9):
        RabbitClass(1)
    r10 = RabbitClass(1)
    assert r10.get_rid() == "011"  # Tag starts from 1
