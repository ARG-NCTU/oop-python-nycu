import mit_ocw_exercises.lec9_inheritance as lec9


def test_animal_person_student_rabbit():
    a = lec9.Animal(4)
    a.set_name('fluffy')
    assert a.get_age() == 4
    assert a.get_name() == 'fluffy'

    p = lec9.Person('jack', 30)
    assert p.get_name() == 'jack'
    p.add_friend('jill')
    assert 'jill' in p.get_friends()

    s = lec9.Student('alice', 20, 'CS')
    s.change_major('Math')
    assert s.major == 'Math'

    r1 = lec9.Rabbit(1)
    r2 = lec9.Rabbit(1)
    r3 = r1 + r2
    assert r3.get_parent1() is r1
    assert r3.get_parent2() is r2
    r4 = r2 + r1
    assert (r3 == r4) is True
