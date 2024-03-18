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
    



def test_1_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5
  
    a = lc.Coordinate(5, 12)
    origin = lc.Coordinate(0,0)
    assert a.x == 5
    assert a.y == 12
    assert a.distance(origin) == 13
    assert origin.distance(a) == 13
  
    b = lc.Coordinate(9, 40)    
    origin = lc.Coordinate(0,0)    
    assert b.x == 9    
    assert b.y == 40
    assert b.distance(origin) == 41   
    assert origin.distance(b) == 41 


def test_1_intset():  
    s = lc.intSet()
    s.insert(3)
    s.insert(4)
    assert s.member(3)
    assert s.member(4)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)
    assert s.member(4)
    s.insert(7)
    assert s.member(7)
    s.remove(7)
    assert not s.member(7)
    assert not s.member(9)

