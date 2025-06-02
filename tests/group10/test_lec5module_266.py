import practice.lec5_module as lec5
import pytest
import random

def test_location():
    # test Location class
    # test __init__, get_x, get_y, dist_from, __str__, move
    loc1 = lec5.Location(3, 4)
    loc2 = lec5.Location(0, 0)
    
    assert loc1.get_x() == 3
    assert loc1.get_y() == 4
    assert loc1.dist_from(loc2) == pytest.approx(5.0)
    assert str(loc1) == "<3, 4>"
    
    loc3 = loc1.move(1, -1)
    assert loc3.get_x() == 4
    assert loc3.get_y() == 3
    assert loc1.dist_from(loc3) == pytest.approx(1.4142135623730951)
    assert loc3.dist_from(loc1) == pytest.approx(1.4142135623730951)

def test_field():
    # test Field class
    # test add_drunk, move_drunk, get_loc
    field = lec5.Field()
    loc1 = lec5.Location(3, 4)
    loc2 = lec5.Location(0, 0)
    
    drunk1 = lec5.UsualDrunk("Drunk1")
    drunk2 = lec5.UsualDrunk("Drunk2")
    
    field.add_drunk(drunk1, loc1)
    field.add_drunk(drunk2, loc2)
    
    assert field.get_loc(drunk1) == loc1
    assert field.get_loc(drunk2) == loc2
    
    field.move_drunk(drunk1)
    field.move_drunk(drunk2)
    
    assert field.get_loc(drunk1) != loc1
    assert field.get_loc(drunk2) != loc2

    # test ValueError for duplicate drunk
    with pytest.raises(ValueError, match='Duplicate drunk'):
        field.add_drunk(drunk1, loc1)
    # test ValueError for drunk not in field
    with pytest.raises(ValueError, match='Drunk not in field'):
        field.move_drunk(lec5.UsualDrunk("Drunk3"))

def test_drunk():
    # test Drunk class
    # test __str__
    drunk = lec5.UsualDrunk("Drunk1")
    assert str(drunk) == "Drunk1"
    
    drunk2 = lec5.UsualDrunk()
    assert str(drunk2) == 'Anonymous'
    
    # test take_step
    step = drunk.take_step()
    assert step in [(0, 1), (0, -1), (1, 0), (-1, 0)]

def test_usual_drunk():
    # test UsualDrunk class
    # test __str__
    drunk = lec5.UsualDrunk("Drunk1")
    assert str(drunk) == "Drunk1"
    
    drunk2 = lec5.UsualDrunk()
    assert str(drunk2) == 'Anonymous'
    
    # test take_step
    step = drunk.take_step()
    assert step in [(0, 1), (0, -1), (1, 0), (-1, 0)]

def test_walk():
    # test walk function
    # test walk function with 10 steps
    drunk = lec5.UsualDrunk("Drunk1")
    loc = lec5.Location(0, 0)
    field = lec5.Field()
    field.add_drunk(drunk, loc)
    
    for _ in range(10):
        field.move_drunk(drunk)
    
    final_loc = field.get_loc(drunk)
    assert final_loc.dist_from(loc) <= 10
    # test walk function with 100 steps
    for _ in range(100):
        field.move_drunk(drunk)
    final_loc = field.get_loc(drunk)
    assert final_loc.dist_from(loc) <= 100

def test_walk_sim():
    # test sim_walks function
    # test sim_walks function with 10 steps and 100 tr
    # ials
    num_steps = 10
    num_trials = 100
    drunk_class = lec5.UsualDrunk
    result = lec5.sim_walks(num_steps, num_trials, drunk_class)
    assert isinstance(result, list)
    assert len(result) == num_trials
    assert all(isinstance(x, float) for x in result)
    assert all(x >= 0 for x in result)
    assert all(x <= num_steps for x in result)





