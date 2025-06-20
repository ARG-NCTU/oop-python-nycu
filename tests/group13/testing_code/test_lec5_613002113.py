import practice.lec5_module as lec5
import pytest
import random

def test_position():
    position1 = lec5.Location(3, 4)
    position2 = lec5.Location(0, 0)
    
    assert position1.get_x() == 3
    assert position1.get_y() == 4
    assert position1.dist_from(position2) == pytest.approx(5.0)
    assert str(position1) == "<3, 4>"
    
    position3 = position1.move(1, -1)
    assert position3.get_x() == 4
    assert position3.get_y() == 3
    assert position1.dist_from(position3) == pytest.approx(1.4142135623730951)
    assert position3.dist_from(position1) == pytest.approx(1.4142135623730951)

def test_playground():
    playground = lec5.Field()
    position1 = lec5.Location(3, 4)
    position2 = lec5.Location(0, 0)
    
    wanderer1 = lec5.UsualDrunk("Walker1")
    wanderer2 = lec5.UsualDrunk("Walker2")
    
    playground.add_drunk(wanderer1, position1)
    playground.add_drunk(wanderer2, position2)
    
    assert playground.get_loc(wanderer1) == position1
    assert playground.get_loc(wanderer2) == position2
    
    playground.move_drunk(wanderer1)
    playground.move_drunk(wanderer2)
    
    assert playground.get_loc(wanderer1) != position1
    assert playground.get_loc(wanderer2) != position2
    
    with pytest.raises(ValueError, match='Duplicate drunk'):
        playground.add_drunk(wanderer1, position1)
    
    with pytest.raises(ValueError, match='Drunk not in field'):
        playground.move_drunk(lec5.UsualDrunk("Walker3"))

def test_walker():
    walker = lec5.UsualDrunk("Walker1")
    assert str(walker) == "Walker1"
    
    walker2 = lec5.UsualDrunk()
    assert str(walker2) == 'Anonymous'
    
    step = walker.take_step()
    assert step in [(0, 1), (0, -1), (1, 0), (-1, 0)]

def test_random_walker():
    walker = lec5.UsualDrunk("Walker1")
    assert str(walker) == "Walker1"
    
    walker2 = lec5.UsualDrunk()
    assert str(walker2) == 'Anonymous'
    
    step = walker.take_step()
    assert step in [(0, 1), (0, -1), (1, 0), (-1, 0)]