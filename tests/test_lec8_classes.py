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

def test_13_coordinate():
    c = lc.Coordinate(14, 48)
    origin = lc.Coordinate(0,0)
    assert c.x == 14
    assert c.y == 48
    assert c.distance(origin) == 50
    assert origin.distance(c) == 50
    
    c = lc.Coordinate(3, 11)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 11
    assert c.distance(origin) == 11.40175425099138
    assert origin.distance(c) == 11.40175425099138
