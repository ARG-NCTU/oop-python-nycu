import pytest
from random import seed
import random
import math
# from lec5_module import walk, sim_walks, UsualDrunk, MasochistDrunk, Field, Location

# set line width
import pylab
pylab.rcParams['lines.linewidth'] = 4
# set font size for titles
pylab.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
# set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
# set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
# set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
# set size of markers, e.g., circles representing points
# set numpoints for legend
pylab.rcParams['legend.numpoints'] = 1


class Location:
    def __init__(self, x, y):
        """x and y are numbers"""
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        """delta_x and delta_y are numbers"""
        return Location(self.x + delta_x, self.y + delta_y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def dist_from(self, other):
        x_dist = self.x - other.get_x()
        y_dist = self.y - other.get_y()
        return math.sqrt(x_dist ** 2 + y_dist ** 2)

    def __str__(self):
        return f"<{self.x}, {self.y}>"


class Field:
    def __init__(self):
        self.drunks = {}

    def add_drunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def move_drunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        x_dist, y_dist = drunk.take_step()
        # use move method of Location to get new location
        self.drunks[drunk] = self.drunks[drunk].move(x_dist, y_dist)

    def get_loc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

class Drunk:
    def __init__(self, name=None):
        """Assumes name is a str"""
        self.name = name

    def __str__(self):
        if self.name is not None:
            return self.name
        return 'Anonymous'

class UsualDrunk(Drunk):
    def take_step(self):
        step_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(step_choices)

class MasochistDrunk(Drunk):
    def take_step(self):
        step_choices = [(0.0, 1.1), (0.0, -0.9),
                        (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)

def walk(f, d, num_steps):
    """Assumes: f a Field, d a Drunk in f, and num_steps an int >= 0.
       Moves d num_steps times, and returns the distance between
       the final location and the location at the start of the
       walk."""
    start = f.get_loc(d)
    for _ in range(num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))

def sim_walks(num_steps, num_trials, d_class):
    """Assumes num_steps an int >= 0, num_trials an int > 0,
         d_class a subclass of Drunk
       Simulates num_trials walks of num_steps steps each.
       Returns a list of the final distances for each trial"""
    distances = []
    for _ in range(num_trials):
        homer = d_class('Homer')
        origin = Location(0, 0)
        f = Field()
        f.add_drunk(homer, origin)
        distances.append(walk(f, homer, num_steps))
    return distances

def test_walk():
    # Test the walk function with a simple case
    f = Field()
    d = UsualDrunk('Test Drunk')
    loc = Location(0, 0)
    f.add_drunk(d, loc)

    # Simulate a walk of 1 step
    distance = walk(f, d, 1)

    # Check if the distance is within expected range for one step
    assert distance in [1.0, pytest.approx(1.0)], "Distance for one step should be 1.0"

def test_sim_walks():
    # Test the sim_walks function with a simple case
    num_steps = 5
    num_trials = 3
    distances = sim_walks(num_steps, num_trials, UsualDrunk)

    # Check if the number of distances returned is equal to num_trials
    assert len(distances) == num_trials, "Number of trials mismatch"

    # Check if all distances are non-negative
    for distance in distances:
        assert distance >= 0, "Distance should be non-negative"

def test_location():
    # Test the Location class
    loc1 = Location(3, 4)
    loc2 = Location(0, 0)

    # Test move method
    new_loc = loc1.move(1, 1)
    assert new_loc.get_x() == 4 and new_loc.get_y() == 5, "Move method failed"
    assert loc1.get_x() == 3 and loc1.get_y() == 4, "Original location should not be modified"

    # Test dist_from method
    distance = loc1.dist_from(loc2)
    assert distance == pytest.approx(5.0), "Distance calculation failed"

    # Test string representation
    assert str(loc1) == "<3, 4>", "String representation failed"

def test_field():
    # Test the Field class
    field = Field()
    loc = Location(0, 0)
    drunk = UsualDrunk('Test Drunk')

    # Add a drunk to the field
    field.add_drunk(drunk, loc)

    # Check if the drunk is in the field
    assert field.get_loc(drunk) == loc, "Drunk location mismatch"

    # Move the drunk and check new location
    initial_loc = field.get_loc(drunk)
    field.move_drunk(drunk)
    new_loc = field.get_loc(drunk)
    assert new_loc != initial_loc, "Drunk did not move"

    # Test error handling for duplicate drunks
    with pytest.raises(ValueError):
        field.add_drunk(drunk, Location(1, 1))

    # Test error handling for moving a drunk not in the field
    new_drunk = UsualDrunk('New Drunk')
    with pytest.raises(ValueError):
        field.move_drunk(new_drunk)

    # Test get_loc for a drunk not in the field
    with pytest.raises(ValueError):
        field.get_loc(new_drunk)

def test_drunk():
    # Test the Drunk class
    drunk = Drunk('Test Drunk')

    # Test string representation
    assert str(drunk) == "Test Drunk", "String representation failed"

    # Test anonymous drunk
    anonymous_drunk = Drunk()
    assert str(anonymous_drunk) == "Anonymous", "Anonymous string representation failed"

def test_usual_drunk():
    # Test the UsualDrunk class
    drunk = UsualDrunk('Test Drunk')

    # Test taking a step
    for _ in range(10):
        step = drunk.take_step()
        assert step in [(0, 1), (0, -1), (1, 0), (-1, 0)], "Step not in expected choices"

def test_masochist_drunk():
    # Test the MasochistDrunk class
    drunk = MasochistDrunk('Test Drunk')

    # Test taking a step
    for _ in range(10):
        step = drunk.take_step()
        assert step in [(0.0, 1.1), (0.0, -0.9), (1.0, 0.0), (-1.0, 0.0)], "Step not in expected choices"