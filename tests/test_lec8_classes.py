import add_path
import mit_ocw_exercises.lec8_classes as lc

def test_9_coordinate():
    c = lc.Coordinate(6,8)
    origin = lc.Coordinate(0,0)
    assert c.x == 6
    assert c.y == 8
    assert c.distance(origin) == 10
    assert origin.distance(c) == 10

def test_9_intset():
    s = lc.intSet()
    s.insert(8)
    s.insert(7)
    assert s.member(8)
    assert s.member(7)
    s.remove(8)
    assert not s.member(8)
    assert s.member(7)

