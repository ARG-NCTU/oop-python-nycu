import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import add_path
import numpy as np
from src.mit_ocw_data_science.lec5.lec5_module import Location, Field ,Drunk , UsualDrunk, MasochistDrunk, StyleIterator , walk , sim_walks , sim_drunk

def test_location():
    loc = Location(3, 4)
    assert loc.get_x() == 3
    assert loc.get_y() == 4
    loc2 = loc.move(1, -2)
    assert loc2.get_x() == 4
    assert loc2.get_y() == 2
    assert str(loc) == "<3, 4>"
    #assert loc.distance(loc2) == np.sqrt(5)

def test_field_and_drunk():
    f = Field()
    d = UsualDrunk("TestDrunk")
    loc = Location(0, 0)
    f.add_drunk(d, loc)
    assert f.get_loc(d) == loc
    f.move_drunk(d)
    new_loc = f.get_loc(d)
    assert new_loc != loc

def test_walk():
    f = Field()
    d = UsualDrunk("Walker")
    loc = Location(0, 0)
    f.add_drunk(d, loc)
    distance = walk(f, d, 10)
    assert distance >= 0

def test_sim_walks():
    distances = sim_walks(10, 5, UsualDrunk)
    assert len(distances) == 5
    for dist in distances:
        assert dist >= 0
    
def test_sim_drunk():
    walk_lengths = [10, 100, 1000]
    mean_distances = sim_drunk(5, UsualDrunk, walk_lengths)
    assert len(mean_distances) == len(walk_lengths)
    for mean in mean_distances:
        assert mean >= 0
