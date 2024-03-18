import add_path
import mit_ocw_exercises.lec8_classes as lc

def test_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5
def test_1_coordinate():
    a = lc.Coordinate(5, 12)
    assert a.distance(origin) == 13
    assert a.x == 5
    assert a.y == 12

def test_intset():
    s = lc.intSet()
    s.insert(3)
    s.insert(4)
    assert s.member(3)
    assert s.member(4)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)
    assert s.member(4)

def test_1_intset():
    b = lc.intSet()
    b.insert(10)
    b.insert(11)
    assert b.member(10)
    assert b.member(11)
    assert not b.member(12)
    b.remove(11)
    assert not b.member(11)
    assert b.member(10)
