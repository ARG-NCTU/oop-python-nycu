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
    c = lc.Coordinate(8,6)
    origin = lc.Coordinate(0,0)
    assert c.x == 8
    assert c.y == 6
    assert c.distance(origin) == 10
    assert origin.distance(c) == 10

def test_7_intset():
    s = lc.intSet()
    s.insert(8)
    s.insert(6)
    assert s.member(8)
    assert s.member(6)
    assert not s.member(10)
    s.remove(8)
    assert not s.member(8)
    assert s.member(6)
