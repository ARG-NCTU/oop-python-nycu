import pytest, random
import math

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
@pytest.fixture
def field():
    return Field()
@pytest.fixture
def usual_drunk():
    return UsualDrunk("Usual Drunk")
@pytest.fixture
def masochist_drunk():
    return MasochistDrunk("Masochist Drunk")
@pytest.fixture
def location():
    return Location(0, 0)
@pytest.fixture
def drunk():
    return Drunk("Test Drunk")
@pytest.fixture
def drunk_location():
    return Location(1, 1)


def test_add_drunk(field, usual_drunk, location):
    field.add_drunk(usual_drunk, location)
    assert field.drunks[usual_drunk] == location
    with pytest.raises(ValueError):
        field.add_drunk(usual_drunk, location)

def test_move_drunk(field, usual_drunk, location, drunk):
    field.add_drunk(usual_drunk, location)
    initial_location = field.get_loc(usual_drunk)
    field.move_drunk(usual_drunk)
    final_location = field.get_loc(usual_drunk)
    assert final_location != initial_location
    with pytest.raises(ValueError):
        field.move_drunk(drunk)

def test_get_loc(field, usual_drunk, location, drunk):
    field.add_drunk(usual_drunk, location)
    assert field.get_loc(usual_drunk) == location
    with pytest.raises(ValueError):
        field.get_loc(drunk)

def test_location_move(location):
    new_location = location.move(1, 1)
    assert new_location.get_x() == 1
    assert new_location.get_y() == 1
    assert location.get_x() == 0
    assert location.get_y() == 0

def test_location_dist_from(location, drunk_location):
    expected_distance = math.sqrt((1 - 0)**2 + (1 - 0)**2)
    assert location.dist_from(drunk_location) == pytest.approx(expected_distance)
    assert drunk_location.dist_from(location) == pytest.approx(expected_distance)

def test_location_str(location, drunk_location):
    assert str(location) == "<0, 0>"
    assert str(drunk_location) == "<1, 1>"

def test_drunk_str(drunk):
    assert str(drunk) == "Test Drunk"
    assert str(Drunk()) == "Anonymous"

def test_usual_drunk(usual_drunk):
    for _ in range(10):
        step = usual_drunk.take_step()
        assert step in [(0, 1), (0, -1), (1, 0), (-1, 0)]

def test_masochist_drunk(masochist_drunk):
    for _ in range(10):
        step = masochist_drunk.take_step()
        assert step in [(0.0, 1.1), (0.0, -0.9), (1.0, 0.0), (-1.0, 0.0)]

def test_drunk_location_fixture(drunk_location):
    assert drunk_location.get_x() == 1
    assert drunk_location.get_y() == 1
    assert str(drunk_location) == "<1, 1>"

def test_drunk_str_fixture(drunk):
    assert str(drunk) == "Test Drunk"
    assert str(Drunk()) == "Anonymous"

def test_drunk_move_fixture(drunk_location):
    initial_x = drunk_location.get_x()
    initial_y = drunk_location.get_y()
    delta_x = 1
    delta_y = 1
    new_location = drunk_location.move(delta_x, delta_y)
    assert new_location.get_x() == initial_x + delta_x
    assert new_location.get_y() == initial_y + delta_y
    assert drunk_location.get_x() == initial_x
    assert drunk_location.get_y() == initial_y

def test_drunk_dist_from_fixture(drunk_location):
    assert drunk_location.dist_from(drunk_location) == 0
    other_location = Location(2, 2)
    expected_distance = math.sqrt((2 - 1)**2 + (2 - 1)**2)
    assert drunk_location.dist_from(other_location) == pytest.approx(expected_distance)
    origin = Location(0, 0)
    expected_distance_origin = math.sqrt((0 - 1)**2 + (0 - 1)**2)
    assert drunk_location.dist_from(origin) == pytest.approx(expected_distance_origin)