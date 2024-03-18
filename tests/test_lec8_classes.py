import add_path
import mit_ocw_exercises.lec8_classes as lc

def test_5_frac():
    quarter = lc.Fraction(1, 4)
    half = lc.Fraction(1,2)
    assert quarter.num == 1
    assert quarter.denom == 4
    sum = half.__add__(quarter)
    assert sum.num == 6
    assert sum.denom == 8
    
#def test_coordinate():
#    c = lc.Coordinate(3, 4)
#    origin = lc.Coordinate(0,0)
#    assert c.x == 3
#    assert c.y == 4
#    assert c.distance(origin) == 5
#    assert origin.distance(c) == 5

#def test_intset():
#    s = lc.intSet()
#    s.insert(3)
#   s.insert(4)
#    assert s.member(3)
#    assert s.member(4)
#    assert not s.member(5)
#    s.remove(3)
#    assert not s.member(3)
#    assert s.member(4)

