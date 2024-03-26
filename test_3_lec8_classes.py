import add_path
import mit_ocw_exercises.lec8_classes as lc
def test_3_intset():
    s = lc.intSet
    s.insert(5)
    s.insert(6)
    assert s.member(5)
    assert s.member(6)
    assert not s.member(7)
    s.remove(6)
    assert not s.member(6)
    assert s.member(5)
