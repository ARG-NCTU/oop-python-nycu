import add_path
import mit_ocw_exercises.lec9_inheritance as lec9
import pytest
import random

def test_animal_basic():
    a = lec9.Animal(4)
    assert a.get_age() == 4
    assert a.get_name() is None
    a.set_name("fluffy")
    assert a.get_name() == "fluffy"
    a.set_age(5)
    assert a.get_age() == 5
    a.set_name()
    assert a.get_name() == ""
    assert str(a) == "animal::5"

def test_cat_inheritance_and_str():
    c = lec9.Cat(3)
    c.set_name("kitty")
    assert c.get_age() == 3
    assert c.get_name() == "kitty"
    assert str(c) == "cat:kitty:3"

def test_person_and_friends_and_age_diff(capsys):
    p1 = lec9.Person("jack", 30)
    p2 = lec9.Person("jill", 25)
    assert p1.get_name() == "jack"
    assert p2.get_name() == "jill"
    assert p1.get_age() == 30
    assert p2.get_age() == 25
    assert p1.get_friends() == []
    p1.add_friend("jill")
    assert "jill" in p1.get_friends()
    p1.add_friend("jill")  # 不會重複加入
    assert p1.get_friends().count("jill") == 1
    assert str(p1) == "person:jack:30"

    # 測試 speak() 和 age_diff 輸出
    p1.speak()
    out = capsys.readouterr().out
    assert "hello" in out

    p1.age_diff(p2)
    diff_output = capsys.readouterr().out
    assert "5 year difference" in diff_output

def test_student_inheritance_and_major_and_speak(monkeypatch, capsys):
    s = lec9.Student("amy", 21, "Math")
    assert s.get_name() == "amy"
    assert s.get_age() == 21
    assert s.major == "Math"
    assert str(s) == "student:amy:21:Math"
    s.change_major("Physics")
    assert s.major == "Physics"

    # 測試 speak() 的不同隨機輸出
    monkeypatch.setattr(random, "random", lambda: 0.1)
    s.speak()
    out = capsys.readouterr().out
    assert "i have homework" in out

    monkeypatch.setattr(random, "random", lambda: 0.3)
    s.speak()
    out = capsys.readouterr().out
    assert "i need sleep" in out

    monkeypatch.setattr(random, "random", lambda: 0.6)
    s.speak()
    out = capsys.readouterr().out
    assert "i should eat" in out

    monkeypatch.setattr(random, "random", lambda: 0.9)
    s.speak()
    out = capsys.readouterr().out
    assert "i am watching tv" in out

def test_rabbit_basic_and_add_and_eq():
    # Reset class variable for consistent test
    lec9.Rabbit.tag = 1
    r1 = lec9.Rabbit(3)
    r2 = lec9.Rabbit(4)
    r3 = lec9.Rabbit(5)

    # 測 rid 生成
    assert r1.get_rid() == "001"
    assert r2.get_rid() == "002"
    assert r3.get_rid() == "003"
    assert r1.get_parent1() is None
    assert r1.get_parent2() is None
    assert str(r1) == "rabbit:001"




