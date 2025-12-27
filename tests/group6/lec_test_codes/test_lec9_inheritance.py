import lec_test_codes.add_path
import mit_ocw_exercises.lec9_inheritance as l9
import pytest

def test_animal_basic():
    a = l9.Animal(4)
    assert a.get_age() == 4
    assert a.get_name() is None
    a.set_name("test_animal_a")
    assert a.get_name() == "test_animal_a"
    a.set_age(10)
    assert a.get_age() == 10
    assert "animal:test_animal_a:10" == str(a)

def test_cat_inheritance(capsys):
    b = l9.Cat(5)
    b.set_name("test_animal_b")
    assert str(b) == "cat:test_animal_b:5"
    b.speak()
    captured = capsys.readouterr()
    assert "meow" in captured.out

def test_person_methods(capsys):
    p1 = l9.Person("P1", 101)
    p2 = l9.Person("P2", 102)
    assert p1.get_name() == "P1"
    assert p2.get_age() == 102
    p1.add_friend("Nobody")
    assert p1.get_friends() == ["Nobody"]
    p1.speak()
    captured = capsys.readouterr()
    assert "hello" in captured.out
    p1.age_diff(p2)
    captured = capsys.readouterr()
    assert "1 year difference" in captured.out
    assert "person:P1:101" == str(p1)

def test_rabbit_creation_and_addition():
    l9.Rabbit.tag = 1  # reset counter for test reproducibility
    r1 = l9.Rabbit(3)
    r2 = l9.Rabbit(4)
    r3 = l9.Rabbit(5)
    assert r1.get_rid() == "001"
    assert r2.get_rid() == "002"
    assert r3.get_rid() == "003"
    assert r1.get_parent1() is None
    assert r1.get_parent2() is None

    r4 = r1 + r2
    assert r4.get_parent1() is r1
    assert r4.get_parent2() is r2
    '''
      這裡不能用 "==" 來比較兩隻兔子是否相同，因為我們在 Rabbit class 裡面定義的 __eq__ 方法中，若父母其中一方是 None，則會回傳 False
      而 r1 和 r2 的父母都是 None。
      def __eq__(self, other):
        if self.parent1 is None or self.parent2 is None or \
        other.parent1 is None or other.parent2 is None:
            return False
        parents_same = self.parent1.rid == other.parent1.rid \
                    and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
                        and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite
    '''
    assert isinstance(r4, l9.Rabbit)
    
def test_rabbit_equality():
    l9.Rabbit.tag = 10  # reset again
    r1 = l9.Rabbit(1)
    r2 = l9.Rabbit(2)
    r3 = l9.Rabbit(3)
    r4 = r1 + r2
    r5 = r3 + r4
    r6 = r4 + r3
    # r5 and r6 should have same parents (but swapped)
    assert r5 == r6
    # r4 and r6 should not have same parents
    assert not (r4 == r6)