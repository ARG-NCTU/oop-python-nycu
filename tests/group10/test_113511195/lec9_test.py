import add_path
import lec9_inheritance as lec9

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