import add_path
import mit_ocw_exercises.lec8_classes as lc

def test_coordinate():
    c = lc.Coordinate(5, 12)
    origin = lc.Coordinate(0,0)
    assert c.x == 5
    assert c.y == 12
    assert c.distance(origin) == 13
    assert origin.distance(c) == 13

def test_intset():
    s = lc.intSet()
    s.insert(5)
    s.insert(6)
    assert s.member(5)
    assert s.member(6)
    assert not s.member(7)
    s.remove(5)
    assert not s.member(5)
    assert s.member(6)
