import add_path
import mit_ocw_exercises.lec8_classes as lc

def test_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5

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

def test_7_coordinate():
    c = lc.Coordinate(6, 8)
    origin = lc.Coordinate(0,0)
    assert c.x == 6
    assert c.y == 8
    assert c.distance(origin) == 10
    assert origin.distance(c) == 10


def test_7_intset():
    s = lc.intSet()
    s.insert(7)
    s.insert(9)
    assert s.member(7)
    assert s.member(9)
    assert not s.member(10)
    s.remove(7)
    assert not s.member(7)
    assert s.member(9)
