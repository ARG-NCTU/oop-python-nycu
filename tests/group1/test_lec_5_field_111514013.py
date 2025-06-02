import pytest
import random
#from lec5_module import Field,  Drunk, UsualDrunk, Location


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
        return (x_dist ** 2 + y_dist ** 2) ** 0.5

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
        if self is not None:
            return self.name
        return 'Anonymous'

class UsualDrunk(Drunk):
    def take_step(self):
        step_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(step_choices)

def test_field():
    # Test adding a drunk
    f = Field()
    d = Drunk("Bob")
    loc = Location(0, 0)
    f.add_drunk(d, loc)
    assert f.get_loc(d) == loc

    # Test moving a drunk
    d.take_step = lambda: (1, 0)
    f.move_drunk(d)
    assert f.get_loc(d).get_x() == 1

    # Test adding a duplicate drunk
    try:
        f.add_drunk(d, loc)
    except ValueError as e:
        assert str(e) == "Duplicate drunk"

    # Test moving a drunk not in the field
    d2 = Drunk("Alice")
    try:
        f.move_drunk(d2)
    except ValueError as e:
        assert str(e) == "Drunk not in field"
