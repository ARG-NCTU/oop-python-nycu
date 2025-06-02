import pytest
#rom lec5_module import Location

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
    
    def __eq__(self, other):
        if isinstance(other, Location):
            return self.x == other.x and self.y == other.y
        return False
    def __ne__(self, other):
        if isinstance(other, Location):
            return not self.__eq__(other)
        return True
def test_location():
    # Test the Location class
    loc1 = Location(0, 0)
    assert loc1.get_x() == 0
    assert loc1.get_y() == 0

    loc2 = Location(1, 1)
    assert loc2.get_x() == 1
    assert loc2.get_y() == 1

    loc3 = loc1.move(2, 3)
    assert loc3.get_x() == 2
    assert loc3.get_y() == 3

    loc4 = loc2.move(-1, -1)
    assert loc4.get_x() == 0
    assert loc4.get_y() == 0

    assert loc1.dist_from(loc2) == pytest.approx(1.41421356237, rel=1e-9)
    assert loc1.dist_from(loc3) == pytest.approx(3.60555127546, rel=1e-9)
    assert loc2.dist_from(loc3) == pytest.approx(2.23606797749, rel=1e-9)

    assert str(loc1) == '<0, 0>'
    assert str(loc2) == '<1, 1>'
    assert str(loc3) == '<2, 3>'
    assert str(loc4) == '<0, 0>'
def test_location_move():
    loc1 = Location(0, 0)
    loc2 = loc1.move(2, 3)
    assert loc2.get_x() == 2
    assert loc2.get_y() == 3

    loc3 = loc1.move(-1, -1)
    assert loc3.get_x() == -1
    assert loc3.get_y() == -1

    loc4 = loc2.move(-2, -3)
    assert loc4.get_x() == 0
    assert loc4.get_y() == 0

def test_location_str():
    loc1 = Location(0, 0)
    loc2 = Location(1, 1)
    loc3 = Location(2, 3)
    loc4 = Location(-1, -1)
    assert str(loc1) == '<0, 0>'
    assert str(loc2) == '<1, 1>'
    assert str(loc3) == '<2, 3>'
    assert str(loc4) == '<-1, -1>'
def test_location_equality():
    loc1 = Location(0, 0)
    loc2 = Location(0, 0)
    loc3 = Location(1, 1)
    loc4 = Location(2, 3)
    assert loc1 == loc2
    assert loc1 != loc3
    assert loc1 != loc4
    assert loc2 != loc3
    assert loc2 != loc4
    assert loc3 != loc4
def test_location_inequality():
    loc1 = Location(0, 0)
    loc2 = Location(1, 1)
    loc3 = Location(2, 3)
    loc4 = Location(-1, -1)
    assert loc1 != loc2
    assert loc1 != loc3
    assert loc1 != loc4
    assert loc2 != loc3
    assert loc2 != loc4
    assert loc3 != loc4
def test_location_move_negative():
    loc1 = Location(0, 0)
    loc2 = loc1.move(-2, -3)
    assert loc2.get_x() == -2
    assert loc2.get_y() == -3

    loc3 = loc1.move(1, 1)
    assert loc3.get_x() == 1
    assert loc3.get_y() == 1

    loc4 = loc2.move(2, 3)
    assert loc4.get_x() == 0
    assert loc4.get_y() == 0
def test_location_move_zero():
    loc1 = Location(0, 0)
    loc2 = loc1.move(0, 0)
    assert loc2.get_x() == 0
    assert loc2.get_y() == 0

    loc3 = loc1.move(1, 1)
    assert loc3.get_x() == 1
    assert loc3.get_y() == 1

    loc4 = loc2.move(-1, -1)
    assert loc4.get_x() == -1
    assert loc4.get_y() == -1
def test_location_move_large():
    loc1 = Location(0, 0)
    loc2 = loc1.move(1000000, 1000000)
    assert loc2.get_x() == 1000000
    assert loc2.get_y() == 1000000

    loc3 = loc1.move(-1000000, -1000000)
    assert loc3.get_x() == -1000000
    assert loc3.get_y() == -1000000

    loc4 = loc2.move(-1000000, -1000000)
    assert loc4.get_x() == 0
    assert loc4.get_y() == 0